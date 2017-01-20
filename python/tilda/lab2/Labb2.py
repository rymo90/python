
def korttrick():
   from arrayQFile import ArrayQ   # importerat array filen

   q =ArrayQ()
   givnakort = input ("Skriv in kortens ordning och särkilj talen med ,").split(",")    # inmatingen

   # för rätt ordning ange 7,1,12,2,8,3,11,4,9,5,13,6,10

   magi = []
   for rad in givnakort:       # lägger till i min lista via enqueue metoden
      q.enqueue(int(rad))

   e = q.isEmpty()

   while e == False:   # medans det är tom
      x = q.dequeue()   # tar ut första värden i listan
      q.enqueue(x)   # den lägger värdet i listan
      y = q.dequeue()
      magi.append(y)  # retunear och lägger det i nya listan
      e=q.isEmpty()  # slutar om emty listan är tom



   print (magi)  # printar ut värden

korttrick()


##x = [1, 2, 3, 4, 5] # skapar arry eller lista.
##print (x)
##
##x.insert(4, 100) # lägger till 100 på den fjärde platsen i listan.
##print (x)
##
##
##x.remove(100)  # skriv talet du vill ta bort från listan (arrayen) inte dennes plats
##print (x)
##
##x.append(100) # Lägger till talet längst bak i listan.
##print (x)
##
##y = x.pop() # Plockar ut ut de sista talet från listan och retunerar det
##print (y)
##print (x)
##
##z = x.pop(0) # plockar och retunerar talet på den valda platsen i listan.
##print (z)
##print (x)
