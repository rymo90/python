# finicky Conter 
# demonstrates the break and continue statements

count = 0
while True: # This technically means the loop will continue forever, 
            # unless there is an exit condition in the loop body. 
	count += 1
	# end loop if count greater then 10
	if count > 10:
		break
	# skip 5
	if count == (5):
		continue
	print(count)
input("\n\nPress the enter key to exit.")
