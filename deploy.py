import gradio as gr
from friends_chatbot.friend_character_chatbox import CharacterChatBot
import os
import pandas as pd

# Mapping of character names to their corresponding model paths
character_models = {
    "Rachel": "nitish-11/friends_Rachel_trained_Llama-3-8B",
    "Ross": "nitish-11/friends_Ross_trained2_Llama-3-8B",
    "Chandler": "nitish-11/friends_Chandler_trained_Llama-3-8B",
    "Monica": "nitish-11/friends_Monica_trained_Llama-3-8B",
    "Joey": "nitish-11/friends_Joey_trained_Llama-3-8B",
    "Phoebe": "nitish-11/friends_Phoebe_trained_Llama-3-8B"
}



# Function to chat with the character chatbot
def chat_with_character_chatbot(character, message, history):
    if character is None:
        return "Please select a character before sending a message.", history
    
    if character not in character_models:
        return "Character not recognized. Please enter a valid character.", history

    # Initialize the chatbot with the selected character's model
    character_chatbot = CharacterChatBot(model_path=character_models[character],
                                         data_path="/content/data/merged_transcripts3.csv",
                                         huggingface_token=os.getenv('huggingface_token'),
                                         character_name=character)
    
    # Generate the response from the chatbot
    output = character_chatbot.chat(message, history)
    response = output['content'].strip()
    
    # Append the user message and bot response to the chat history
    history.append((message, response))
    
    return response, history



def load_insight_html():
    # Load the character insight HTML file content
    with open("data/friends_character_insight.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    # Replace single quotes with double quotes for proper embedding
    html_content = html_content.replace("'", "\"")

    # Create iframe HTML with full page width and height adjustments
    output_html = f"""
    <iframe style="width: 100%; height: 1000px; margin: 0 auto; border: none;" 
    name="result" allow="midi; geolocation; microphone; camera; display-capture; 
    encrypted-media;" sandbox="allow-modals allow-forms allow-scripts allow-same-origin 
    allow-popups allow-top-navigation-by-user-activation allow-downloads" 
    allowfullscreen="" allowpaymentrequest="" frameborder="0" 
    srcdoc='{html_content}'></iframe>
    """
    
    return output_html


# Main function for Gradio interface
def main():
    with gr.Blocks() as iface:
        # Static title for the page
        with gr.Row(elem_id="header_row", equal_height=True):
            gr.HTML("""<div style="text-align: center; padding: 20px; background-color: #f5f5f5; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
                        <h1 style="font-family: 'Arial', sans-serif; color: #333;">Friends Character Chatbot</h1>
                        </div>""")

        # Create a tabbed interface
        with gr.Tab("Chatbot"):
            # Dynamic text for the selected character
            character_status = gr.Markdown("### Chat with your favorite Friends character: *No character selected*")

            # Character selection section
            with gr.Row(elem_id="selection_row", equal_height=True):
                with gr.Column():
                    # Radio button for character selection
                    character_radio = gr.Radio(label="Choose a character", choices=list(character_models.keys()), value=None)

            # Textbox for user query (message) and submit button
            with gr.Row(elem_id="input_row", equal_height=True):
                user_message = gr.Textbox(label="Your message", placeholder="Type your message here...")
                submit_button = gr.Button("Submit")

            # Chatbot display below the input section
            with gr.Row(elem_id="chat_row", equal_height=True):
                chatbot = gr.Chatbot(label="Chat with the selected character", height=600)

            # Chat history state
            chat_history = gr.State([])

            # Function when user submits a message
            def process_input(character, message, history):
                # Get response from the chatbot
                response, updated_history = chat_with_character_chatbot(character, message, history)
                return updated_history, updated_history

            # Function to reset the chat when character changes
            def reset_chat(character):
                # Update the dynamic character status
                status_message = f"### Chat with your favorite Friends character: *{character}*"
                return [], "", [], status_message  # Reset chat history, message input, and update the status

            # Connect submit button to input processing
            submit_button.click(fn=process_input, 
                                inputs=[character_radio, user_message, chat_history], 
                                outputs=[chatbot, chat_history])

            # Reset chat history, input, and state when character changes
            character_radio.change(fn=reset_chat, 
                                   inputs=[character_radio], 
                                   outputs=[chatbot, user_message, chat_history, character_status])




        with gr.Tab("Character Network"):
            # Title of the section
            gr.Markdown("<h1 style='text-align:center'>Character Insight</h1>")
            
            # Show character insight button and iframe
            with gr.Row():
                load_insight_button = gr.Button("Show Character Insight", scale=1)
            
            # Separate row for the iframe to make sure it occupies the entire width
            with gr.Row():
                insight_html = gr.HTML()  # Placeholder for the iframe HTML
                
            # Button action loads the HTML into the iframe container
            load_insight_button.click(load_insight_html, outputs=[insight_html])

                    # # Display the insight HTML below the button
                    # insight_html.render()
                                    #get_network_graph_button.click(get_character_network, inputs=[subtitles_path,ner_path], outputs=[network_html])



    iface.launch(share=True)

if __name__ == '__main__':
    main()


