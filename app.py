
import streamlit as st

from whatsapp_rag import ask_whatsapp_rag

st.title("Whatsapp Instructions")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if user_query := st.chat_input("aapla whasapp related prashn vichara!"):

    with st.chat_message("user"):
        st.markdown(user_query)

    st.session_state.messages.append({"role" : "user", "content" : user_query})


    with st.spinner("Scanning database and consulting Gemini..."):
        try:
            # Run your actual RAG function using the query string
            ai_response = ask_whatsapp_rag(user_query)
        except Exception as e:
            ai_response = f"⚠️ System Error: {str(e)}"

    # Display the strict RAG response
    with st.chat_message("assistant"):
        st.markdown(ai_response)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})

