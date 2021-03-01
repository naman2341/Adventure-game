import random
import time

global char

def move_on():
	pass
def game_over():
	pass

#Level 1
def level1():
	var=0
	print("Alice is reading a book.")
	time.sleep(0.7*var)
	print("The weather outside is dark and gloomy.")
	time.sleep(1.5*var)
	print("It’s raining heavily and she is alone at home.")
	time.sleep(1.5*var)
	print("She hears a thud on the door and gets out of bed to check if it was a stray cat in need of shelter from the harsh rain.")
	time.sleep(6*var)
	print("However, she finds herself across a shady person holding a gun.")
	time.sleep(4.5*var)
	print("The person opens fire on Alice before she could cry for help and she’s dead on the spot.")
	time.sleep(6*var)
	print("Police investigation begins the next day and the case is assigned to you (Elyse/Kevin).")
	time.sleep(5.25*var)
	print("The player is filled in with the details and the gameplay begins.")
	time.sleep(3.5*var)
	a=1
	op=input("Are you ready to solve this case?\n")
	op=op.lower()
	if op=='y' or op=='yes':
		a=0
	while a:
		print("Are you sure you arn't excited to go on this amazing adventure!!?")
		op=input("So are you ready to solve this case?\n")
		op=op.lower()
		if op=='y' or op=='yes':
			a=0
	print("That is great let the journey begin!")
	op=input("Character? (Elyse/Kevin)\n")
	op=op.lower()
	if op=='elyse':
		char=True
	else:
		char=False

level1()

#Level 6
def level6_puz():
	pa_l6=1
	print("Looks like you have forgot your math! Time to test your basic math knowlege!")
	for i in range(3):
		a = random.randint(-100, 100)
		b = random.randint(-100, 100)
		ans = 1
#Changed to 1 for testing!
		inp = int(input("What is the sum of {} and {}\n".format(a, b)))
		if inp!=ans:
			print("Oops looks like your answer is wrong")
			pa_l6=0
			break
	if pa_l6==0:
		game_over()
	else:
		print("Looks like you have passed this puzzle too!")
		move_on()

print("Level 6")
#level6_puz()

#Timed input
def input_time():
	t=time.localtime()
	ct1=int(time.strftime("%S", t))
	a=input()
	t=time.localtime()
	ct2=int(time.strftime("%S", t))
	if ct1==59:
		ct1=0
		ct2+=1
		if ct2==60:
			ct2=0
	if ct2-ct1<=2:
		return a
	else:
		return 0
#Level 7
def level7_puz():
	pa_l7=1
	print("Looks like you are getting late for you flight! Time to speed!")
	for i in range(5):
		print("Enter the following character within 2 seconds")
		time.sleep(2)
		ch=random.choice("abcdefghijklmnopqrstuvwxyz")
		print(ch)
		a=input_time()
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

print("Level 7")
#level7_puz()
