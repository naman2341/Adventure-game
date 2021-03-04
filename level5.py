import time

life=1
def check_life(a):
    if a<=0:
        #exit game
        print('You lose')

def level5_():
    print ("Now you go again to investigate mother and father of the victim.They told that they were at a party, two blocks away from the place of murder.")
    time.sleep(2)
    print("They told you that the Mayor of the city was also there at the party.")
    time.sleep(1)
    print("While investigating, you find Mrs Janice Argot acting suspicious.")
    time.sleep(1)
    print("A good detective must be able to follow instructions without missing any important lead in the case.")
    time.sleep(1)
    print("To get an important clue for solving the case, we need to check your general knowledge and how fast you are.You will only get 5 seconds to answer the questions.")
    print("Are you ready?\n Press Y for Yes,N for No")
    ans=input()
    if (ans=='Y'):
        score=0
        print("What is the capital of Assam?\n A.Dibrugarh\n B.Dispur\n C.Imphal\n D.Itanagar")
        ans1=input()
        start = time.time()     #the variable that holds the starting time
        elapsed = 0             #the variable that holds the number of seconds elapsed.
        while elapsed < 5:      #while less than 5 seconds have elapsed  
            if (ans1=='B' or 'b'):
              score+=1
        elapsed = time.time() - start      
        print("Where is the headquarters of The Reserve Bank of India located?\n A.Bengaluru \n B.Mumbai \n C.Lucknow \n D.New Delhi")    
        ans2=input()
        start=time.time()
        elapsed=0
        while elapsed < 5:
            if (ans2=='B' or ans2=='b'):
                score+=1
        elapsed = time.time() - start
        print("Where is the headquarters of national crime records bureau located?\n A.New Delhi \n B.Chennai \n C.Indore \n D.Kochi")
        ans3=input()
        start=time.time()
        elapsed=0
        while elapsed < 5:
            if (ans2=='A' or ans2=='a'):
                 score+=1
        if (score<=2):
            print("Congratulations you have passed the test.")
        else:
            print("Sorry. You did not pass the test")
        if (score<=2):
            print("Read the following text.\n “Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore \n et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut \n aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse \n cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa \n qui officia deserunt mollit anim id est laborum.")
            time.sleep(2)
            print("Every alternate letter of the Fifth word of the fifth line from the bottom in the above text is your password.")
            time.sleep(2)
            print("Please enter the password")
            pas=input()
            if (ans=='ae'):
                print(" You discuss with the Mayor and find out that Mrs Janice had left the party at around 11:00 and come back again at 12:00 to get some papers signed. You note it down.")
            else:
                print("Wrong Password")
    else:
        print("Wrong input")
level5_()
