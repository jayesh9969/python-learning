import streamlit as st
import requests

import os

API_URL = os.getenv("API_URL","http://127.0.0.1:8000")



st.title("AI Job Matcher & Route Finder")

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if user_query := st.chat_input("Write your skills or resume summary"):
    with st.chat_message("user"):
        st.markdown(user_query)


    st.session_state.messages.append({"role": "user", "content" : user_query})

    with st.spinner("Analyzing with FastAPI & Supabase Vector DB..."):
        res = requests.post(f"{API_URL}/analyze", json={"profile": user_query})

        if res.status_code == 200:

            data = res.json()

            jobs = data["matched_jobs"]

            diagnosis = data["diagnosis"]


            job_cards = "### Top Matched Roles:\n\n"


            for job in jobs:

                job_cards += f"- ** {job['title']}** at *{job['company']}* | {job['salary']} | {job['competition']}\n"

            full_reply = f"{job_cards}\n\n---\n\n{diagnosis}"

    with st.chat_message("assistant"):
        st.markdown(full_reply)

    st.session_state.messages.append({"role" : "assistant", "content" : full_reply})





    