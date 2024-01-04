import pyttsx3

engine = pyttsx3.init("sapi5")  # specify the driver name
voices = engine.getProperty("voices")
for voice in voices:
    print(voice.name, voice.id)  # print the name and ID of each voice
engine.setProperty(
    "voice",
    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0",
)  # select a natural male voice by ID
engine.setProperty("rate", 0.5)  # set the speech rate to 80%
engine.setProperty("volume", 1)  # set the speech volume to 90%
engine.say("Hello, this is a natural male voice using the sapi5 driver on Windows.")
engine.runAndWait()
