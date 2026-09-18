from DataGenerator import DataGenerator
from DataHandler import DataHandler
from Participant import Participant
from GenerateReport import GenerateReport
from SessionClassifyer import SessionClassifyer

class Fitness:
    def __init__(self, participants: list[Participant]):
        self.participants = participants

        #We first get the data from the fitness tracker
        i = 0
        for participant in self.participants:
            dataGenerator = DataGenerator(participant)

            #Connect the training data to our participant
            participant.profile = dataGenerator.profile
            participant.observations = dataGenerator.observations

            # Now we need to handle the data
            dataHandler = DataHandler(participant)
            sessionClassifyer = SessionClassifyer(dataHandler) 

            # Generate report
            i += 1
            generateReport = GenerateReport(dataHandler, sessionClassifyer, i)
            print(generateReport)

        
