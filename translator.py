from gtts import gTTS
import sys, getopt, os


def translatorTTS(file):
    language = 'fr'
    fichier = open(file, "r")
    contenu = fichier.read()
    print(contenu)
    speech = gTTS(text=contenu, lang=language, slow=False)
    speech.save("{}.mp3".format(file))
    print("Fichier audio enregisté avec succès")
    fichier.close()


def main(argv):
    inputfile = ''
    outputtype = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "otype="])
    except getopt.GetoptError:
        print('translator.py -i <inputfile> -o <outputtype>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('translator.py -i <inputfile> -o <outputtype>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--otype"):
            outputtype = arg
    if outputtype == "v":
        translatorTTS(inputfile)
    else:
        print(
            "Aucun type de sortie choisi ou mauvais format choisi. Les choix sont v ou t. ex: '-o v'"
        )


if __name__ == "__main__":
    main(sys.argv[1:])
