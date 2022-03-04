import random
x = -1;
flag = False;
while(not flag):
	try:
		key = int(input('Press 1 to roll the die:'));
	except:
		continue
	if(key==1):
		dice = random.randint(1,6);
		if(dice == 1):
			x = 0;
			flag = True;
		else:
			print(f"oops!! dice rolled at {dice} , you need to the dice to roll at 1 for the game to start")
		
	else:
		print('enter valid input')
print("Yess!! the dice rolled to one , you can start the game")
while(flag):
	try:
		key = int(input("Press 1 to roll the die:"))
	except:
		continue;
	flagkey = False;
	if(key == 1):
		flagkey = True;
	if(flagkey):
		dice = random.randint(1,6);
		print('dice rolled to ',dice)
	x = x + dice;
	if(x>100):
		x = x - dice;
	if(x==98):
		print(f"oops!! there was a snake at 98th square!");
		x = 79;
	if(x==69):
		print(f"oops!! there was a snake at 98th square! user moved to 56th square");
		x = 56;
	if(x==12):
		print("You hopped into a ladder!!!")
		x = 24 
	if(x==32):
		print("You hopped into a ladder!!!")
		x = 98 		
	
	print('User position at ',x)
	if(x==100):
		flag = False  
	
print(" hooray!!! game complete");





