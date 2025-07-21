import streamlit as st
import requests
import uuid

st.set_page_config(page_title="Mental Health Chatbot")

st.title("🧠 Mental Health Support Chatbot")
session_id = str(uuid.uuid4())  # Unique session per user

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        # Call Flask backend
        res = requests.post("http://127.0.0.1:5000/chat", json={
            "message": user_input,
            "session_id": session_id
        })

        bot_response = res.json().get("response", "")
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", bot_response))

# Display conversation history
for sender, message in st.session_state.chat:
    if sender == "You":
        st.markdown(f"**🧍 You**: {message}")
    else:
        st.markdown(f"**🤖 Bot**: {message}")
