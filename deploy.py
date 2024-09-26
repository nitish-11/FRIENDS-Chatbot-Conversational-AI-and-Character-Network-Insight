import gradio as gr
from friends_chracter_new import CharacterChatBot
import os




def chat_with_character_chatbot(message, history):
    character_chatbot = CharacterChatBot("nitish-11/friends_Chandler_trained_Llama-3-8B",
                                         #data_path="merged_transcripts.xlsx",
                                         huggingface_token = os.getenv('huggingface_token')
                                         )

    output = character_chatbot.chat(message, history)
    output = output['content'].strip()
    return output



def main():
    with gr.Blocks() as iface:

        # Character Chatbot Section
        with gr.Row():
            with gr.Column():
                gr.HTML("<h1>Character Chatbot</h1>")
                gr.ChatInterface(chat_with_character_chatbot)


    iface.launch(share=True)




if __name__ == '__main__':
    main()


