# from typing import Annotated
import ollama

from src.tools.get_humid_tool import get_humid_tool
from src.tools.get_temp_tool import get_temp_tool


class Agent:
    def __init__(self):
        self.tools = [get_humid_tool, get_temp_tool]

    def get_response(self, message: str):
        return ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": f"{message}",
                },
            ],
            tools=self.tools,
        )


# from langchain_ollama.llms import OllamaLLM
# from langgraph.graph import START, StateGraph
# from langgraph.graph.message import add_messages
# from langgraph.prebuilt import ToolNode, tools_condition
# from typing_extensions import TypedDict


# class State(TypedDict):
#     messages: Annotated[list, add_messages]


# graph_builder = StateGraph(State)

# tools = [get_humid_tool, get_temp_tool]
# llm = OllamaLLM(model="llama3.2", temperature=0.0)
# llm_with_tools = llml


# def chatbot(state: State):
#     return {"message": [llm_with_tools.invoke(state["messages"])]}


# graph_builder.add_node("chatbot", chatbot)

# tool_node = ToolNode(tools=tools)

# graph_builder.add_node("tools", tool_node)

# graph_builder.add_conditional_edges("chatbot", tools_condition)

# graph_builder.add_edge("tools", "chatbot")
# graph_builder.add_edge(START, "chatbot")

# compiled_graph = graph_builder.compile()


# def get_response(message: str):
#     return compiled_graph.invoke({"messages": [{"role": "user", "content": message}]})
