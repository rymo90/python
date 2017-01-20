#  Mood computer 
# demonstrates the elif clause

import random 

print(" I sense your energy. Your true emotions are coming across my screen.")
print("you are..")

mood = random.randint(1,3) 
if mood == 1:
	# happy
	print(\
	""" 
	   

	   -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | .     . |
       |  `...`  |
       ----------- """)


elif mood == 2:
   # neutral 
   print(\
   	""" 
   	    -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | ------  |
       |         |
       ----------- """)
elif mood == 3:
    # sad 
   print(\
   	""" 
   	   -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       |  .'.    |
       | '   '   |
       ----------- """) 

else:
     print("illegal mood value! (you must be in a really bad mood).")


print("...today.") 
input("\nPress the enter key to exit.") 
