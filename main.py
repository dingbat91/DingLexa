from modules.audio import audioInputManager
from modules.gpt import GPT
import logging
from dotenv import load_dotenv

if __name__ == "__main__":
    # Load environment variables
    load_dotenv()
    # Set up logging
    FMT = "[%(levelname)s] %(asctime)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=FMT)

    # Start Audio management and accept input
    am = audioInputManager()
    am.calibrate()
    prompt = am.listen()
    # Start GPT and answer the prompt
    if prompt == "INPUTERROR" or prompt == "REQUESTERROR":
        logging.debug(f"Voice input error: {prompt}")
        am.speak("I'm sorry, an error occured")
        exit()
    gpt = GPT()
    result = gpt.answer(prompt)
    # Output the result
    logging.debug(f"Voice output string: {result}")
    am.speak(result)
