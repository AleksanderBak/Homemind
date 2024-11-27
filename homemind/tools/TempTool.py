from typing import Type

from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool
from langchain_core.runnables.config import RunnableConfig


class TempToolInput(BaseModel):
    room: str = Field(description="Room in which the temperature is to be measured")


class TempTool(BaseTool):
    name: str = "TempTool"
    description: str = """
        Useful when you want to get current temperature of a room. 
    """
    args_schema: Type[BaseModel] = TempToolInput

    def _run(
        self,
        config: RunnableConfig,
        room: str,
    ) -> str:
        """Use the tool."""
        return f"The temperature in {room} is 25 degrees"
