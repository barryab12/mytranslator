from gtts import gTTS
import os
import sys
language = 'fr'


def translator(file):
    fichier = open(file, "r")
    contenu = fichier.read()
    print(contenu)
    speech = gTTS(text=contenu, lang=language, slow=False)
    speech.save("{}.mp3".format(file))
    print("Fichier audio enregisté avec succès")
    fichier.close()


if __name__ == "__main__":
    file = str(sys.argv[1])
    output = str(sys.argv[2])
    if not file or not output:
        print('Ajouter les parametres')
    if output == "v":
        translator(file)
    else:
        print("Ajouter le second paramètre")
