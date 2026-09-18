from Participant import Participant
from ObservationValidator import ObservationValidator

class DataHandler:
    def __init__(self, Participant: Participant):
        self.participant = Participant
        self.observations = self.participant.observations
        self.heart_rate_summary, self.skin_response_summary, self.temperature_summary, self.activity_level_summary, self.signal_quality_summary = self.average(self.observations)

        #Now lets make two lists from observations
        #One with the first three values and one with the last three
        #This way we can see if the heart rate is recovering near the end
        self.observationsBeginning = self.participant.observations[:3]
        self.observationsEnd = self.participant.observations[-3:]

        self.heart_rate_summaryBeginning = self.average(self.observationsBeginning)[0]
        self.heart_rate_summaryEnd = self.average(self.observationsEnd)[0]

        self.activity_level_summaryBeginning = self.average(self.observationsBeginning)[3]
        self.activity_level_summaryEnd = self.average(self.observationsEnd)[3]
        

    def average(self, observationList):
        heart_rates = []
        skin_responses = []
        temperatures = []
        activity_levels = []
        signal_qualities = []
        i = 0
        for observation in observationList:
            validate = ObservationValidator.validate(observation)
            if("heart_rate" not in validate):
                heart_rates.append(observation["heart_rate"])
            if("skin_response" not in validate):
                skin_responses.append(observation["skin_response"])
            if("temperature" not in validate):
                temperatures.append(observation["temperature"])
            if("activity_level" not in validate):
                activity_levels.append(observation["activity_level"])
            if("signal_quality" not in validate):
                signal_qualities.append(observation["signal_quality"])
            i += 1


        def calculate_summary(values):
            if len(values) > 0:
                return {
                    "Average": round(sum(values) / len(values),2),
                    "Maximum": round(max(values), 2),
                    "Minimum": round(min(values), 2),
                    "Invalid measurements": i - len(values)
                }

            return {
                "Average": None,
                "Maximum": None,
                "Minimum": None,
                "Invalid measurements": i - len(values)
            }
        
        heart_rate_summary = calculate_summary(heart_rates)
        skin_response_summary = calculate_summary(skin_responses)
        temperature_summary = calculate_summary(temperatures)
        activity_level_summary = calculate_summary(activity_levels)
        signal_quality_summary = calculate_summary(signal_qualities)

        return heart_rate_summary, skin_response_summary, temperature_summary, activity_level_summary, signal_quality_summary


# def main():
#     participant = Participant("Knut","P001","resting",42,10)
#     participant.profile = {'participant_id': 'P001', 'baseline_heart_rate': 78, 'baseline_skin_response': 1.17, 'baseline_temperature': 32.76}
#     participant.observations = [{'timestamp': 0, 'heart_rate': None, 'skin_response': 2.69, 'temperature': 32.41, 'activity_level': 0.37, 'signal_quality': 0.34},{'timestamp': 1, 'heart_rate': 265, 'skin_response': 2.18, 'temperature': 32.36, 'activity_level': 0.78, 'signal_quality': 0.36},{'timestamp': 2, 'heart_rate': 90, 'skin_response': 2.94, 'temperature': 32.56, 'activity_level': -0.2, 'signal_quality': 0.41},{'timestamp': 3, 'heart_rate': 54, 'skin_response': None, 'temperature': 32.11, 'activity_level': 0.77, 'signal_quality': 0.27},{'timestamp': 4, 'heart_rate': None, 'skin_response': 2.03, 'temperature': 31.87, 'activity_level': 0.82, 'signal_quality': 0.45},{'timestamp': 5, 'heart_rate': 265, 'skin_response': 2.78, 'temperature': 32.4, 'activity_level': 0.49, 'signal_quality': 0.46},{'timestamp': 6, 'heart_rate': 90, 'skin_response': 2.38, 'temperature': 32.49, 'activity_level': -0.2, 'signal_quality': 0.49},{'timestamp': 7, 'heart_rate': 80, 'skin_response': None, 'temperature': 32.29, 'activity_level': 0.2, 'signal_quality': 0.45},{'timestamp': 8, 'heart_rate': None, 'skin_response': 2.42, 'temperature': 31.78, 'activity_level': 0.31, 'signal_quality': 0.33},{'timestamp': 9, 'heart_rate': 265, 'skin_response': 1.95, 'temperature': 32.23, 'activity_level': 0.62, 'signal_quality': 0.53}]
#     dataHandler = DataHandler(participant)
#     dataHandler.average()
# main()
