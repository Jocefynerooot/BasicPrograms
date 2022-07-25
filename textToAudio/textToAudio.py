# pip install gTTS
from gtts import gTTS

def textToAudioFile(text, filename):
    myText = str(text)
    language = 'hi'
    v_obj = gTTS(text=myText, lang=language, slow=False)
    v_obj.save(filename)

if __name__ == "__main__":
    textToAudioFile("Kaise ho aap log", "myaudio")