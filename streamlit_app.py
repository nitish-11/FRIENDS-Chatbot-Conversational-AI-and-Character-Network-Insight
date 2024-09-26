import streamlit as st
from friends_chracter_new import CharacterChatBot
import os

def chat_with_character_chatbot(message, history):
    # Initialize chatbot (replace with actual Hugging Face model path)
    character_chatbot = CharacterChatBot("nitish-11/friends_Ross_trained2_Llama-3-8B",
                                         huggingface_token=os.getenv('huggingface_token')
                                         )
    # Get chatbot response
    output = character_chatbot.chat(message, history)
    output = output['content'].strip()
    return output

def main():
    # Set up page title and layout
    st.set_page_config(page_title="Friends Character Chatbot", layout="centered")
    
    # App header
    st.title("Friends Character Chatbot")
    st.write("Chat with your favorite Friends character")

    # Initialize chat history
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    # User input
    user_input = st.text_input("You: ", placeholder="Type your message here...")

    # If user submits a message
    if user_input:
        with st.spinner("Character is typing..."):
            # Pass the message and chat history to the chatbot function
            bot_response = chat_with_character_chatbot(user_input, st.session_state['history'])
            
            # Append user message and bot response to the history
            st.session_state['history'].append(f"You: {user_input}")
            st.session_state['history'].append(f"Bot: {bot_response}")

    # Display chat history
    if st.session_state['history']:
        st.write("### Chat History")
        for msg in st.session_state['history']:
            st.write(msg)

if __name__ == '__main__':
    main()
