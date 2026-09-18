from DataHandler import DataHandler
from SessionClassifyer import SessionClassifyer


class GenerateReport:
    def __init__(self, DataHandler: DataHandler, SessionClassifyer: SessionClassifyer, i):
        self.i = i
        self.dataHandler = DataHandler
        self.sessionClassifyer = SessionClassifyer
        self.participant = self.dataHandler.participant

    def __str__(self):
        
        result = (f"{'=' * 50} \n")
        result += (f"FITNESS SESSION REPORT {self.i}\n")
        result += (f"{'=' * 50}\n")
        result += (f"\n")
        result += (f"Navn: {self.participant.name} \n")
        result += (f"Reference ID: {self.participant.profile['participant_id']}") + "\n"
        result += (f"Baseline heart_rate: {self.participant.profile['baseline_heart_rate']}bpm") + "\n"
        result += (f"Baseline skin response : {self.participant.profile['baseline_skin_response']}") + "\n"
        result += (f"Baseline temperature: {self.participant.profile['baseline_temperature']}°C") + "\n"
        result += f"Number of windows: {self.participant.number_of_windows} \n"
        result += f"Session classification: {self.participant.scenario} (This is the one used in data_generator)\n"
        result += f"Session classification: {self.sessionClassifyer.classification} (This is the one we found by analyzing the numbers)\n"
        result += "\n"

        result += (f"Heart rate summary\t\t|Skin response summary:\t\t|Temperature summary:\t\t|Activity level summary:\t|Signal quality summary:\n")
        result += (f"Average:                {self.dataHandler.heart_rate_summary["Average"]}" f"\t|" f"Average:                {self.dataHandler.skin_response_summary["Average"]}" f"\t|" f"Average:                {self.dataHandler.temperature_summary["Average"]}" f"\t|" f"Average:                {self.dataHandler.activity_level_summary["Average"]}" f"\t|" f"Average:                {self.dataHandler.signal_quality_summary["Average"]}\n")
        result += (f"Maximum:                {self.dataHandler.heart_rate_summary["Maximum"]}" f"\t|" f"Maximum:                {self.dataHandler.skin_response_summary["Maximum"]}" f"\t|" f"Maximum:                {self.dataHandler.temperature_summary["Maximum"]}" f"\t|" f"Maximum:                {self.dataHandler.activity_level_summary["Maximum"]}" f"\t|" f"Maximum:                {self.dataHandler.signal_quality_summary["Maximum"]}\n")
        result += (f"Minimum:                {self.dataHandler.heart_rate_summary["Minimum"]}" f"\t|" f"Minimum:                {self.dataHandler.skin_response_summary["Minimum"]}" f"\t|" f"Minimum:                {self.dataHandler.temperature_summary["Minimum"]}" f"\t|" f"Minimum:                {self.dataHandler.activity_level_summary["Minimum"]}" f"\t|" f"Minimum:                {self.dataHandler.signal_quality_summary["Minimum"]}\n")
        result += (f"Invalid measurements:   {self.dataHandler.heart_rate_summary["Invalid measurements"]}" f"\t|" f"Invalid measurements:   {self.dataHandler.skin_response_summary["Invalid measurements"]}" f"\t|" f"Invalid measurements:   {self.dataHandler.temperature_summary["Invalid measurements"]}" f"\t|" f"Invalid measurements:   {self.dataHandler.activity_level_summary["Invalid measurements"]}" f"\t|" f"Invalid measurements:   {self.dataHandler.signal_quality_summary["Invalid measurements"]}\n")

        result += (f"\n")
        result += (f"{'=' * 50}\n")
        result += (f"RECOVERY \n")
        result += (f"{'=' * 50} \n")
        if(self.dataHandler.heart_rate_summaryBeginning["Invalid measurements"] != 0 or self.dataHandler.heart_rate_summaryEnd["Invalid measurements"]):
            result += f"Can not check the recovery because of invalid messurements in the beginning/end \n"
        else:
            result += f"Heart rate avg in the first 3 messurements: {self.dataHandler.heart_rate_summaryBeginning["Average"]} \n"
            result += f"Heart rate avg in the last 3 messurements: {self.dataHandler.heart_rate_summaryEnd["Average"]} \n"
            if(self.dataHandler.heart_rate_summaryBeginning["Average"] > self.dataHandler.heart_rate_summaryEnd["Average"]):
                result += "Heart rate did recover well near the end \n"
            else:
                result += "Heart rate did not recover well near the end \n"

        if(self.dataHandler.activity_level_summaryBeginning["Invalid measurements"] != 0 or self.dataHandler.activity_level_summaryEnd["Invalid measurements"]):
            result += f"Can not check the recovery because of invalid messurements in the beginning/end \n"
        else:
            result += f"Activity level in the first 3 messurements: {self.dataHandler.activity_level_summaryBeginning["Average"]} \n"
            result += f"Activity level in the last 3 messurements: {self.dataHandler.activity_level_summaryEnd["Average"]} \n"
            if(self.dataHandler.activity_level_summaryBeginning["Average"] > self.dataHandler.activity_level_summaryEnd["Average"]):
                result += "Activity level did recover well near the end"
            else:
                result += "Activity level did not recover well near the end"

        return result