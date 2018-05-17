import random

number = random.randint(0,3)

words = ["Black Knight","Dark Voyager","The Reaper","Havoc"]
hint1 = ["Tier 70 in Season 2","Tier 70 in Season 3","Tier 100 in Season 3","Twitch Prime pack"]
hint2 = ["he is the last skin in the Season 2 Battle Pass","he has orange highlights","he looks like John Wick","the camouflage raptor"]

secretword = words[number]

guess = ""
counter = 1

while True:
    print("Guess the secret word")
    print("Type 'hint1', 'hint2', 'first letter', or 'give up', for answer.")
    guess = input()

    if guess == secretword:
        print("You won!")
        print("it took you " + str(counter) + " guesses.")
        break
    elif guess == "hint1":
        print( hint1[number1] )
    elif guess == "hint2":
        print( hint2[number] )
    elif guess == "first letter":
        print("You gave up.")
        print("You failed " + str(counter)+ " times.")
        break
    
    else:
        print("Guess again.")
        counter += 1
