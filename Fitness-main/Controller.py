import random

from Fitness import Fitness
from Participant import Participant
from standaloneFunctions import newParticipant_id, userInputScenario, userInputWindow


class Controller: 
    __id = "P000"
    __seed = 0
    #Konstruktør, her lager vi våres objekter
    def __init__(self):
        self.participants = [] #create participants
        
        while True:
            name, id, scenario, seed, number_of_windows = self.__createParticipant()
            participant = Participant(name, id, scenario, seed, number_of_windows)
            self.participants.append(participant)
            stop = input("Do you wanr more participants? Yes: y, No: n\n")
            
            if(stop == "y"): 
                continue
            elif(stop == "n"):
                break
            else:
                raise ValueError("Må enten være y eller n")

        fitness = Fitness(self.participants) 
            

    #Her lager vi våre participants
    def __createParticipant(self):
        #Get info aboout new participant
        name = input("Name on the participant: ")
        id = newParticipant_id(self.__id)
        self.__id = id
        scenario = userInputScenario()
        number_of_windows = userInputWindow()
        seed = self.__seed
        self.__seed += 1

        return name, id, scenario, seed, number_of_windows



