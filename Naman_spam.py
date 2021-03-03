import time

def level4_ethan_spuz():
	pa_l4_e_spuz=1
	print("Find Ethan’s diary and examine it to get the address of the drug lord and go to the mentioned.")
	print("You go with your own team to arrest them in the process however you go in alone since there doesn’t seem to be anyone at the address.")
	print("You come across many illegal intoxicants and record them during the investigation.")
	print("Unexpectedly a bulky man with strong facial features walks in and challenges you")
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
		if(e>=1):
			z=0
		if(e<0.2):
			z+=1
			if z>=wi:
				break
		#print("*"*z,end='')
		'''
		for i in range(z):
			print("*{:026x}".format(),end='')
		print("|||")
		'''
		print("*"*z,format("|||",">30"),end='')
		#print()
	if z>=wi:
		print("You win")
	else:
		print("Time up")

def level4_ethan():
	print('\n\n')
	print(format("LEVEL 4 ETHAN",'^100'))
	print('\n')
	level4_ethan_spuz()

level4_ethan()
