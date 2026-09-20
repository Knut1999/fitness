from ObservationValidator import ObservationValidator
from standaloneFunctions import newParticipant_id, calculate_summary
print("test for some important functions")

def newParticipantIdTest():
    print("Testing with ID P001")
    print(f"New ID is {newParticipant_id('P001')}")
    
    print("Testing with ID P010")
    print(f"New ID is {newParticipant_id('P010')}")
    
    print("Testing with ID P100")
    print(f"New ID is {newParticipant_id('P100')}")


def calculate_summaryTest():
    print("Testing summary function")
    print(calculate_summary([1,2,3,4,5,6,7,8,9], 10))

def ObservationValidatorTest():
    print("First check static function with valid numbers")
    print(ObservationValidator.validate({
        "heart_rate": 65,
        "skin_response": 1.4,
        "activity_level": 0.12,
        "signal_quality": 0.13,
    }))
    
    print("Now check static function with non-valid numbers")
    print(ObservationValidator.validate({
        "heart_rate": 645,
        "skin_response": None,
        "activity_level": 4.12,
        "signal_quality": 10.13,
    }))
    



newParticipantIdTest()
calculate_summaryTest()
ObservationValidatorTest()