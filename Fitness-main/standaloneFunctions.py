#Standalone functions

#This function updates the id
def newParticipant_id(id):
    if(id == "P000"):
        id = "P001"
        return id
    #get the number in the id
    idInt:int = int(id[1:])
    #increase the id
    idInt += 1
    #new id
    if(idInt >= 1000):
        raise ValueError("Too many id's, must be below 1000")
    elif(idInt >= 100):
        id:str = str(f"P{idInt}")
        return id
    elif(idInt >= 10):
        id:str = str(f"P0{idInt}")   
        return id
    elif(idInt < 10):
        id:str = str(f"P00{idInt}")
        return id

def userInputScenario():
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

def userInputWindow():
    number_of_windows:int = int(input("Enter how many windows you want\nNB! Must be more than 6\n"))
    if(type(number_of_windows) != int or number_of_windows < 6):
        raise ValueError("Must be more than 6 windows")

    return number_of_windows

#values er liste med tall og i er 
def calculate_summary(values, i):
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