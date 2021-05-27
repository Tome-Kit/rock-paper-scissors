'''
Created on May 27, 2021

@author: kalmer
'''
from numpy.matlib import rand
from builtins import input


class RockPaperScissors(object):
    '''
    This class describes a game of rock-paper-scissors in Estonian.
    '''
    '''
    @cvar winsOfComputer: The number of point wins of the computer.
    '''
    winsOfComputer = 0
    '''
    @cvar winsOfUser: The number of point wins of the user.
    '''
    winsOfUser = 0

    def __init__(self):
        '''
        Constructor
        '''
        import random
        '''
        @var randomIndex: the pseudorandom choice of the computer: either 1 (rock), 2 (paper) or 3 (scissors)
        '''
        randomIndex = random.randint(1, 3)
        '''
        @var rockPaperOrScissors: This variable contains the textual value of the user input which can be either "kivi" (rock), "paber" (paper) or "käärid" (scissors).
        '''
        rockPaperOrScissors = input("Kas kivi, paber või käärid? ")
        if ("kivi" == rockPaperOrScissors):
            if 2 == randomIndex:
                RockPaperScissors.winsOfComputer += 1
                print("Arvuti võitis punkti.")
            elif 3 == randomIndex:
                RockPaperScissors.winsOfUser += 1
                print("Sina võitsid punkti.")
            else:
                print("viik")
        elif "paber" == rockPaperOrScissors:
            if 3 == randomIndex:
                RockPaperScissors.winsOfComputer += 1
                print("Arvuti võitis punkti.")
            elif 1 == randomIndex:
                RockPaperScissors.winsOfUser += 1
                print("Sina võitsid punkti.")
            else:
                print("viik")
        elif "käärid" == rockPaperOrScissors:
            if 1 == randomIndex:
                RockPaperScissors.winsOfComputer += 1
                print("Arvuti võitis punkti.")
            elif 2 == randomIndex:
                RockPaperScissors.winsOfUser += 1
                print("Sina võitsid punkti.")
            else:
                print("viik")
        else:
            print("Palun kirjuta kas 'kivi', 'paber' või 'käärid'.")
            
        print("Arvuti on võitnud {0} punkti, sina oled võitnud {1} punkti.".format(RockPaperScissors.winsOfComputer, RockPaperScissors.winsOfUser))
        if (RockPaperScissors.winsOfComputer < 5) and (RockPaperScissors.winsOfUser < 5):
            RockPaperScissors()
        else:
            print("Mäng lõppes.")
            if RockPaperScissors.winsOfComputer > 4:
                print("Arvuti võitis mängu.")
            else:
                print("Sina võitsid mängu.")

        
RockPaperScissors()
