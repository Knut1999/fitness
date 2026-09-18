from DataHandler import DataHandler
from ObservationValidator import ObservationValidator


class SessionClassifyer:
    def __init__(self, dataHandler:DataHandler):
        self.dataHandler = dataHandler
        self.observations = self.dataHandler.observations
        self.participant = self.dataHandler.participant
        self.baseline_heart_rate = self.participant.profile["baseline_heart_rate"]
        self.insufficientData = self.findInsufficientData()
        self.sufficientData = len(self.observations) - self.findInsufficientData()
        self.beginningHR = self.dataHandler.heart_rate_summaryBeginning["Average"]
        self.endHR = self.dataHandler.heart_rate_summaryEnd["Average"]
        self.beginningActivity = self.dataHandler.activity_level_summaryBeginning["Average"]
        self.endActivity = self.dataHandler.activity_level_summaryEnd["Average"]


        self.HRpercentageDifference = (self.dataHandler.heart_rate_summary["Average"] - self.baseline_heart_rate) / self.baseline_heart_rate * 100
        self.activity_level = self.dataHandler.activity_level_summary["Average"]

        if(self.insufficientData > 0):
            self.classification = "Poor quality"
        elif(self.beginningHR > self.endHR and self.beginningActivity > self.endActivity):
            self.classification = "Recovering"
        elif(self.activity_level < 0.25 and abs(self.HRpercentageDifference) < 15):
            self.classification = "Resting"
        elif(self.activity_level >= 0.68 and self.HRpercentageDifference >= 40):
            self.classification = "High activity"
        elif(self.activity_level >= 0.38 and self.HRpercentageDifference >= 20):
            self.classification = "Moderate activity"
        else:
            self.classification = "Unknown"

    def findInsufficientData(self):
        i = 0
        for observation in self.observations:
            validate = ObservationValidator.validate(observation)
            #its valid if the dict "valid" is empty, but if it is not empty, we have corrupt data
            if not validate: 
                continue
            i += 1
        return i