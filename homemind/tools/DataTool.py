from typing import Type

import pandas as pd
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool
from langchain_core.runnables.config import RunnableConfig


class DataToolInput(BaseModel):
    number_of_days: int = Field(
        description="Number of days for which availability is to be checked"
    )
    # return_direct: bool = Field(
    #     description="Whether to return the data directly to the user without you seeing what it is",
    #     default=True,
    # )


class DataTool(BaseTool):
    name: str = "DataTool"
    description: str = """
        Useful when you want to get report of the data for given number of days"
    """
    args_schema: Type[BaseModel] = DataToolInput

    def _run(
        self,
        config: RunnableConfig,
        number_of_days: str,
        return_direct: bool = True,
    ) -> str:
        """Use the tool."""
        df = pd.DataFrame({"Temperature": [1, 2, 3], "Humidity": [4, 5, 6]})
        return df
