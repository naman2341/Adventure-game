import random
import time

char=True
var=0 #Changed to 0 for testing
BOH=3
game_start_time=time.time()

def move_on():
	pass

def game_over(): #Still WIP
	global BOH
	print("You lost a badge of honour")
	BOH-=1
	if BOH<=0:
		print("Oh no! Now you have lost all of your Badge of Honours")
		print("You cannot be allowed to continue this investigation further!")
		exit()

def end_game():
	print("Oh looks like you did not want to continue further")
	print("Thank you for playing")
	exit()

def intro():
	print(format('Welcome to "Murder in New York"','^100'))
	print("This is a text based adventure game consisting of several levels and challenges as the story progresses")
	print("We hope you enjoy!")
	time.sleep(5*var)

#Level 1
def level1():
	global char
	print('\n\n')
	print(format("LEVEL 1",'^100'))
	print('\n')
	print("Alice is reading a book.")
	time.sleep(0.7*var)
	print("The weather outside is dark and gloomy.")
	time.sleep(1.5*var)
	print("It's raining heavily and she is alone at home.")
	time.sleep(1.5*var)
	print("She hears a thud on the door and gets out of bed to check if it was a stray cat in need of shelter from the harsh rain.")
	time.sleep(4*var)
	print("However, she finds herself across a shady person holding a gun.")
	time.sleep(2*var)
	print("The person opens fire on Alice before she could cry for help and she is dead on the spot.")
	time.sleep(3*var)
	print("Police investigation begins the next day and the case is assigned to you (Elyse/Kevin).")
	time.sleep(3*var)
	print("The player is filled in with the details and the gameplay begins.")
	time.sleep(2.5*var)
	a=1
	op=input("Are you ready to solve this case?\n")
	op=op.lower()
	if op!='y' and op!='yes':
		end_game()
	print("That is great let the journey begin!")
	op=input("Character? (Elyse/Kevin)\n")
	op=op.lower()
	if op=='elyse':
		char=True
	else:
		char=False

#Level 2 Puzzle
def level2_puz():
	pa_l2=1
	print("That is great! Lets start with Ethan")
	#boyfriend,suspicious-Ethan
	#bestfriend,friendly-Kiera
	#Words might have to be changed probabily
	print("Looks like Alice loved writing about her friends in her diary , but looks like its scrambelled!")
	print("Start by unscrambling these clues related to Ethan")
	while 1:
		str1="boyfriend"
		str2="suspicious"
		l1=list(str1)
		l2=list(str2)
		random.shuffle(l1)
		random.shuffle(l2)
		st1="".join(l1)
		st2="".join(l2)
		if st1[0]!=str1[0] and st2[0]!=str2[0]:
			break
	print(st1)
	in1=input("The unscrambled word is:")
	if in1=='ch':
		return
	print(st2)
	in2=input("The unscrambled word is:")
	if (in1!=str1 or in2!=str2) :
		pa_l2=0

	print("Now time to unscramble the clues related to Kiera")
	while 1:
		str1="bestfriend"
		str2="friendly"
		l1=list(str1)
		l2=list(str2)
		random.shuffle(l1)
		random.shuffle(l2)
		st1="".join(l1)
		st2="".join(l2)
		if st1[0]!=str1[0] and st2[0]!=str2[0]:
			break
	print(st1)
	in1=input("The unscrambled word is:")
	print(st2)
	in2=input("The unscrambled word is:")
	if (in1!=str1 or in2!=str2) :
		pa_l2=0
	if pa_l2==0:
		print("Oops, looks like your answer was wrong!")
		game_over()
	else:
		print("Looks like you have passed this puzzle")
		move_on()

#Level 2
def level2():
	print('\n\n')
	print(format("LEVEL 2",'^100'))
	print('\n')
	print("The victim’s family is enquired about Alice’s recent behaviour.")
	time.sleep(4.5*var)
	print("The father comments about her boyfriend Ethan and best friend Kiera.")
	time.sleep(5*var)
	a=input("Do you wish to investigate Ethan or Kiera?\n")
	a=a.lower()
	if a=='y' or a=='yes':
		level2_puz()
	else:
		end_game()

#Level 4 Side Puzzle Ethan
def level4_ethan_spuz():
	pa_l4_e_spuz=1
	print("Find Ethan’s diary and examine it to get the address of the drug lord and go to the mentioned.")
	time.sleep(3*var)
	print("You go with your own team to arrest them in the process however you go in alone since there doesn’t seem to be anyone at the address.")
	time.sleep(5*var)
	print("You come across many illegal intoxicants and record them during the investigation.")
	time.sleep(2.5*var)
	print("Unexpectedly a bulky man with strong facial features walks in and challenges you")
	time.sleep(2.5*var)
	print("The bulky man thinks that you cannot beat him in a duel")
	time.sleep(2*var)
	print("But little does he know that you are a trained martial-artist")
	time.sleep(2*var)
	print("The challenge is to press the ENTER key as fast as you can")
	time.sleep(3*var)
	print("READY?")
	time.sleep(1*var)
	print("3")
	time.sleep(1*var)
	print("2")
	time.sleep(1*var)
	print("1")
	time.sleep(1*var)
	print("GO!!!")
	time.sleep(1*var)
	t=time.localtime()
	ct1=time.time()
	ct2=ct1
	d=ct2-ct1
	wi=25
	z=0
	while d<=10.3:
		ct3=time.time()
		a=input()
		if(a=='ch'):
			z=wi
			break
		ct2=time.time()
		d=ct2-ct1
		e=ct2-ct3
		if(e>=0.3):
			z-=int(e*10)
			#print(e)
		if(e<0.2):
			#print(e)
			z+=1
			if z>=wi:
				break
		print()
		print('-'*25)
		print("{:<{}}{}".format("#"*z,wi-1,"|"))
		#print('\r')
		print('-'*25,end='')
		#print("*"*z,format("",">30"),end='')
		#print()
	if z>=wi:
		print("\nYou WIN! and are able to extract information about the entire system of peddlers and send your team to deal with it while you go back to your teammate to continue on the Alice case.")
		print("Congratulations!!!")
		print("Sidequest successful")
		time.sleep(4)
		move_on()
	else:
		print("\nOh no! Looks like you were not fast enough, the bulky man flees away by tricking you ")
		time.sleep(4)
		move_on()

#Level 4
def level4_ethan():
	print('\n\n')
	print(format("LEVEL 4 ETHAN",'^100'))
	print('\n')
	level4_ethan_spuz()

#Level 6 Puzzle
def level6_puz():
	pa_l6=1
	print("Looks like you have forgot your math! Time to test your basic math knowlege!")
	for i in range(3):
		a = random.randint(-100, 100)
		b = random.randint(-100, 100)
		ans = a+b
		inp = int(input("What is the sum of {} and {}\n".format(a, b)))
		if inp==-999: #Cheat answer is ch
			break
		if inp!=ans: 
			print("Oops looks like your answer is wrong")
			pa_l6=0
			break
	if pa_l6==0:
		game_over()
	else:
		print("Looks like you have passed this puzzle too!")
		move_on()

#Level 6
def level6():
	print('\n\n')
	print(format("LEVEL 6",'^100'))
	print('\n')
	level6_puz()

#Timed input
def input_time():
	ct1=time.time()
	a=input()
	ct2=time.time()
	if ct2-ct1<=2.3:
		return a
	else:
		return 0

#Level 7 Puzzle
def level7_puz():
	pa_l7=1
	print("Looks like you are getting late for you flight! Time to speed!")
	time.sleep(3)
	for i in range(5):
		print("Enter the following character within 2 seconds")
		time.sleep(2)
		ch=random.choice("abcdefghijklmnopqrstuvwxyz")
		print(ch)
		a=input_time()
		if 'ch' == a: #Cheat answer is ch
			break
		if a==0:
			print("Oops looks like you were too slow!")
			pa_l7=0
			break
		elif a!=ch:
			print("Oops looks like you enter a wrong character")
			pa_l7=0
			break
	if pa_l7==0:
		game_over()
	else:
		print("Looks like you have passed this puzzle too!")
		move_on()

#Level 7
def level7():
	print('\n\n')
	print(format("LEVEL 7",'^100'))
	print('\n')
	level7_puz()

#Main function calling other functions
def main_game():
	intro()
	level1()
	level2()
	level4_ethan()
	level6()
	level7()
	game_end_time=time.time()
	t=game_end_time-game_start_time
	t=int(t)
	h=t//3600
	m=(t%3600)//60
	s=t%60
	print("Congratulations! You beat the game in {} hours {} minutes and {} seconds!".format(h,m,s))

main_game()
#Tab changed
