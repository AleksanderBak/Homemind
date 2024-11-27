from homemind.graph import Graph


class Agent:
    def __init__(self):
        self.graph = Graph().get_graph()

    async def get_response(self, msg: str):
        async for event in self.graph.astream_events(
            {"messages": [("user", msg)]}, version="v2"
        ):
            match event["event"]:
                case "on_chat_model_stream":
                    content = event["data"]["chunk"].content
                    yield content
                case _:
                    pass
