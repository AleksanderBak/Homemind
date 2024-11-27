import json
import os
from typing import Annotated

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from typing_extensions import TypedDict

from homemind.tools.ToolController import ToolController

load_dotenv()
API_KEY = os.getenv("OPENAI_KEY")


class State(TypedDict):
    messages: Annotated[list, add_messages]


class Graph:
    def __init__(self):
        self.graph_builder = StateGraph(State)
        self.tools = ToolController.get_tools()
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=API_KEY,
            temperature=0.0,
        ).bind_tools(self.tools)

    def get_graph(self):
        def chatbot(state: State):
            return {"messages": [self.llm.invoke(state["messages"])]}

        def final_answer(state: State):
            tool = state["messages"][-1].tool_calls[0]
            print(tool)
            return {"messages": "Test"}

        def check_tool_call(state: State):
            messages = state["messages"]
            last_message = messages[-1]

            if last_message.tool_calls:
                arguments = json.loads(
                    last_message.additional_kwargs["tool_calls"][0]["function"][
                        "arguments"
                    ]
                )
                # print(f"Final arguments {arguments}")
                # # if arguments["return_direct"]:
                # #     return "final_answer"
                return "final_answer"
            else:
                return END

        self.graph_builder.add_node("chatbot", chatbot)
        self.graph_builder.add_node("tool_node", ToolNode(self.tools))
        self.graph_builder.add_node("final_answer", final_answer)

        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", check_tool_call)
        self.graph_builder.add_edge("tool_node", "chatbot")
        self.graph_builder.add_edge("final_answer", END)

        graph = self.graph_builder.compile()
        # Visualize the graph
        graph.get_graph().draw_mermaid_png(output_file_path="graph_schema.png")
        return graph
