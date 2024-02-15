# Trouver les mots : plus court et plus long de la phrase

phrase = "Un chasseur sachant chasser sait chasser sans son chien"

def mots_min_max(phrase) :
    temp = phrase.split(" ")
    temp.sort()
    mot_min, mot_max = min((temp), key=len), max((temp), key=len)
    return mot_min, mot_max

min, max = mots_min_max(phrase)

print(phrase)
print(f"Mot le plus court : '{min}' et le plus long : '{max}'")

