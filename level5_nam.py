def level5():
    pa_l5=2
    print("You return to the Argot mansion and together with Mr and Mrs Argot decide to visit the mayor since the parents were at a party in the mayor's house")
    time.sleep(var*1)
    print("The mayor says he wont reveal facts unless he knows your potential")
    time.sleep(var*0.5)
    print('Prove your expert sleuth skill through this minigame')
    time.sleep(var*0.25)
    print("Are you ready to search nooks and corners for the best clue to solve the case?!!")
    time.sleep(var*1)
    print("Read the below paragraph")
    print('"The “locked-room” mystery: This is a type of detective story in which a murder is committed under impossible conditions.')
    time.sleep(var*1)
    print('Usually in a place that the murderer couldn’t have entered or left.')
    time.sleep(var*1)
    print(' Although he isn’t given enough credit for it, Doyle was one of the earliest innovators of this classic subgenre of crime fiction.')
    time.sleep(var*1)
    print('Examples of this type include “The Speckled Band,” “The Empty House,” and The Valley of Fear."')
    time.sleep(var*1)
    print('')
    ans=int(input("Enter the number of times 'the' is repeated in the above paragraph: "))
    print('')
    if(ans!=6):
        pa_l5-=1
        print("You answered wrong :(. The correct answer is 6")
    else:
        print("That was spot on!!")
    print('\n\n')
    print("Read the below paragraph")
    print("A lavish trip through Europe quickly unfolds into a race againt time to solve a murder aboard a train.")
    time.sleep(var*1)
    print("Everyone's a suspect when Detective Hercule Poirot arrives to interrogate all passengers and search for clues before the killer can strike again.")
    time.sleep(var*2)
    ans=input("Enter the word to the right of the word which consists the letters 'v' and 't': ")
    print('')
    ans=ans.lower()
    if(ans!='hercule'):
        pa_l5-=1
        print("You answered wrong :(. The correct answer is 'Hercule'")
    else:
        print("That was spot on!!")
    print('\n\n')
    print('Read the below paragraph: ')
    print("In the dead of a hot summer's night, Detective Erika Foster is called to a murder scene.")
    time.sleep(var*1)
    print("The victim, a doctor, is found suffocated in bed. His wrists are bound and his eyes bulging through a clear plastic bag")
    time.sleep(var*1)
    print("A few days later, another victim is foung dead, in exactly the same curcumstances.")
    time.sleep(var*1)
    print("As Erika and her team start digging deeper, they discover a calculated serial killer- stalking their victims before striking")
    time.sleep(var*1)
    print("As a heat wave descends upon London, Erika will do everuthing to stop the Night Stalker before the body count rises. ")
    time.sleep(var*1)
    print("But the victims might not be the only ones being watched... Erika's own life could be on the line")
    print('')
    print("The final key to the mayor's trust: Find the antonym of 'lost' from the extract and enter every alternate letter of the word.")
    ans=input("Enter answer: ")
    ans=ans.lower()
    if(ans!='fud' and ans!='on'):
        pa_l5-=1
        print("You answered wrong :(. The correct answer is 'on' or 'fud'")
    else:
        print("That was spot on!!")
    move_on(pa_l5)
    print("The mayor trusts you and realises theres no reason to hold back important information from you")
    time.sleep(var*1)
    print('"Mrs Argot left the part at 11:00 stating she had to bring some papers" he said sinisterly')
    time.sleep(var*1)
    print('"She had returned with a change in clothes which I felt was weird" he said and he definitely sounded like he was onto something')
    time.sleep(var*1)
    print('"I decided to check what these important papers were and," he said while pulling out some papers"I think you should go through them"')
    time.sleep(var*1)
    print('Your team along with the mayor set to work')
