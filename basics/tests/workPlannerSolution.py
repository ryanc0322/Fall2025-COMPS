from workInfo import checkList
from workInfo import day_multipliers, neighborhood_multipliers


def amount_made_func(base_pay, num_jobs_per_hr, hours, day_multiplier, neighborhood_multiplier):
    day_mult_value = list(day_multiplier.values())[0]
    neighborhood_mult_value = list(neighborhood_multiplier.values())[0]

    amount_made = base_pay * num_jobs_per_hr * hours * day_mult_value * neighborhood_mult_value
    return amount_made

def deduction_func(miles_traveled, fuel_efficiency, cost_of_fuel):
    deduction = (miles_traveled / fuel_efficiency) * cost_of_fuel
    return deduction

def value_func(amount_made, deduction):
    value = amount_made - deduction
    return value


def main() :
    name = input("What is your name: ")
    hours = int(input("How many hours will you work: "))
    neighborhood_input = input("Enter the neighborhoods you want to work seperated by a space: ").split()
    neighborhoods = list(neighborhood_input)
    day_input = input("Enter the days you want to work seperated by a space: ").split()
    days = list(day_input)
    fuel_efficiency = int(input("What is the fuel efficiency of your vehicle: "))
    miles_traveled = int(input("How many miles are you traveling: "))
    cost_of_fuel = float(input("What is the cost of fuel: "))
    day_multiplier = checkList(days)
    neighborhood_multiplier = checkList(neighborhoods)
    amount_made = amount_made_func(10, 2, hours, day_multiplier, neighborhood_multiplier)
    deduction = deduction_func(miles_traveled, fuel_efficiency, cost_of_fuel)
    value = value_func(amount_made, deduction)
    print(f"{name} is expected to make: ${value:.2f}")

if __name__=="__main__":
    main()