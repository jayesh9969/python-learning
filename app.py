import streamlit as st

from whatsapp_rag import res, response, q

st.title("Whatsapp info")

if "messages" not in st.session_state:
    st.session_state.messages = []

if user_query := st.chat_input("ask new group kasa banau"):
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

with st.spinner("thinking..."):
    ai_response = response.text.strip()


with st.chat_message("assistant"):
    st.markdown(ai_response)

st.session_state.messages.append({"role": "assistant", "content": ai_response})