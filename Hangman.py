import random
words = [
    "planet", "animal", "school", "pencil", "garden", "friend", "family", "summer", "window", "forest",
    "rocket", "orange", "bridge", "castle", "pirate", "jungle", "desert", "island", "butter", "cookie",
    "mountain", "river", "teacher", "library", "science", "history", "bottle", "camera", "pillow", "blanket",
    "market", "basket", "rabbit", "turtle", "monkey", "shadow", "puzzle", "ticket", "planet", "circle",
    "adventure", "treasure", "volcano", "diamond", "whistle", "lantern", "compass", "harvest", "journey", "magnet",
    "parade", "rainbow", "shelter", "tractor", "unicorn", "voyage", "weather", "zebra", "yogurt", "quartz"
]
word = words[random.randint(0, len(words)-1)]
incorrect=0 #can go upto 6
correct = 0
print("The word has ", len(word), " letters")
dash=[]
for i in range(len(word)):
    dash.append("_")
print(" ".join(dash))


def guess(letter):
    global incorrect
    global correct
    if letter in word:
        correct+=1
        print("Correct guess")
        for i in range(len(word)):
            if word[i] == letter:
                dash[i] = letter
        print(" ".join(dash))
    else:
        incorrect+=1
        print("Incorrect guess")
        print("You have ", 6-incorrect, " guesses left")
        print(" ".join(dash))


while(incorrect<6):
    letter=input("Enter a letter: ")
    if(letter=="Reveal"):
        print("The word is: ", word)
        break
    if(letter==word):
        print("You win")
        print ("The word is: ", word)
        break       
    guess(letter)
    if correct == len(word):
        print("You win")
        print ("The word is: ", word)
        break
if incorrect == 6:
    print("You lose")
    print ("The word was: ", word)