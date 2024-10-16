from langchain_ollama.llms import OllamaLLM


class HomeAgent:
    def get_response(self, prompt):
        llm = OllamaLLM(model="llama3.2")

        for chunk in llm.stream(prompt):
            yield chunk
