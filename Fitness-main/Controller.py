import random

from Fitness import Fitness
from Participant import Participant


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
        id = self.__newParticipant_id()
        scenario = self.__userInputScenario()
        number_of_windows = self.__userInputWindow()
        seed = self.__seed
        self.__seed += 1

        return name, id, scenario, seed, number_of_windows


    def __userInputScenario(self):
        scenario = input("Enter scenario. \nNOTE! Enter one letter as input \nr = resting \nm = moderate_activity \nh = high_activity \nc = recovery \np = poor_quality \n")
        if scenario not in ["r", "m", "h", "c", "p"]:
            raise ValueError("Invalid scenario")    

        if scenario == "r":
            scenario = "resting"
        elif scenario == "m":
            scenario = "moderate_activity"
        elif scenario == "h":
            scenario = "high_activity"
        elif scenario == "c":
            scenario = "recovery"
        elif scenario == "p":
            scenario = "poor_quality"

        return scenario

    def __userInputWindow(self):
        number_of_windows:int = int(input("Enter how many windows you want\nNB! Must be more than 6\n"))
        if(type(number_of_windows) != int or number_of_windows < 6):
            raise ValueError("Must be more than 6 windows")

        return number_of_windows


    #This function updates the id
    def __newParticipant_id(self):
        if(self.__id == "P000"):
            self.__id = "P001"
            return self.__id
        #get the number in the id
        idInt:int = int(self.__id[1:])
        #increase the id
        idInt += 1
        #new id
        if(idInt >= 1000):
            raise ValueError("Too many id's, must be below 1000")
        elif(idInt >= 100):
            self.__id:str = str(f"P{idInt}")
            return self.__id
        elif(idInt >= 10):
            self.__id:str = str(f"P0{idInt}")   
            return self.__id
        elif(idInt < 10):
            self.__id:str = str(f"P00{idInt}")
            return self.__id


#class main:
#    controller1 = Controller()
