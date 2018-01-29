from linkedQFile import LinkedQ
class Molekylnfel(Exception):
    pass
def readMolekyl(q):
    readAtom(q)
    if q.peek()==".":
        q.dequeue()
    else:
        readNum(q)
def readAtom(q):
    readLetterUpper(q)
    if q.peek().islower():
        readLetterLower(q)
def readLetterUpper(q):
    letter = q.dequeue()
    if letter.isupper():
        return
    else:
        raise Molekylnfel("Saknar stor bokstav")
def readLetterLower(q):
    letter = q.dequeue()
    return
def readNum(q):
    num = q.dequeue()
    if q.peek().isdigit():
        q.dequeue()
        q.dequeue()
        return
    else:
        if int(num) >= 2:
            q.dequeue()
            return
        else:
            raise Molekylnfel("För litet tal vid radslutet")
def storMolekylen(molekyl):
    q= LinkedQ()
    molekyl = list(molekyl)
    for i in molekyl:
        q.enqueue(i)
    q.enqueue(".")
    return q
def kollaMolekylen(molekyl):
    q = storMolekylen(molekyl)
    try:
        readMolekyl(q)
        return "Formeln är syntaktiskt korrekt"
    except Exception as fel:
        return str(fel) 
def printQueue(q):
    while not q.isEmpty():
        molekyl = q.dequeue()
        print(molekyl,end=" ")
    print()
def main():
    q= LinkedQ()
    molekyl = input("skriv din molekyl: ")
    resultat = kollaMolekylen(molekyl)
    print(resultat)
if __name__=="__main__":
    main()
