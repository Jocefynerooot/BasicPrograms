import pyttsx3 

v_engine = pyttsx3.init('sapi5')

voice_list = v_engine.getProperty('voices')

# print(voice_list[0].id) // for debug

v_engine.setProperty('voice', voice_list[0].id)

v_engine.say("Hello World")

v_engine.runAndWait() # without this line code not work properly
