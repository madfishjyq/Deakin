import sys

sentence = str(sys.argv[1])

sentence=sentence.upper()
set_sentence=set(sentence)
print len(set_sentence)
print set_sentence
