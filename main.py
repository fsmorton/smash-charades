import random

start = input("Welcome to Smash Charades! Press enter to begin.")
print("\n")

# reading files into list
with open("characters.txt") as file
    characters = list(file)

with open("moves.txt") as file
    moves = list(file)

with open("specials.txt") as file:
    specials = list(file)

while True:
    start = input("Press enter to get your choice!")
    
    if random.randint(1, 100) < 90:
        character = random.choice(characters)
        character = character.replace("\n", "")
        
        move = random.choice(moves)
        move = move.replace("\n", "")

        print(f"{character} using {move}\n")
    else:
        special = random.choice(specials)
        special = special.replace("\n","")
        print(f"{special}\n")
