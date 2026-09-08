import streamlit as st
# Import the function we just created
from whatsapp_rag import ask_whatsapp_rag 

st.set_page_config(page_title="WhatsApp Guide Bot", page_icon="💬", layout="centered")
st.title("💬 WhatsApp Guide Assistant")
st.caption("Ask questions strictly based on the loaded WhatsApp installation guide context.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create the input text box and send button
if user_query := st.chat_input("Ask a question about the guide..."):
    
    # Display user's question
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    # Display a loading spinner while processing embeddings and RAG pipeline
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
