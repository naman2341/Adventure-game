import time


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