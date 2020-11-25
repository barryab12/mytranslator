from gtts import gTTS
import os
language = 'fr'

fichier = open("text.txt", "r")
contenu = fichier.read()
print(contenu)
speech = gTTS(text=contenu, lang=language, slow=False)
speech.save("text.mp3")
print("Fichier audio enregisté avec succès")
fichier.close()