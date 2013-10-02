import sys

sequence = str(sys.argv[1])

count_a = sequence.count("A")
count_t = sequence.count("T")
count_g = sequence.count("G")
count_c = sequence.count("C")
total =float( count_a+count_g+count_c+count_t)

dic_seq = {'A':count_a,'T':count_t,'G':count_g,'C':count_c}
print dic_seq

print "proportion of GC: "+str((count_g+count_c)/total)
