# python academy global

# le script dans l'image ci-desous permet
# de convertir auomatiquement un texte en 
# code morse et inversement avec python.

# il utilise un dictionnaire de correspondance
# et les dictionnaires par comprehension
# pour effectuer les deux conversions.

# un excellent exercice pratique pour 
# comprendre comment Python peut etre 
# utilise pour developper de petits outils de 
# communication et de cryptage.

# #python #programmation #Morse
# #pythonacademyglobal

MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", 
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", 
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", 
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", 
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---", 
    "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", 
    "8": "---..", "9": "----.", 
}

REVERSE = {code: letter for letter, code in MORSE.items()}

def to_morse(text):
    return " / ".join(" ".join(MORSE.get(c, "?") for c in word)
                      for word in text.upper().split())

def from_morse(code):
    return " ".join(" ".join(REVERSE.get(s, "?") for s in word.split())
                    for word in code.split(" / "))

message = input("text a convertir : ")
morse = to_morse(message)
print("Morse : ", morse)
print("Retour : ", from_morse(morse))