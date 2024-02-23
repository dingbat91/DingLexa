import logging
import autogen
from autogen import AssistantAgent, UserProxyAgent


class GPT:
    def __init__(self) -> None:
        self.CONFIG = {
            "config_list": [
                {
                    "model": "argilla_capybarahermes-2.5-mistral-7b",
                    "base_url": "http://127.0.0.1:8000/v1",
                    "api_key": "NULL",
                }
            ],
            "timeout": 120,
        }
        self.USERPROXY = UserProxyAgent(
            name="User",
            llm_config=self.CONFIG,
            human_input_mode="NEVER",
            max_consecutive_auto_reply=10,
            code_execution_config=False,
        )
        self.ASSISTANT = AssistantAgent(
            name="Assistant",
            llm_config=self.CONFIG,
            human_input_mode="NEVER",
            system_message="You are a helpful assistant, answering any questions given as best as you are able. If you are unsure of the answer say 'I don't know' and do not give guess. Reply with the answer in a style readable to a text to speech programme finishing with the word 'TERMINATE' when the task is done",
        )
        self.USERPROXY._is_termination_msg = lambda x: x.get("content", "") and x.get(
            "content", ""
        ).rstrip().endswith("TERMINATE")

    async def answer(self, question: str):
        try:
            await self.USERPROXY.a_initiate_chat(self.ASSISTANT, message=question)
            last_message = self.USERPROXY.last_message(self.ASSISTANT)
            if last_message:
                formatted_last_message: str = last_message["content"].rstrip(
                    " TERMINATE"
                )
                return formatted_last_message
            else:
                raise Exception("No final message")
        except Exception as e:
            logging.debug(f"Error: {e}")
            return "REQUESTERROR"


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    gpt = GPT()
    gpt.USERPROXY.initiate_chat(gpt.ASSISTANT, message="What is the capital of France?")
    last_message = gpt.USERPROXY.last_message(gpt.ASSISTANT)
    if last_message:
        logging.debug(f"Last message: {last_message['content'].rstrip(' TERMINATE')}")
    # result = gpt.answer("What is the capital of France?")
