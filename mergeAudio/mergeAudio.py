# pip install gTTS
# pip install pydub
from gtts import gTTS
from pydub import AudioSegment

# funrtion to convert text to audio file
def textToAudioFile(text, filename):
    myText = str(text)
    language = 'hi'
    v_obj = gTTS(text=myText, lang=language, slow=False)
    v_obj.save(filename)

# function to merge more than 1 audio file to one
def mergeAudioFile(audio_list):
    merged = AudioSegment.empty()
    for audio in audio_list:
        merged += AudioSegment.from_mp3(audio)
    return merged

if __name__ == "__main__":
    textToAudioFile("Kaise ho aap log", "myaudio1.mp3")
    textToAudioFile("like share comment", "myaudio2.mp3")
    textToAudioFile("like share comment", "myaudio3.mp3")
    textToAudioFile("like share comment", "myaudio4.mp3")

    lst = ["myaudio1.mp3","myaudio2.mp3","myaudio3.mp3","myaudio4.mp3"]
    merge_audios = mergeAudioFile(lst)
    merge_audios.export("allMergeAudios.mp3", format="mp3")

