from langchain_core.tools import ToolException

from homemind.tools.DataTool import DataTool
from homemind.tools.TempTool import TempTool


def _handle_tool_error(error: ToolException) -> str:
    return f"Error occured_while running the tool: {error}"


class ToolController:
    tool_list = {
        "TempTool": TempTool(handle_tool_error=_handle_tool_error),
        "DataTool": DataTool(handle_tool_error=_handle_tool_error),
    }

    @staticmethod
    def get_tools():
        return [tool for tool in ToolController.tool_list.values()]
