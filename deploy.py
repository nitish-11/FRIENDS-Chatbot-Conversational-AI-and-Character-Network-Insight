# import gradio as gr
# from friends_chracter_new import CharacterChatBot
# import os

# def chat_with_character_chatbot(message, history):
#     character_chatbot = CharacterChatBot("nitish-11/friends_Ross_trained2_Llama-3-8B",
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

def chat_with_character_chatbot(character, message, history):
    character_chatbot = CharacterChatBot(model_path= character_models[character],
                                         data_path="/content/data/merged_transcripts3.csv",
                                         huggingface_token=os.getenv('huggingface_token'),
                                         character_name=character)  # Pass the character name here)
    output = character_chatbot.chat(message, history)
    output = output['content'].strip()
    return output

def main():
    with gr.Blocks() as iface:
        # Full-screen layout
        with gr.Row(elem_id="header_row", equal_height=True):
            gr.HTML("""<div style="text-align: center; padding: 20px; background-color: #f5f5f5; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
                        <h1 style="font-family: 'Arial', sans-serif; color: #333;">Friends Character Chatbot</h1>
                        <p style="font-size: 18px; color: #555;">Chat with your favorite Friends character</p>
                        </div>""")

        # Character Selection and Chatbot Section
        with gr.Row(elem_id="chat_row", equal_height=True):
            with gr.Column():
                # Dropdown for character selection
                character_dropdown = gr.Dropdown(label="Choose a character", 
                                                  choices=list(character_models.keys()), 
                                                  value="Chandler")
                
                # Chat Interface
                chat_interface = gr.ChatInterface(fn=lambda message, history: chat_with_character_chatbot(character_dropdown.value, message, history))

        # Link dropdown change to chat interface
        character_dropdown.change(fn=lambda _: chat_interface.clear(), inputs=character_dropdown, outputs=chat_interface)

    iface.launch(share=True)

if __name__ == '__main__':
    main()
