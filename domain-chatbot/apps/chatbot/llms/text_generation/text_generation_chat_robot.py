from dotenv import load_dotenv
from langchain import LLMChain, PromptTemplate
from .text_generation_model_impl import TextGenerationModel

llm = TextGenerationModel()


class TextGeneration():

    def chat(prompt: str, role_name: str, you_name: str, query: str, history: str) -> str:
        role_prompt_str = prompt.format(
            you_name=you_name, input="{input}", history=history)
        prompt = PromptTemplate(
            input_variables=["input"], template=role_prompt_str
        )
        llm_chain = LLMChain(
            llm=llm,
            prompt=prompt,
            verbose=True
        )
        return llm_chain.predict(input=query)