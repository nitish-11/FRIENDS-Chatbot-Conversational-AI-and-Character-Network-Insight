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




import gradio as gr
from friends_chracter_new import CharacterChatBot
import os

def chat_with_character_chatbot(message, history):
    character_chatbot = CharacterChatBot("nitish-11/friends_Ross_trained2_Llama-3-8B",
                                         huggingface_token=os.getenv('huggingface_token')
                                         )
    output = character_chatbot.chat(message, history)
    output = output['content'].strip()
    return output

def main():
    with gr.Blocks() as iface:
        # Full-screen layout
        with gr.Row(elem_id="header_row", equal_height=True):
            gr.HTML("""
                <div style="text-align: center; padding: 20px; background-color: #f5f5f5; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
                    <h1 style="font-family: 'Arial', sans-serif; color: #333;">Friends Character Chatbot</h1>
                    <p style="font-size: 18px; color: #555;">Chat with your favorite Friends character</p>
                </div>
            """)
        
        # Chatbot Section
        with gr.Row(elem_id="chat_row", equal_height=True):
            with gr.Column():
                gr.ChatInterface(fn=chat_with_character_chatbot, 
                                 height=600,  # Set the chat window height
                                 container=True)

    iface.launch(share=True)

if __name__ == '__main__':
    main()
