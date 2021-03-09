import random
import time

char=True
var=0 #Changed to 0 for testing
BOH=3
choice=True
score=0

def move_on(pa):
    global BOH
    if pa<=0:
        BOH-=1
        if(BOH==1):
            print('You lost a badge and you currently have ',BOH,' badge')
        else:
            print('You lost a badge and you currently have ',BOH,' badges')
    else:
        if(BOH==1):
            print('Good Job! You passed the level and have',BOH,'badge')
        else:
            print('Good Job! You passed the level and have',BOH,'badges')
    if BOH<=0:
        print("Oh no! Now you have lost all of your Badge of Honours")
        print("You cannot be allowed to continue this investigation further!")
        print("Thank you for your service detective")
        exit()
    
def end_game():
    print("Oh looks like you did not want to continue further")
    print("Thank you for playing")
    exit()

def intro():
    print(format('Welcome to "Murder in New York"','^100'))
    print("This is a text based adventure game consisting of several levels and challenges as the story progresses")
    print("We hope you enjoy!")
    time.sleep(3*var)

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
    time.sleep(5*var)   
    print("However, she finds herself across a shady person holding a gun.")
    time.sleep(4.5*var)
    print("The person opens fire on Alice before she could cry for help and she is dead on the spot.")
    time.sleep(5*var)
    print("Police investigation begins the next day and the case is assigned to you.")
    time.sleep(4.25*var)
    a=1
    op=input("Are you ready to solve this case?(Y/N)\n")
    op=op.lower()
    if op!='y' and op!='yes':
        end_game()
    print("That is great! Let the journey begin!")
    op=input("Which character would you like to play as? (Elyse/Kevin)\n")
    op=op.lower()
    if op=='elyse':
        char=True
    else:
        char=False
def char_name(ch):
    if ch:
        return 'Kevin'
    else:
        return 'Elyse'

def level2():
    print('\n\n')
    print(format("LEVEL 2",'^100'))
    print('\n')
    print("You begin investigating by questioning the girl's parents")
    time.sleep(3*var)
    print("You find out she was close to Kiera and Ethan")
    time.sleep(2*var)
    a=input("Do you wish to investigate further?(Y/N)\n")
    a=a.lower()
    if a=='y' or a=='yes':
    	level2_puz()
    else:
    	end_game()

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
    print('Relation to Alice:',st1)
    in1=input("Enter the unscrambled word: ")
    if (in1!=str1) :
        print('The correct answer is: ',str1)
        pa_l2=0
    print('Personality of Ethan:',st2)
    in2=input("Enter the unscrambled word: ")
    if(in2!=str2):
        print('The correct answer is: ',str2)
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
    print('Relation to Alice: ',st1)
    in1=input("Enter the unscrambled word: ")
    if (in1!=str1) :
        print('The correct answer is: ',str1)
        pa_l2=0
    print('Personality of Kiera:',st2)
    in2=input("Enter the unscrambled word: ")
    if (in2!=str2):
        print('The correct answer is: ',str2)
        pa_l2=0
    move_on(pa_l2)

def level3() :
    
    global choice
    print('Now that you have information on the two, your team decides to split up')
    time.sleep(2*var)
    op=input('Who do you wish to approach?(Kiera/Ethan): ')
    print('\n\n')
    print(format("LEVEL 3",'^100'))
    print('\n')
    if op.lower()=='ethan':
        choice=True
        print('You get ready to investigate Ethan while',char_name(char),'parts ways to investigate Kiera')
        level3_ethan()
        level4_ethan1()
        
    else:
        choice=False
        print('You get ready to investigate Kiera while',char_name(char),'parts ways to investigate Ethan')
        level3_kiera()
        level4_kiera()

def level3_ethan():
    pa_l3=2
    print('You reach Ethans home and introduce yourself as a detective for the NYPD.')
    time.sleep(1*var)
    print('This triggers a suspicious reaction and you decide to look more into why Ethan looks so anxious')
    time.sleep(2*var)
    print('You start questioning him and notice him holding back some important information and giving vague answers.')
    time.sleep(2*var)
    print('Show Ethan that you cant be outwitted by answering these questions:\n\n')
    time.sleep(2*var)
    print('What is the capital of the USA?')
    print('a)Los Angeles','b)New York','c)Florida','d)Wahington D.C',sep='\n')
    ans=input('\nEnter the correct option (a/b/c/d): ')
    if ans!='d':
        pa_l3-=1
        print('The correct answer is d)Wahington D.C')
    else:
        print('Correct Answer!!')
    print('\nWhat is the currency used in Dubai')
    print('a)Dirham','b)US Dollar','c)Rupees','d)Won',sep='\n')
    ans=input('\nEnter the correct option (a/b/c/d): ')
    if ans!='a':
        pa_l3-=1
        print('The correct answer is a)Dirham')
    else:
        print('Correct Answer!!')
    print('\n71% of the Earth is covered by?')
    print('a)Lava','b)Water','c)Gold','d)Humans',sep='\n')
    ans=input('\nEnter the correct option (a/b/c/d): ')
    if ans!='b':
        pa_l3-=1
        print('The correct answer is b)Water')
    else:
        print('Correct Answer!!')
    print('\nIn which season do we experience the most heat?')
    print('a)summer','b)spring','c)winter','d)autumn',sep='\n')
    ans=input('\nEnter the correct option (a/b/c/d): ')
    if ans!='a':
        pa_l3-=1
        print('The correct answer is a)summer')
    else:
        print('Correct Answer!!')
    print('\nWhat is the capital of the Republic of Senegal?')
    print('a)Dakha','b)Dakar','c)Delhi','d)Dallas',sep='\n')
    ans=input('\nEnter the correct option (a/b/c/d): ')
    if ans!='b':
        pa_l3-=1
        print('The correct answer is b)Dakar')
    else:
        print('Correct Answer!!')
    time.sleep(3*var)
    print('\nIn return for the questions you answered... you got to question Ethan.')
    time.sleep(2*var)
    print('He unknowingly exposes himself as a drug dealer.')
    time.sleep(1*var)
    print('You are ready to catch the source however, he faints and is sent to the hospital, requiring immediate attention')
    time.sleep(1*var)
    move_on(pa_l3)

def examine1():
    ch2='x'
    while(ch2!='c'):
        print('You enter Ethans room and observe','a)Bathroom','b)Closet','c)Desk',sep='\n')
        ch2=input('Enter (a/b/c) to examine: ')
        if ch2=='c':
            examine2()
        else:
            print('Nothing suspicious here')

def examine2():
    ch3='x'
    print("You observe Ethan's desk and can tell that he isnt the brightest bulb in the room based on him unused academic books")
    print('But there is one book which seemed like it was often reffered to and sure enough it had what you were looking for!')
    while(ch3!='a'):
        print('You find three highlighted addresses. Which of these could be the headquarters of drug traficking bussiness?','a)Abandoned horror movie set','b)Downtown NewYork',"c)Ethan's house",sep='\n')
        ch3=input('Enter (a/b/c) to examine: ')
        if ch3=='a':
            print('An abandoned horror movie set would be perfect to stay hidden especially when it is in a poor locality!!')
            print('You copy down the address and start to it with your team')
            print("You're determined to bring this gang down")
            print()
            level4_ethan2()
        else:
            print('You didnt quite think this through did you...')
            print('Try again!')
        

def level4_ethan1():
    print('Put on your detective hat and get ready to examine the house')
    print('You enter the house and there are three rooms ahead of you.')
    ch1='x'
    while(ch1!='b'):
        print('Would you like to examine','a)The kitchen','b)Ethans room','c)Head upstairs', sep='\n')
        ch1=input('Enter (a/b/c)')
        ch1=ch1.lower()
        if ch1=='b':
            examine1()
        else:
            print('There doesnt seem to be anything interesting here')
        
def level4_ethan2():
    global char
    pa_l4=1
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
    print("The challenge is to press the ENTER key as fast as you can. The # shows the number of succesful hits")
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
        ct2=time.time()
        d=ct2-ct1
        e=ct2-ct3
        if(e>=0.2):
            z-=int(e*8)
        if(z<0):
            z=1
        if(e<0.18):
            z+=1
            if z>=wi:
                break
        print()
        print('-'*25)
        print("{:<{}}{}".format("#"*z,wi-1,"|"))
        print('-'*25,end='')
    if z>=wi:
        print("\nYou WIN! and are able to extract information about the entire system of peddlers and send your team to deal with it while you go back to your teammate to continue on the Alice case.")
        print("Congratulations!!!")
        print("Sidequest successful")
        move_on(pa_l4)
        print('You rush back to',char_name(char),'and discuss what you accomplished.')
        print(char_name(char),'and you share notes and decide to head back to the Argot mansion for further investigation')
    else:
        print("\nOh no! Looks like you were not fast enough, the bulky man flees away by tricking you ")
        print('You return back to', char_name(char),'with a heavy heart')
        move_on(0)
        print('However, ',char_name(char),'has good news and developments in the Alice case.')
        print('The two of you discuss the happenings and decide to head back to the Argot mansion')

def move(f):
    if f>0 and f<=(1/3):
        return 'rock'
         
    elif f>(1/3) and f<=(2/3):
        return 'paper'
        
    else:
        return 'scissors'
        
def shoot(move,opp_move):
    global score
    if move[0]==opp_move[0]:
        print('Kiera played',opp_move ,'. Its a draw')
    elif move[0]=='p' and opp_move=='rock':
        print('Kiera played',opp_move ,'. You won!')
        score+=1
    elif move[0]=='r' and opp_move=='scissors':
        print('Kiera played',opp_move ,'. You won!')
        score+=1
    elif move[0]=='s' and opp_move=='paper':
        print('Kiera played',opp_move ,'. You won!')
        score+=1
    else:
        print('Kiera played',opp_move ,'. You lost!')
    return score

def level3_kiera():
    
    pa_l3=1
    print('You reach Kieras house and introduce yourself as a detective from the NYPD')
    print('She seems a little bit scared and intimidated')
    print('Play play a series of rock paper scissors matches to make her feel comfortable')
    print('Bonus!! You get to move to the next level even if you lose the match, because either way your goal is to make Kiera happy')
    print('Enter rock/paper/scissors each turn. Are you ready?')
    opp1=random.random()
    m1=input('Enter your first move: ')
    score=shoot(m1,move(opp1))
    opp2=random.random()
    m2=input('Enter your second move: ')
    score=shoot(m2,move(opp2))
    opp3=random.random()
    m3=input('Enter your third move: ')
    score=shoot(m3,move(opp3))
    if score==0:
        print('You lost all three matches but Kiera had fun')
        s=r('"Alice used to lose against me all the time too!! ", she says with a soft painful giggle.')
        print(s)
    print('After the small game you notice Kiera has calmed down and she starts to talk about Alice')
    print('She is determined to help you solve the case.')
    print('You find out that there was a slight change in the behaviour of cheerful Alice the past week or so')
    print('Alice seemed worried and tensed about her father’s NGO activities and Mrs.Argots involvement in them')
    print('Kiera also reveals that Mrs. Argot was actually Alices stepmother and they were never on good terms. This seems like a very valuable clue.')
    move_on(pa_l3)

def level4_kiera():
    pa_l4=3
    print("You finish talking with and Kiera and you are alerted about the forensic reports on Alice's body")
    print("Answer these questions to infer useful data from the forensics")
    time.sleep(1)
    print("Which of the injuries could have been caused by using the baseball bat?")
    print("a)Stab wound in the abdomen","b)Entry wound on the arm",'c)Contusion and fracture of head','d)Incised wound on the thigh',sep='\n')
    ans=input('Enter the correct option (a/b/c/d): ')
    ans=ans.lower()
    if ans!='c':
        pa_l4-=1
        print('The correct answer is c)Contusion and fracture of head since the others tear the skin which isnt possible with a blunt object')
    else:
        print('Correct Answer!!')
    print("What part of the body do investigators commonly swab to get a DNA sample?")
    print('a)The cheek','b)The scalp','c)The inner ear','d)The wrist',sep='\n')
    ans=input('Enter the correct option (a/b/c/d): ')
    ans=ans.lower()
    if ans!='a':
        pa_l4-=1
        print('The correct answer is a)The cheek because buccal cells in the cheek provide a readily available, noninvasive source of DNA')
    else:
        print('Correct Answer!!')
    print('When a suspect is not available in person, what might be tested for DNA instead?')
    print('a)Their pen or pencil','b)The milk carton in the fridge','c)A household surface','d)Their toothbrush',sep='\n')
    ans=input('Enter the correct option (a/b/c/d): ')
    ans=ans.lower()
    if ans!='d':
        pa_l4-=1
        print('The correct answer is d)Their toothbrush since this couldve come in contact with buccal cells in the cheek')
    else:
        print('Correct Answer!!')
    print('A test result that is not certain enough to be useful to an investigation is called _______.')
    print('a)Unfortunate','b)Valid','c)Invalid','d)Inconclusive',sep='\n')
    ans=input('Enter the correct option (a/b/c/d): ')
    ans=ans.lower()
    if ans!='d':
        pa_l4-=1
        print('The correct answer is d)Inconclusive')
    else:
        print('Correct Answer!!')
    print('Hercule Poirot states on many occasions that in order to deduce the identity of a murderer one must use their______.')
    time.sleep(var*1)
    print('a)grey matter','b)skilllz','c)little grey cells','d)heart strings',sep='\n')
    ans=input('Enter the correct option (a/b/c/d): ')
    ans=ans.lower()
    if ans!='c':
        pa_l4-=1
        print('The correct answer is c)little grey cells from Agatha Chritie novels')
    else:
        print('Correct Answer!!')
    move_on(pa_l4)
    if(pa_l4<=0):
        print('You failed to answer correctly however your team takes over for you and you are able to acquire the results')
    print("The lab results show that the murder weapon was a stolen one and hence the killer couldn't be traced")
    print('However you also have been told that the murder happened aorund 11:30 PM to 12:00 midnight ')
    print('While you were out investigating Kiera,',char_name(char),'brings back info on Ethan with a triumphant drug case win!')
    print('The two of you share notes and head back to the Argot mansion to find out more about where the other members of the family were')
    

def level5():
    pa_l5=1
    print("You return to the Argot mansion and together with Mr and Mrs Argot decide to visit the mayor since the parents were at a party in the mayo's house")
    print("The mayor says he wont reveal facts unless he knows your potential")
    print('Prove your expert sleuth skill through this minigame')
    print("Are you ready to search nooks and corners for the best clue to solve the case?!!")
    print("Read the below paragraph")
    print('The “locked-room” mystery: This is a type of detective story in which a murder is committed under impossible conditions.')
    time.sleep(var*1)
    print('Usually in a place that the murderer couldn’t have entered or left.')
    time.sleep(var*1)
    print(' Although he isn’t given enough credit for it, Doyle was one of the earliest innovators of this classic subgenre of crime fiction.')
    time.sleep(var*1)
    print('Examples of this type include “The Speckled Band,” “The Empty House,” and The Valley of Fear.')
    time.sleep(var*1)
    ans=int(input("Enter the number of times 'the' is repeated: "))
    if(ans!=6):
        pa_l5=0
    move_on(pa_l5)
    print("The mayor trusts you and realises theres no reason to hold back important information from you")
    print('"Mrs Argot left the part at 11:00 stating she had to bring some papers" he said sinisterly')
    print('"She had returned with a change in clothes which I felt was weird" he said and he definitely sounded like he was onto something')
    print('"I decided to check what these important papers were and," he said while pulling out some papers"I think you should go through them"')
    print('Your team along with the mayor set to work')
    
#Level 6 Puzzle
def level6_puz():
    pa_l6=1
    print("But, it requires math skills! Time to test your basic math knowlege!")
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
    move_on(pa_l6)
    if pa_l6==0:
        print('You couldnt help your team with this task... hope you do better next time')
    print("Your team is able to discover that there was a 10 million error in Mr Alan Argot's bank account!!")
    print("The money seemed to have been tranfereed to a 'Capyper Island' to escape from the hands of the law")
    print("This error seemed to fit with the papers the mayor had slipped out of Mrs Argot's hands but it is too soon to conclude")
    print("This placed major suspicion on Mrs.Janice Argot and you set out to arrest her")

#Level 6
def level6():
    print('\n\n')
    print(format("LEVEL 6",'^100'))
    print('\n')
    print('There seems to be a surprising discovery around the corener!!!')
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
    print("You need to reach befor Janice to arrest her. She has a headstart!!")
    print("Time to speed up based on if you are fast enough")
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
    move_on(pa_l7)
    if pa_l7:
        print("You couldnt be of help to your team")
    print('You are able to reach before time and catch up to Mrs.Argot!!')
    print("Janice confesses about the murder and explained that she was motivated by jealousy and had married Mr Alan only for his wealth.")
    print("Meanwhile, the money transfers are tracked and another crime of Janice comes to surface.")
    print("Turns out the mayor's hunch was right as the one on the receiving end of the 10 million was none other than Janice’s ex-husband.")

#Level 7
def level7():
    print('\n\n')
    print(format("LEVEL 7",'^100'))
    print('\n')
    print("You try to locate MrsArgot")
    print("However, she has fled to the airport ready to catch a flight and escape!")
    level7_puz()

#Main function calling other functions
def main_game():
    intro()
    level1()
    level2()
    level3()
    level5()
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
