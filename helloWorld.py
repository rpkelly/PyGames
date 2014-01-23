command = 'p'
while(1):
	if(command == 'p'):
		print('Hello, World!\n')
		command = input('Enter Command(h for help):')
	elif(command == 'h'):
		print('p prints statement, q quits, and h is help')
		command = input('Enter Command(h for help):')
	elif(command == 'q'):
		break
	else:
		command = input('Unrecognized command, please enter another(h for help):')
