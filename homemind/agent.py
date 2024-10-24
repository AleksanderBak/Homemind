from typing import Annotated

from langchain_core.messages import HumanMessage
from langchain_core.messages.system import SystemMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict


class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)


@tool
def get_humid_tool() -> str:
    """Get the current humidity"""
    return "The current humidity is 69%"


@tool
def get_temperature() -> str:
    """Get the current temperature"""
    return "The current temperature is 89°C"


class Agent:
    def __init__(self):
        tools = [get_humid_tool]
        self.model = ChatOllama(model="llama3.2").bind_tools(tools)
        self.messages = [
            SystemMessage(
                "You are a cheerfull assistant that wants to help a human with its daily tasks"
            ),
        ]

    def get_response(self, message):
        self.messages.append(HumanMessage(message))
        response = self.model.invoke(self.messages)
        print(response)
        return response
