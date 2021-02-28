 import random

def move_on():
	pass
def level7():
	pass
def game_over():
	pass

def level6():
	pa=1
	print("Looks like you have forgot your math! Time to test your basic math knowlege!")
	for i in range(3):
		a = random.randint(-100, 100)
		b = random.randint(-100, 100)
		ans = a+b
		inp = int(input("What is the sum of {} and {}\n".format(a, b)))
		if inp!=ans:
			print("Oops looks like your answer is wrong")
			pa=0
			break
	if pa==0:
		game_over()
	else:
		print("Looks like you have passed this puzzle too!")
		move_on()
		level7()

print("Level 6")
level6()