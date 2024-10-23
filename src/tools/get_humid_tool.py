from langchain.tools import tool


@tool
def get_humid_tool() -> str:
    """Get the current humidity"""
    return "The current humidity is 69%"
