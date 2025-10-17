class dayParams :
    multipliers = {
        'Monday' : 1,
        'Tuesday' : 1.05,
        'Wednesday' : 1,
        'Thursday' : 1,
        'Friday' : 1.1,
        'Saturday' : 1.4,
        'Sunday' : 1.4
    }

class neighborhoodParams :
    multipliers = {
        'A' : 1.05,
        'B' : 1.1,
        'C' : 1.08,
        'D' : 1.07
    }

def checkList(givenList)  :
    total = 1
    if not givenList :
        raise ValueError("There are no entries in the given list.  \nPlease check both your neighborhoods and your days lists and make sure that there are values there that correspond to what the list is looking for.")
    seen = set()
    first = givenList[0]
    if first in dayParams.multipliers :
        for item in givenList :
            if item in seen :
                raise ValueError("There is a duplicate day in your list of days.  \nMake sure there is only one of each of the days you are selecting")
            elif item in dayParams.multipliers:
                seen.add(item)
                total = total * dayParams.multipliers[item]
            else :
                 raise ValueError("You have entered something invalid to your days list.  \nPlease check to make sure there are only either 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', or 'Sunday' in your list.")

    elif first in neighborhoodParams.multipliers :
        for item in givenList :
            if item in seen :
                raise ValueError("There is a duplicate neighborhood in your list of days.  \nMake sure there is only one of each of the neighborhoods you are selecting")
            elif item in neighborhoodParams.multipliers:
                seen.add(item)
                total = total * neighborhoodParams.multipliers[item]
            else:
                raise ValueError("You have entered something invalid to your neighborhoods list.  \nPlease check to make sure there are only either 'A', 'B', 'C', or 'D' in your list.")
    else :
        raise ValueError("You have entered something into the list that is not a valid day or neighborhood.\nPlease check both your neighborhoods and you days lists and make sure that you only have either 'A', 'B', 'C', or 'D' in the neighborhoods list \nand 'Monday', 'Tuesday', 'Wednesday', 'Thursday', or 'Friday' in the days list.")
    return total

def amountMadeFunc(base_pay, num_jobs_per_hr, hours, day_multiplier, neighborhood_multiplier):
    dayMultiplier = checkList(days)
    neighborhoodMultiplier = checkList(neighborhoods)
    amountMade = base_pay * num_jobs_per_hr * hours * dayMultiplier * neighborhoodMultiplier
    return amountMade

def deductionFunc(milesTraveled, fuelEfficiency, costOfFuel):
    deduction = (milesTraveled / fuelEfficiency) * costOfFuel
    return deduction

def valueFunc(amountMade, deduction):
    value = amountMade - deduction
    return value


def main() :
    name = input("What is your name: ")
    hours = int(input("How many hours will you work: "))
    neighborhoodInput = input("Enter the neighborhoods you want to work seperated by a space: ").split()
    neighborhoods = list(neighborhoodInput)
    dayInput = input("Enter the days you want to work seperated by a space: ").split()
    days = list(dayInput)
    fuelEfficiency = int(input("What is the fuel efficiency of your vehicle: "))
    milesTraveled = int(input("How many miles are you traveling: "))
    costOfFuel = float(input("What is the cost of fuel: "))
    dayMultiplier = checkList(days)
    neighborhoodMultiplier = checkList(neighborhoods)
    print(f"{name} is expected to make: ${value:.2f}")

if __name__=='__main__':
    main()