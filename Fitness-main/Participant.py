class Participant:
    def __init__(self, name, participant_id, scenario, seed, number_of_windows):
        self.name = name
        self.participant_id = participant_id
        self.scenario = scenario
        self.seed = seed
        self.number_of_windows = number_of_windows

        #fremtidig data
        self.profile = None
        self.observations = None
