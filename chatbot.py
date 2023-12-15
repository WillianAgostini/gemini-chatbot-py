import streamlit as st
from streamlit_chat import message
from streamlit.components.v1 import html
from api import ask_question

def start():
    def on_input_change():
        user_input = st.session_state.user_input
        st.session_state.past.append(user_input)
        response = ask_question(user_input)
        st.session_state.generated.append({'type': 'normal', 'data': response})
        st.session_state.user_input = ""

    def on_btn_click():
        del st.session_state.past[:]
        del st.session_state.generated[:]

    st.title("Chat placeholder")

    if "generated" not in st.session_state:
        st.session_state["generated"] = []

    if "past" not in st.session_state:
        st.session_state["past"] = []

    chat_placeholder = st.empty()

    with chat_placeholder.container():    
        for i in range(len(st.session_state['generated'])):                
            message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
            print(st.session_state['past'])
            message(
                st.session_state['generated'][i]['data'], 
                key=f"{i}", 
                allow_html=True,
                is_table=True if st.session_state['generated'][i]['type']=='table' else False
            )

        st.button("Clear message", on_click=on_btn_click)

    with st.container():
        st.text_input("User Input:", on_change=on_input_change, key="user_input")

if __name__ == "__main__":
    start()