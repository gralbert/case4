"""Case-study #4 Text analysis
Developers:
Batenev P.A.(46%), Grigorev A.E.(55%), Dolgih N.A. (39%)
"""

from rulocal import *
text = input(TEXT)
count_sentence = text.count(".") + text.count("?") + text.count("!")
number = text.split()
count_words = len(number)
text_ = text.lower()
count_syllables = text_.count(RUS_VOWELS[0]) + text_.count(RUS_VOWELS[1])\
                  + text_.count(RUS_VOWELS[2]) + text_.count(RUS_VOWELS[3])\
                  + text_.count(RUS_VOWELS[4]) + text_.count(RUS_VOWELS[5])\
                  + text_.count(RUS_VOWELS[6]) + text_.count(RUS_VOWELS[7])\
                  + text_.count(RUS_VOWELS[8]) + text_.count(RUS_VOWELS[9])
asl = count_words/count_sentence
asw = count_syllables/count_words
fre = 206.835 - (1.3 * asl) - (60.1 * asw)
print(SENTENCE, count_sentence)
print(WORDS, count_words)
print(SYLLABLES, count_syllables)
print(ASL, asl)
print(ASW, asw)
print(FRE, fre)
if fre > 80:
    print(SIMPLE)
elif fre > 50:
    print(EASY)
elif fre > 25:
    print(MEDIATE)
else:
    print(HARD)
