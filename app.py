import streamlit as st

st.set_page_config(
    page_title="HomeMind",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed",
)
st.title("HomeMind")

st.sidebar.title("Settings", anchor="bottom")


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?", "avatar": "🏠"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"], avatar=msg.get("avatar")).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    st.session_state.messages.append(
        {"role": "assistant", "content": msg["content"], "avatar": "🏠"}
    )
    st.chat_message("assistant", avatar="🏠").write(msg["content"])
