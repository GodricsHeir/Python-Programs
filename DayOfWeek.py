#This program functions on the basis of Zeller's Congruence algorithm to find the day of the week for a given date.
def day_of_week(year, month, day):
    # Adjust month and year for January and February
    if month < 3:
        month += 12
        year -= 1

    # Zeller's Congruence formula
    k = year % 100
    j = year // 100
    f = day + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) - (2 * j)
    day_of_week = f % 7

    # Map the result to the corresponding day of the week
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[day_of_week]


day=int(input("Enter day: "))
month=int(input("Enter month: "))
year=int(input("Enter year: "))
print("The day of the week is:", day_of_week(year, month, day))