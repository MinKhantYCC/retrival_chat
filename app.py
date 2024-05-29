import streamlit as st
from chat import get_response
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
import nltk
nltk.download('punkt')

def clear_input_field():
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input = ""

def set_send_input():
    st.session_state.send_input = True
    clear_input_field()

def main():
    st.title("Simple Retrieval ChatBot")
    chat_container = st.container()

    if "send_input" not in st.session_state:
        st.session_state.send_input = False
        st.session_state.user_question = ""
    
    user_input = st.text_input("Type your message here: ", 
                               key="user_input",
                               on_change=set_send_input)
    send_button = st.button("Send", key="send_button")

    if send_button or st.session_state.send_input:
        if st.session_state.user_question != "":
            with chat_container:
                response = get_response(st.session_state.user_question)
                with st.chat_message("user"):
                    st.write(st.session_state.user_question)
                    st.session_state.user_question = ""
                message = st.chat_message("assistant")
                message.write(response)

if __name__ == "__main__":
    main()
