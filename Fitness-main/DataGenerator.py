from dataGeneration.data_generator import generate_fitness_data
from Participant import Participant


class DataGenerator:
    def __init__(self, participant:Participant):
        self.participant_id = participant.participant_id
        self.scenario = participant.scenario
        self.seed = participant.seed
        self.number_of_windows = participant.number_of_windows

        self.profile, self.observations = generate_fitness_data(
            self.participant_id,
            self.scenario,
            self.seed,
            self.number_of_windows,
        )

        