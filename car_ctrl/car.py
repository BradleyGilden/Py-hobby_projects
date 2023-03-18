# create help page for:
# start - start the car
# stop -  stop car
# quit - exit

# invalid entry = "i dont understand that"
help = '''start - start the car
stop - stop the car
quit - exit the program'''
print("Car activated")
option = ""

while option != "quit":
	option = input("> ")
	if option == "help":
		print(help)
	elif option == "start":
		print("start the car")
	elif option == "stop":
		print("stop the car")
	else:
		if option != "quit":
			print("I don't understand that")
