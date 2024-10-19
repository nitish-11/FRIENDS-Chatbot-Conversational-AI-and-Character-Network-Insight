import spacy
from nltk.tokenize import sent_tokenize
import pandas as pd
import re
from ast import literal_eval



class NamedEntityRecognizer:
    def __init__(self):
        self.nlp_model = self.load_model()
        pass
    
    def get_ners(self):
        df = pd.read_csv('/content/merged_transcripts4.csv')
        df = df.dropna(subset=['Dialogue'])

        def clean_dialogue(text):
            # 1. Remove everything within braces or brackets {} or [] or ()
            text = re.sub(r'\[.*?\]|\{.*?\}|\(.*?\)', '', text)

            # 2. Remove everything before ] or } or )
            text = re.sub(r'.*[\]\}\)]', '', text)

            # 3. Remove everything after [, {, (
            text = re.sub(r'[\[\{\(].*', '', text)

            # 4. Remove all \n and other escape characters, including those in between
            text = text.replace('\n', ' ').strip()

            # 5. Remove extra spaces that may be left behind after removing \n
            text = re.sub(r'\s+', ' ', text)

            return text

        df['Dialogue'] = df['Dialogue'].apply(clean_dialogue)
        # Apply NER to the Dialogue column
        df['ners'] = df['Dialogue'].apply(get_ners_inference)




    def load_model():
        if spacy.prefer_gpu():
            print("Using GPU")
        else:
            print("Using CPU")
        nlp = spacy.load("en_core_web_trf")
        return nlp

    nlp_model = load_model()

        # Function to perform NER inference on dialogue
    def get_ners_inference(dialogue):
        script_sentences = sent_tokenize(dialogue)
        ner_output = []

        for sentence in script_sentences:
            doc = nlp_model(sentence)
            ners = set()

            for entity in doc.ents:
                if entity.label_ == "PERSON":
                    first_name = entity.text.split(" ")[0].strip()
                    ners.add(first_name)

            ner_output.append(ners)

            return ner_output

