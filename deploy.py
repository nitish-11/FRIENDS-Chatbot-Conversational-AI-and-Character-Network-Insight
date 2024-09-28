# import gradio as gr
# from friends_chracter_new import CharacterChatBot
# import os

# def chat_with_character_chatbot(message, history):
#     character_chatbot = CharacterChatBot("nitish-11/friends_Monica_trained_Llama-3-8B",
#                                          #data_path="merged_transcripts.xlsx",
#                                          huggingface_token = os.getenv('huggingface_token')
#                                          )

#     output = character_chatbot.chat(message, history)
#     output = output['content'].strip()
#     return output



# def main():
#     with gr.Blocks() as iface:

#         # Character Chatbot Section
#         with gr.Row():
#             with gr.Column():
#                 gr.HTML("<h1>Character Chatbot</h1>")
#                 gr.ChatInterface(chat_with_character_chatbot)


#     iface.launch(share=True)




# if __name__ == '__main__':
#     main()


#----------------------------------------------------------------------------------------------------------------------------------

# import gradio as gr
# from friends_chracter_new import CharacterChatBot
# import os

# def chat_with_character_chatbot(message, history):
#     character_chatbot = CharacterChatBot("nitish-11/friends_Ross_trained2_Llama-3-8B",
#                                          huggingface_token=os.getenv('huggingface_token')
#                                          )
#     output = character_chatbot.chat(message, history)
#     output = output['content'].strip()
#     return output

# def main():
#     with gr.Blocks() as iface:
#         # Header Section
#         with gr.Row():
#             gr.HTML("""
#                 <div style="text-align: center; padding: 20px; background-color: #f5f5f5; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
#                     <h1 style="font-family: 'Arial', sans-serif; color: #333;">Friends Character Chatbot</h1>
#                     <p style="font-size: 18px; color: #555;">Chat with your favorite Friends character</p>
#                 </div>
#             """)
        
#         # Chatbot Section
#         with gr.Row():
#             with gr.Column():
#                 gr.ChatInterface(fn=chat_with_character_chatbot)

#     iface.launch(share=True)

# if __name__ == '__main__':
#     main()

#----------------------------------------------------------------------------------------------------------------------------------






# import gradio as gr
# from friends_chracter_new.friend_character_chatbox import CharacterChatBot
# import os

# # Mapping of character names to their corresponding model paths
# character_models = {
#     "Ross": "nitish-11/friends_Ross_trained2_Llama-3-8B",
#     "Rachel": "nitish-11/friends_Rachel_trained_Llama-3-8B",
#     "Chandler": "nitish-11/friends_Chandler_trained_Llama-3-8B",
#     "Monica": "nitish-11/friends_Monica_trained_Llama-3-8B",
#     "Joey": "nitish-11/friends_Joey_trained_Llama-3-8B",
#     "Phoebe" : "nitish-11/friends_Phoebe_trained_Llama-3-8B"
# }




# def chat_with_character_chatbot(character, message, history):
#     character_chatbot = CharacterChatBot(character_models[character],
#                                          huggingface_token=os.getenv('huggingface_token'))
#     output = character_chatbot.chat(message, history)
#     output = output['content'].strip()
#     return output

# def main():
#     with gr.Blocks() as iface:
#         # Full-screen layout
#         with gr.Row(elem_id="header_row", equal_height=True):
#             gr.HTML("""
#                 <div style="text-align: center; padding: 20px; background-color: #f5f5f5; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
#                     <h1 style="font-family: 'Arial', sans-serif; color: #333;">Friends Character Chatbot</h1>
#                     <p style="font-size: 18px; color: #555;">Chat with your favorite Friends character</p>
#                 </div>
#             """)

#         # Character Selection and Chatbot Section
#         with gr.Row(elem_id="chat_row", equal_height=True):
#             with gr.Column():
#                 # Dropdown for character selection
#                 character_dropdown = gr.Dropdown(label="Choose a character", 
#                                                   choices=list(character_models.keys()), 
#                                                   value="Ross")
                
#                 # Chat Interface
#                 chat_interface = gr.ChatInterface(fn=lambda message, history: chat_with_character_chatbot(character_dropdown.value, message, history))
#                                                    #height=600,  # Set the chat window height
#                                                    #container=True)

#         # Link dropdown change to chat interface
#         character_dropdown.change(fn=lambda _: chat_interface.clear(), inputs=character_dropdown, outputs=chat_interface)

#     iface.launch(share=True)

# if __name__ == '__main__':
#     main()




#----------------------------------------------------------------------------------------------------------------




# import gradio as gr
# from friends_chracter_new.friend_character_chatbox import CharacterChatBot
# import os

# # Mapping of character names to their corresponding model paths
# character_models = {
#     "Rachel": "nitish-11/friends_Rachel_trained_Llama-3-8B",
#     "Ross": "nitish-11/friends_Ross_trained2_Llama-3-8B",
#     "Chandler": "nitish-11/friends_Chandler_trained_Llama-3-8B",
#     "Monica": "nitish-11/friends_Monica_trained_Llama-3-8B",
#     "Joey": "nitish-11/friends_Joey_trained_Llama-3-8B",
#     "Phoebe": "nitish-11/friends_Phoebe_trained_Llama-3-8B"
# }

# def chat_with_character_chatbot(character, message, history):

#     if character is None:
#      return "Please select a character before sending a message."

#     # Store the selected character name
#     selected_character = character

#     # Notify user of the character they are talking to
#     response_message = f"You are going to talk to {selected_character}. Let's begin!"

#     character_chatbot = CharacterChatBot(model_path= character_models[selected_character],
#                                          data_path="/content/data/merged_transcripts3.csv",
#                                          huggingface_token=os.getenv('huggingface_token'),
#                                          character_name=selected_character)  # Pass the character name here)
#     output = character_chatbot.chat(message, history)
#     output = output['content'].strip()
#     return output

# def main():
#     with gr.Blocks() as iface:
#         # Full-screen layout
#         with gr.Row(elem_id="header_row", equal_height=True):
#             gr.HTML("""<div style="text-align: center; padding: 20px; background-color: #f5f5f5; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
#                         <h1 style="font-family: 'Arial', sans-serif; color: #333;">Friends Character Chatbot</h1>
#                         <p style="font-size: 18px; color: #555;">Chat with your favorite Friends character</p>
#                         </div>""")

#         # Character Selection and Chatbot Section
#         with gr.Row(elem_id="chat_row", equal_height=True):
#             with gr.Column():
#                 # Dropdown for character selection
#                 # character_radio = gr.Radio(label="Choose a character", 
#                 #            choices=list(character_models.keys()))
#                 character_textbox = gr.Textbox(label="Enter the character's name", placeholder="e.g., Rachel, Ross, Monica, Phoebe, Joey, Chandler")
#                 submit_button = gr.Button("Submit")

#                 # Chat Interface
#                 chat_interface = gr.ChatInterface(fn=lambda message, history: chat_with_character_chatbot(character_textbox.value, message, history))

#                 # Clear chat history when the character name changes
#                 character_textbox.change(fn=lambda _: chat_interface.clear(), inputs=character_textbox, outputs=chat_interface)

#                 # Submit button action
#                 submit_button.click(fn=lambda message, history: chat_with_character_chatbot(character_textbox.value, message, history), 
#                                     inputs=[character_textbox, chat_interface], 
#                                     outputs=chat_interface)


#     iface.launch(share=True)

# if __name__ == '__main__':
#     main()








#-------------------------------------------------------------------------------------------------------------------------------------



# import gradio as gr
# from friends_chracter_new.friend_character_chatbox import CharacterChatBot
# import os

# # Mapping of character names to their corresponding model paths
# character_models = {
#     "Rachel": "nitish-11/friends_Rachel_trained_Llama-3-8B",
#     "Ross": "nitish-11/friends_Ross_trained2_Llama-3-8B",
#     "Chandler": "nitish-11/friends_Chandler_trained_Llama-3-8B",
#     "Monica": "nitish-11/friends_Monica_trained_Llama-3-8B",
#     "Joey": "nitish-11/friends_Joey_trained_Llama-3-8B",
#     "Phoebe": "nitish-11/friends_Phoebe_trained_Llama-3-8B"
# }


# def chat_with_character_chatbot(character, message, history):
#     # Check if the selected character is valid
#     if character not in character_models:
#         return "Please select a valid character before sending a message."

#     # Notify user of the character they are talking to
#     response_message = f"You are going to talk to {character}. Let's begin!"

#     character_chatbot = CharacterChatBot(model_path=character_models[character],
#                                          data_path="/content/data/merged_transcripts3.csv",
#                                          huggingface_token=os.getenv('huggingface_token'),
#                                          character_name=character)
#     output = character_chatbot.chat(message, history)
#     output = output['content'].strip()
#     return output


# def main():
#     with gr.Blocks() as iface:
#         # Full-screen layout
#         with gr.Row(elem_id="header_row", equal_height=True):
#             gr.HTML("""<div style="text-align: center; padding: 20px; background-color: #f5f5f5; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
#                         <h1 style="font-family: 'Arial', sans-serif; color: #333;">Friends Character Chatbot</h1>
#                         <p style="font-size: 18px; color: #555;">Chat with your favorite Friends character</p>
#                         </div>""")

#         # Character Selection and Chatbot Section
#         with gr.Row(elem_id="chat_row", equal_height=True):
#             with gr.Column():
#                 # Textbox for character selection
#                 character_textbox = gr.Textbox(label="Enter the character's name", placeholder="e.g., Rachel, Ross, Monica")

#                 # State to store the selected character
#                 selected_character = gr.State()

#                 # Submit Button
#                 submit_button = gr.Button("Submit")

#                 # Chat Interface
#                 chat_interface = gr.ChatInterface(fn=lambda message, history: chat_with_character_chatbot(selected_character.value, message, history))

#                 # Update the state with the selected character name
#                 character_textbox.change(fn=lambda character: character, inputs=character_textbox, outputs=selected_character)

#                 # Clear chat history when the character name changes
#                 character_textbox.change(fn=lambda _: chat_interface.clear(), inputs=character_textbox, outputs=chat_interface)

#                 # Submit button action
#                 submit_button.click(fn=lambda message, history: chat_with_character_chatbot(selected_character.value, message, history), 
#                                     inputs=[character_textbox, chat_interface], 
#                                     outputs=chat_interface)

#     iface.launch(share=True)

# if __name__ == '__main__':
#     main()









#----------------------------------------------------------------------------------------------------


# WORKING ------------***************
# import gradio as gr
# from friends_chracter_new.friend_character_chatbox import CharacterChatBot
# import os

# # Mapping of character names to their corresponding model paths
# character_models = {
#     "Rachel": "nitish-11/friends_Rachel_trained_Llama-3-8B",
#     "Ross": "nitish-11/friends_Ross_trained2_Llama-3-8B",
#     "Chandler": "nitish-11/friends_Chandler_trained_Llama-3-8B",
#     "Monica": "nitish-11/friends_Monica_trained_Llama-3-8B",
#     "Joey": "nitish-11/friends_Joey_trained_Llama-3-8B",
#     "Phoebe": "nitish-11/friends_Phoebe_trained_Llama-3-8B"
# }

# # Function to chat with the character chatbot
# def chat_with_character_chatbot(character, message, history):
#     if character is None:
#         return "Please select a character before sending a message.", history
    
#     if character not in character_models:
#         return "Character not recognized. Please enter a valid character.", history

#     # Initialize the chatbot with the selected character's model
#     character_chatbot = CharacterChatBot(model_path=character_models[character],
#                                          data_path="/content/data/merged_transcripts3.csv",
#                                          huggingface_token=os.getenv('huggingface_token'),
#                                          character_name=character)
    
#     # Generate the response from the chatbot
#     output = character_chatbot.chat(message, history)
#     response = output['content'].strip()
    
#     # Append the user message and bot response to the chat history
#     history.append((message, response))
    
#     return response, history

# # Main function for Gradio interface
# def main():
#     with gr.Blocks() as iface:
#         # Header
#         with gr.Row(elem_id="header_row", equal_height=True):
#             gr.HTML("""
#                 <div style="text-align: center; padding: 20px; background-color: #f5f5f5; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
#                     <h1 style="font-family: 'Arial', sans-serif; color: #333;">Friends Character Chatbot</h1>
#                     <p style="font-size: 18px; color: #555;">Chat with your favorite Friends character</p>
#                 </div>
#             """)

#         # Character selection and chat section
#         with gr.Row(elem_id="chat_row", equal_height=True):
#             with gr.Column():
#                 # Textbox for entering character name
#                 character_textbox = gr.Textbox(label="Enter the character's name", placeholder="e.g., Rachel, Ross, Monica, Phoebe, Joey, Chandler")

#                 # Textbox for user query (message)
#                 user_message = gr.Textbox(label="Your message", placeholder="Type your message here...")

#                 # Chatbot display
#                 chatbot = gr.Chatbot(label="Chat with the selected character", height=600)

#                 # Submit button to start the conversation
#                 submit_button = gr.Button("Submit")

#                 # Chat history state
#                 chat_history = gr.State([])

#                 # Function when user submits a message
#                 def process_input(character, message, history):
#                     # Get response from the chatbot
#                     response, updated_history = chat_with_character_chatbot(character, message, history)
#                     return updated_history, updated_history

#                 # Connect submit button to input processing
#                 submit_button.click(fn=process_input, 
#                                     inputs=[character_textbox, user_message, chat_history], 
#                                     outputs=[chatbot, chat_history])

#     iface.launch(share=True)

# if __name__ == '__main__':
#     main()






#------------------------------------------------------------------------------------------------------------------------------------


# import gradio as gr
# from friends_chracter_new.friend_character_chatbox import CharacterChatBot
# import os

# # Mapping of character names to their corresponding model paths
# character_models = {
#     "Rachel": "nitish-11/friends_Rachel_trained_Llama-3-8B",
#     "Ross": "nitish-11/friends_Ross_trained2_Llama-3-8B",
#     "Chandler": "nitish-11/friends_Chandler_trained_Llama-3-8B",
#     "Monica": "nitish-11/friends_Monica_trained_Llama-3-8B",
#     "Joey": "nitish-11/friends_Joey_trained_Llama-3-8B",
#     "Phoebe": "nitish-11/friends_Phoebe_trained_Llama-3-8B"
# }

# # Function to chat with the character chatbot
# def chat_with_character_chatbot(character, message, history):
#     if character is None:
#         return "Please select a character before sending a message.", history
    
#     if character not in character_models:
#         return "Character not recognized. Please enter a valid character.", history

#     # Initialize the chatbot with the selected character's model
#     character_chatbot = CharacterChatBot(model_path=character_models[character],
#                                          data_path="/content/data/merged_transcripts3.csv",
#                                          huggingface_token=os.getenv('huggingface_token'),
#                                          character_name=character)
    
#     # Generate the response from the chatbot
#     output = character_chatbot.chat(message, history)
#     response = output['content'].strip()
    
#     # Append the user message and bot response to the chat history
#     history.append((message, response))
    
#     return response, history

# # Main function for Gradio interface
# def main():
#     with gr.Blocks() as iface:
#         # Header
#         with gr.Row(elem_id="header_row", equal_height=True):
#             gr.HTML("""
#                 <div style="text-align: center; padding: 20px; background-color: #f5f5f5; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
#                     <h1 style="font-family: 'Arial', sans-serif; color: #333;">Friends Character Chatbot</h1>
#                     <p style="font-size: 18px; color: #555;">Chat with your favorite Friends character</p>
#                 </div>
#             """)

#         # Character selection and chat section
#         with gr.Row(elem_id="chat_row", equal_height=True):
#             with gr.Column():
#                 # Radio button for character selection
#                 character_radio = gr.Radio(label="Choose a character", choices=list(character_models.keys()), value=None)

#                 # Textbox for user query (message)
#                 user_message = gr.Textbox(label="Your message", placeholder="Type your message here...")

#                 # Chatbot display
#                 chatbot = gr.Chatbot(label="Chat with the selected character", height=600)

#                 # Submit button to start the conversation
#                 submit_button = gr.Button("Submit")

#                 # Chat history state
#                 chat_history = gr.State([])

#                 # Function when user submits a message
#                 def process_input(character, message, history):
#                     # Get response from the chatbot
#                     response, updated_history = chat_with_character_chatbot(character, message, history)
#                     return updated_history, updated_history

#                 # Function to reset the chat when character changes
#                 def reset_chat():
#                     return [], "", []  # Clear chat history, message input, and reset the chat_history state

#                 # Connect submit button to input processing
#                 submit_button.click(fn=process_input, 
#                                     inputs=[character_radio, user_message, chat_history], 
#                                     outputs=[chatbot, chat_history])

#                 # Reset chat history, input, and state when character changes
#                 character_radio.change(fn=reset_chat, 
#                                        inputs=[], 
#                                        outputs=[chatbot, user_message, chat_history])

#     iface.launch(share=True)

# if __name__ == '__main__':
#     main()




#------------------------------------------------------------
# without colores

import gradio as gr
from friends_chracter_new.friend_character_chatbox import CharacterChatBot
import os

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

# Main function for Gradio interface
def main():
    with gr.Blocks() as iface:
        # Static title for the page
        with gr.Row(elem_id="header_row", equal_height=True):
            gr.HTML("""<div style="text-align: center; padding: 20px; background-color: #f5f5f5; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
                        <h1 style="font-family: 'Arial', sans-serif; color: #333;">Friends Character Chatbot</h1>
                        </div>""")
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

    iface.launch(share=True)

if __name__ == '__main__':
    main()




#-------------------------------------------------------------------

import gradio as gr
from friends_chracter_new.friend_character_chatbox import CharacterChatBot
import os

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

# Main function for Gradio interface
def main():
    with gr.Blocks() as iface:
        # Stylish title for the page with colors and calligraphy
        with gr.Row(elem_id="header_row", equal_height=True):
            gr.HTML("""
                <div style="text-align: center; padding: 20px; background-color: #f0f8ff; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
                    <h1 style="font-family: 'Brush Script MT', cursive; color: #ff4500; font-size: 60px; letter-spacing: 2px;">
                        Friends Character Chatbot
                    </h1>
                    <p id="character-status" style="font-family: 'Georgia', serif; color: #2e8b57; font-size: 24px; margin-top: 5px;">
                        Chat with your favorite Friends character: <i>No character selected</i>
                    </p>
                </div>
            """)

        # Character selection section
        with gr.Row(elem_id="selection_row", equal_height=True):
            with gr.Column():
                # Radio button for character selection
                character_radio = gr.Radio(label="Choose a character", choices=list(character_models.keys()), value=None)

        # Textbox for user query (message) and submit button
        with gr.Row(elem_id="input_row", equal_height=True):
            user_message = gr.Textbox(label="Your message", placeholder="Type your message here...", elem_id="message_input", lines=3)
            submit_button = gr.Button("Submit", elem_id="submit_button", size="small")  # Small button size

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
            # Update the dynamic character status in the top bar
            status_message = f"Chat with your favorite Friends character: <i>{character}</i>"
            return [], "", [], gr.update(value=status_message, elem_id="character-status")

        # Connect submit button to input processing
        submit_button.click(fn=process_input, 
                            inputs=[character_radio, user_message, chat_history], 
                            outputs=[chatbot, chat_history])

        # Reset chat history, input, and state when character changes
        character_radio.change(fn=reset_chat, 
                               inputs=[character_radio], 
                               outputs=[chatbot, user_message, chat_history, gr.Markdown.update()])

    iface.launch(share=True)

if __name__ == '__main__':
    main()
