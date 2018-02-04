def tryit(x):
    temp= 0
    if x > 4:
        temp+= x
        print(temp)
        x-=1
        tryit(x)
tryit(16)
