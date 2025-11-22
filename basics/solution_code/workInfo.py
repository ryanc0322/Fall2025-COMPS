day_multipliers = {
    'Monday' : 1,
    'Tuesday' : 1.05,
    'Wednesday' : 1,
    'Thursday' : 1,
    'Friday' : 1.1,
    'Saturday' : 1.4,
    'Sunday' : 1.4
}

neighborhood_multipliers = {
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
    if first in day_multipliers :
        for item in givenList :
            if item in seen :
                raise ValueError("There is a duplicate day in your list of days.  \nMake sure there is only one of each of the days you are selecting")
            elif item in day_multipliers:
                seen.add(item)
                total = total * day_multipliers[item]
            else :
                 raise ValueError("You have entered something invalid to your days list.  \nPlease check to make sure there are only either 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', or 'Sunday' in your list.")

    elif first in neighborhood_multipliers :
        for item in givenList :
            if item in seen :
                raise ValueError("There is a duplicate neighborhood in your list of days.  \nMake sure there is only one of each of the neighborhoods you are selecting")
            elif item in neighborhood_multipliers:
                seen.add(item)
                total = total * neighborhood_multipliers[item]
            else:
                raise ValueError("You have entered something invalid to your neighborhoods list.  \nPlease check to make sure there are only either 'A', 'B', 'C', or 'D' in your list.")
    else :
        raise ValueError("You have entered something into the list that is not a valid day or neighborhood.\nPlease check both your neighborhoods and you days lists and make sure that you only have either 'A', 'B', 'C', or 'D' in the neighborhoods list \nand 'Monday', 'Tuesday', 'Wednesday', 'Thursday', or 'Friday' in the days list.")
    return total

