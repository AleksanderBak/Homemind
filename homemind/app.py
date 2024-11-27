import streamlit as st

from homemind.agent import Agent
from homemind.utils import to_sync_generator

st.set_page_config(
    page_title="HomeMind",
    page_icon="🧠",
    layout="centered",
)

st.markdown(
    """
    <style>
        .st-emotion-cache-janbn0 {
            flex-direction: row-reverse;
            text-align: right;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

llm_agent = Agent()

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?", "avatar": "🏠"}
    ]


for msg in st.session_state.messages:
    st.chat_message(msg["role"], avatar=msg.get("avatar")).write(msg["content"])


if prompt := st.chat_input():
    st.session_state.messages.append(
        {"role": "user", "content": prompt, "avatar": "🧑‍💻"}
    )
    st.chat_message("user", avatar="🧑‍💻").write(prompt)

    message = st.chat_message("assistant", avatar="🏠").write_stream(
        to_sync_generator(llm_agent.get_response(prompt))
    )

    st.session_state.messages.append(
        {"role": "assistant", "content": message, "avatar": "🏠"}
    )
