import sys

i = int(sys.argv[1])

if (i>0 and i<50):
    print "Minor"
elif (i>=50 and i<1000):
    print "Major"
else:
    print "Severe"
