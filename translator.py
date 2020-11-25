from gtts import gTTS
import os
language = 'en'

text = "Global warming is the long-term rise in the average temperature of the Earth’s climate system"
speech = gTTS(text=text, lang=language, slow=False)
speech.save("text.mp3")
os.system("start text.mp3")