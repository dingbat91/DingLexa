from modules.audio import audioInputManager
from modules.gpt import GPT
import logging
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    FMT = "[%(levelname)s] %(asctime)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=FMT)
    am = audioInputManager()
    am.calibrate()
    prompt = am.listen()
    gpt = GPT()
    gpt.answer(prompt)
