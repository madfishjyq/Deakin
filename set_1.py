import sys

sentence_1 = str(sys.argv[1])
sentence_2 = str(sys.argv[2])

sentence_1=sentence_1.upper()
sentence_2=sentence_2.upper()
set_1 = set(sentence_1)
set_2 = set(sentence_2)
set_inter=set_1.intersection(set_2)
set_diff=set_1.difference(set_2)
print len(set_inter)
print len(set_diff)
