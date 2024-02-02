import time, ast
import speech_recognition as sr

"""
Class for audio input and speech recognition using the Vosk API and SpeechRecognition library
"""


class audioInputManager:
    r: sr.Recognizer
    m: sr.Microphone

    """
    contructor
    """

    def __init__(self):
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

    """
    calibrates the microphone for ambient noise
    """

    def calibrate(self):
        with self.m as source:
            print("A moment of silence, please...")
            self.r.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(self.r.energy_threshold))

    """
    listens to the microphone and returns the recognized text
    """

    def listen(self):
        with self.m as source:
            print("Recognizing...")
            audio = self.r.listen(source)
            try:
                data = self.r.recognize_vosk(audio)
                input: dict = ast.literal_eval(data)
                print(input["text"])
                return input["text"]
            except sr.UnknownValueError:
                print("Could not understand audio")
                return "INPUTERROR"
            except sr.RequestError as e:
                print("Error; {0}".format(e))
                return "REQUESTERROR"


if __name__ == "__main__":
    am = audioInputManager()
    am.calibrate()
    am.listen()
