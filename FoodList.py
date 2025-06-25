#A program that creates a list of food items and allows the user to add, remove, and display them.
import random
class Eat:
    Day=""
    Breakfast=""
    Lunch=""
    Dinner=""
breakList=["Utpam", "Puri Sabji", "Aaloo Paratha", "Pyazz Paratha & Bhujiya", "Chowmein", "Pasta", "Sandwich", "Pav Bhaji"]
lunchList=["Rajama Chawal", "Lauki", "Parwal", "Sehjan", "Bhindi", "Gobhi", "Dal Poori", "Baigan", "Palak"]
dinnerList=["Nenua", "Tadka", "Lemon Rice", "Mix Veg", "Aaloo Beans", "Nutrella", "Methi Lauki"]
dayList=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
def getRandomFood():
    eat=Eat()
    print("Days of the week are: ", dayList)
    eat.Day=input("Enter the day of the week: ")
    eat.Breakfast=random.choice(breakList)
    eat.Lunch=random.choice(lunchList)
    eat.Dinner=random.choice(dinnerList)
    return eat
def displayFood(eat):
    print("Day:         ", eat.Day)
    if eat.Day=="Saturday":
        eat.Lunch="Khichdi"
        eat.Dinner="Makuni Chokha"
    elif eat.Day=="Sunday":
        eat.Breakfast="Idli Sambhar"
        eat.Lunch="Pulao"
        eat.Dinner="Paneer"
    print("Breakfast:   ", eat.Breakfast)
    print("Lunch:       ", eat.Lunch)
    print("Dinner:      ", eat.Dinner)
displayFood(getRandomFood())
