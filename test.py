import sys

a=str(sys.argv[1])
b=str(sys.argv[2])
c=str(sys.argv[3])
d=str(sys.argv[4])

d='and '+d
result = ','.join([a,b,c,d])
result+='.'
print result
