from langchain_ollama.llms import OllamaLLM


class HomeAgent:
    def __init__(self):
        self.name = "HomeAgent"

    async def get_response(self, prompt):
        llm = OllamaLLM(model="llama3.1")

        for chunk in llm.stream(prompt):
            yield chunk
