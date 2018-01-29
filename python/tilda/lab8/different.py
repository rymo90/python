import sys
for num in sys.stdin:
    ab= num.split()
    a= int(ab[0])
    b= int(ab[1])
    print(abs(a-b))
    
