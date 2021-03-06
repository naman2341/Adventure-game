import time
var=0
def move_on():
	pass

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
    print("Are you ready?\nPress Y for Yes,N for No")
    ans=input()
    if (ans=='Y'):
        score=0
        print("What is the name of Sherlock Holmes's landlady? \nA.Mrs Hanson\nB.Mrs Henson\nC.Mrs Hodgson\nD.Mrs Hudson")
        start = time.time()             #the variable that holds the starting time        
        ans1=input()
        elapsed = time.time() - start   #the variable that holds the number of seconds elapsed.
        if(elapsed<5 and ans1.lower()=='d'):
            score+=1  
        print("Byomkesh Bakshi is an Indian-Bengali fictional detective created by Sharadindu Bandyopadhyay. Referring to himself as a Truth seeker or Satyanweshi in the stories, Bakshi is known for his proficiency with observation, logical reasoning, and forensic science which he uses to solve complicated cases, usually murders.\n Initially appearing in the 1932 story Satyanweshi, the character's popularity immensely increased in Bengal and other parts of India.")
        time.sleep(5)
        print("What is Byomkesh Bakshi popularly known as ?")
        ans2=input()
        start=time.time()
        elapsed=0
        if (ans2=='satyanweshi'):
            score+=1
            elapsed = time.time() - start
        print("Where is the headquarters of national crime records bureau located?\n A.New Delhi \n B.Chennai \n C.Indore \n D.Kochi")
        ans3=input()
        start=time.time()
        elapsed=0
        if (ans2=='A' or ans2=='a'):
            score+=1
            elapsed = time.time() - start
        if (score>=2): 
            print("Congratulations you have passed the test.")
            time.sleep(2)
        else:
            print("Sorry. You did not pass the test")
            time.sleep(2)
        if (score>=2):
            print("Read the following text.\n The One Thousand and One Nights contains several of the earliest detective stories, anticipating modern detective fiction.  The oldest known example of a detective story was The Three Apples, one of the tales narrated by Scheherazade in the One Thousand and One Nights (Arabian Nights).\n  In this story, a fisherman discovers a heavy, locked chest along the Tigris river, which he then sells to the Abbasid Caliph, Harun al-Rashid. When Harun breaks open the chest, he discovers the body of a young woman who has been cut into pieces.\n Harun then orders his vizier, Ja'far ibn Yahya, to solve the crime and to find the murderer within three days, or be executed if he fails in his assignment.\n Suspense is generated through multiple plot twists that occur as the story progressed. With these characteristics this may be considered an archetype for detective fiction. It anticipates the use of reverse chronology in modern detective fiction, where the story begins with a crime before presenting a gradual reconstruction of the past.")
            time.sleep(5)
            print("The name of the river along which the fisherman finds the chest is your password.")
            time.sleep(2)
            print("Please enter the password")
            pas=input()
            if (pas=='tigris'):
                print(" You discuss with the Mayor and find out that Mrs Janice had left the party at around 11:00 and come back again at 12:00 to get some papers signed. You note it down.")
                print("This is one of the very important clue in solving the case")
            else:
                print("Wrong Password")
    else:
        print("Wrong input")
level5_()
