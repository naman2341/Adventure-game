import time

life=3
def check_life(a):
    if a<=0:
        #exit game
        print('You lose')
def ethan_level3_puz():
    pa_l3=2
    print('You reach Ethans home and introduce yourself as a detective for the NYPD. This triggers a suspicious reaction and you decide to look more into why Ethan looks so anxious')
    print('You start questioning him and notice him holding back some inportant information or manipulating your questions')
    print('Show Ethan that you cant be outwitted by answering these questions:')
    time.sleep(1)
    print('What is the capital of the USA?')
    print('a)Los Angeles','b)New York','c)Florida','d)Wahington D.C',sep='\n')
    ans=input()
    if ans!='d':
        pa_l3-=1
    print('What is the currency used in Dubai')
    print('a)Dirham','b)US Dollar','c)Rupees','d)Won',sep='\n')
    ans=input()
    if ans!='a':
        pa_l3-=1
    print('71% of the Earth is covered by?')
    print('a)Lava','b)Water','c)Gold','d)Humans',sep='\n')
    ans=input()
    if ans!='b':
        pa_l3-=1
    print('In which season do we experience the most heat?')
    print('a)summer','b)spring','c)winter','d)autumn',sep='\n')
    ans=input()
    if ans!='a':
        pa_l3-=1
    print('What is the capital of the Republic of Senegal?')
    print('a)Dakha','b)Dakar','c)Delhi','d)Dallas',sep='\n')
    ans=input()
    if ans!='b':
        pa_l3-=1
    return pa_l3
res=keira_level4_puz()
if res>0:
    print("Next level")
else:
    print("YOu lost a life")
    life-=1
check_life(life)

def keira_level4_puz():
    pa_l4=3
    print("Answer these questions if you can infer useful data from the forensics")
    time.sleep(1)
    print("Which of the injuries could have been caused by using the baseball bat?")
    print("a)Stab wound in the abdomen","b)Entry wound on the arm",'c)Contusion and fracture of head','d)Incised wound on the thigh',sep='\n')
    ans=input()
    if ans!='c':
        pa_l4-=1
    print("What part of the body do investigators commonly swab to get a DNA sample?")
    print('a)The cheek','b)The scalp','c)The inner ear','d)The wrist',sep='\n')
    ans=input()
    if ans!='a':
        pa_l4-=1
    print('When a suspect is not available in person, what might be tested for DNA instead?')
    print('a)Their pen or pencil','b)The milk carton in the fridge','c)A household surface','d)Their toothbrush',sep='\n')
    ans=input()
    if ans!='d':
        pa_l4-=1
    print('A test result that is not certain enough to be useful to an investigation is called _______.')
    print('a)Unfortunate','b)Valid','c)Invalid','d)Inconclusive',sep='\n')
    ans=input()
    if ans!='d':
        pa_l4-=1
    print('Hercule Poirot states on many occasions that in order to deduce the identity of a murderer one must use their______.')
    print('a)grey matter','b)skilllz','c)little grey cells','d)heart strings',sep='\n')
    ans=input()
    if ans!='c':
        pa_l4-=1
    return pa_l4

res=keira_level4_puz()
if res>0:
    print("Next level")
else:
    print("YOu lost a life")
    life-=1
    
check_life(life)

#level 5
def level5_puz():
    pa_l5=1
    print("Are you ready to search nooks and corners for the best clue to solve the case?!!")
    s= r"Type the word that comes before 'murder'"
    print(s)
    print('The “locked-room” mystery: This is a type of detective story in which a murder is committed under impossible conditions, usually in a place that the murderer couldn’t have entered or left. Although he isn’t given enough credit for it, Doyle was one of the earliest innovators of this classic subgenre of crime fiction. Examples of this type include “The Speckled Band,” “The Empty House,” and The Valley of Fear. ')
    time.sleep(1)
    ans=input()
    if(ans!='a'):
        pa_l5=0
    return pa_l5
    
res=level5_puz()
if res>0:
    print("Next level")
else:
    print("YOu lost a life")
    life-=1
    
check_life(life)
    
    
    
    
    
