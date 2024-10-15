import asyncio

import streamlit as st

from agent import HomeAgent

st.set_page_config(
    page_title="HomeMind",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed",
)
st.title("HomeMind")

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

agent = HomeAgent()

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?", "avatar": "🏠"}
    ]


for msg in st.session_state.messages:
    st.chat_message(msg["role"], avatar=msg.get("avatar")).write(msg["content"])


async def print_async_response(prompt):
    async for response in agent.get_response(prompt):
        st.session_state.messages[-1]["content"] += response
        st.chat_message(
            "assistant",
            avatar="🏠",
        ).write(response)


if prompt := st.chat_input():
    st.session_state.messages.append(
        {"role": "user", "content": prompt, "avatar": "🧑‍💻"}
    )
    st.chat_message("user", avatar="🧑‍💻").write(prompt)

    asyncio.run(print_async_response(prompt))
