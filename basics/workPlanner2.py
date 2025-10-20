from workInfo import checkList
from workInfo import day_multipliers, neighborhood_multipliers


def amountMadeFunc(base_pay, num_jobs_per_hr, hours, day_multiplier, neighborhood_multiplier):
    day_mult_value = list(day_multiplier.values())[0]
    neighborhood_mult_value = list(neighborhood_multiplier.values())[0]

    amountMade = base_pay * num_jobs_per_hr * hours * day_mult_value * neighborhood_mult_value
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