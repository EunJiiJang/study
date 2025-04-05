import sys
a= int(sys.stdin.readline())
b= sys.stdin.readline()

a1 =a*int(b[2])
a2 =a*int(b[1])
a3 =a*int(b[0])
a4 =a*int(b)

print (a1, a2, a3, a4, sep='\n')

