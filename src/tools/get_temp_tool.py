from langchain.tools import tool


@tool
def get_temp_tool() -> str:
    """Get the current temperature"""
    return "The current temperature is 78°C"
