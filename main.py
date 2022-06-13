import random

start = input("Welcome to Smash Charades! Press enter to begin.")
print()

# reading files into list
file = open("characters.txt")
characters = [line for line in file]
file.close()

file = open("moves.txt")
moves = [line for line in file]
file.close()

file = open("specials.txt")
specials = [line for line in file]
file.close()

while True:
    start = input("Press enter to get your choice!")
    
    if random.randint(1,100) < 70:
        
        # get random index to assign to var && remove newline
        character = (characters[random.randint(0,88)])
        character = character.replace("\n", "")
        move = (moves[random.randint(0,19)])
        move = move.replace("\n", "")

        print(character + " using " + move)
        print()
    else:
        special = (specials[random.randint(0,len(specials) - 1)])
        special = special.replace("\n","")
        print(special)
        print()
