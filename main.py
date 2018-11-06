"""Case-study #4 Text analysis
Developers:
Batenev P.A.(47%), Grigorev A.E.(55%), Dolgih N.A.
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
                  + text_.count(RUS_VOWELS[8])

asl = None
asw = None
fre = None
print(SENTENCE, count_sentence)
print(WORDS, count_words)
print(SYLLABLES, count_syllables)
print(ASL, asl)
print(asw, ASW)
print(fre, FRE)
