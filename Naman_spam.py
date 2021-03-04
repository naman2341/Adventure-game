import time
var=0
def move_on():
	pass


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
		if(e>=0.2):
			z-=int(e*10)
			#print(e)
		if(e<0.18):
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
		move_on()
	else:
		print("\nOh no! Looks like you were not fast enough, the bulky man flees away by tricking you ")
		move_on()

def level4_ethan():
	print('\n\n')
	print(format("LEVEL 4 ETHAN",'^100'))
	print('\n')
	level4_ethan_spuz()

level4_ethan()
