import time
import speech_recognition as sr


class audioManager:
    r: sr.Recognizer
    m: sr.Microphone

    def __init__(self):
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

    def listen(self):
        with self.m as source:
            print("A moment of silence, please...")
            self.r.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(self.r.energy_threshold))
            print("Recognizing...")
            audio = self.r.listen(source)
            try:
                print("Vosk thinks you said " + self.r.recognize_vosk(audio))
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Error; {0}".format(e))


if __name__ == "__main__":
    am = audioManager()
    am.listen()
