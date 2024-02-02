from langchain.llms.llamacpp import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain_core.output_parsers.string import StrOutputParser
import logging


class GPT:
    MODEL: LlamaCpp
    TEMPLATE = """
    You are an assistant that can help with a variety of tasks.

    take the following question and do you best to answer it. Avoid using statements without evidence or that are not supported by the text. If you are unsure, you can say "I don't know" or "I'm not sure".

    The question is {question}
    
    Only give the direct answer to the question. Do not provide any additional information that is not directly related to the question. If the question is ambiguous, you can ask for clarification.
    """
    FORMATTED_TEMPLATE: PromptTemplate

    def __init__(self) -> None:
        logging.debug("Loading GPT Model")
        self.FORMATTED_TEMPLATE = PromptTemplate.from_template(self.TEMPLATE)
        self.MODEL = LlamaCpp(model_path="E:\Code Projects\Ding VA\llm\capybarahermes-2.5-mistral-7b.Q4_K_M.gguf", n_gpu_layers=-1, n_batch=1024, n_ctx=2048, f16_kv=True, verbose=True)  # type: ignore
        self.chain = (
            RunnablePassthrough()
            | self.FORMATTED_TEMPLATE
            | self.MODEL
            | StrOutputParser()
        )
        logging.debug("GPT Model Loaded")
        return

    def answer(self, question: str):
        result = self.chain.invoke({"question": question})
        print(f"The reply is: {result}")
        logging.debug("Answering question")
