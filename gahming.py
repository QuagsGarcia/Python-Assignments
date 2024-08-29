#imports for vectors and random numbers
from collections import namedtuple
import random

# vector3 classifications
Vector3 = namedtuple('Vector3', ['x', 'y', 'z'])
# version string for beginning print
version = "v0.1 ALPHA"
# stats to decide when the game ends
money = 200
karma = 50
health = 100
#used to print out the options while updating the stats when selecting one or two
def process_choice(options):
    tbloptions = []
    tbloutcomes = []
    #used to add values for each option to change stats
    for option, outcome in options.items():
        tbloptions.append(option)
        tbloutcomes.append(outcome)
    #multiple choice prompt
    print(f"Options: [1] {tbloptions[0]} [2] {tbloptions[1]}")
    choice = input("Enter your choice (1 or 2): ")
    #used to see if the person typed 1 or 2
    while choice not in ["1", "2"]:
        #error message for not choosing 1 or 2
        print("Invalid choice. Please enter 1 or 2.")
        #used to ask for another input
        choice = input("Enter your choice (1 or 2): ")
    #used for getting a specific table value, using -1 bc it starts at 0 not 1
    choice_index = int(choice) - 1
    #separting values from vector3 into 3 separtate variables
    money_change, karma_change, health_change = tbloutcomes[choice_index]
    #returns the values of the Vectors in outcome
    return money_change, karma_change, health_change
#main choice function
def mainChoice():
    #used to get the stats
    global money, karma, health
    #checks to see if you have high karma for good choices or low karma for bad choices. uses the total length of options in random select for compatibility
    if karma >= 50:
        #rng number based on option length
        rng = random.randint(0, len(goodOptions) - 1)
        #separates the prompt message and options
        prompt, options = goodOptions[rng]
    else:
        #rng number based on option length
        rng = random.randint(0, len(badOptions) - 1)
        #separates the prompt message and options
        prompt, options = badOptions[rng]
    #prints the scenario
    print(prompt)
    #gets the stat changes defined in the table with vector3
    money_change, karma_change, health_change = process_choice(options)
    #stat update
    money += money_change
    karma += karma_change
    health += health_change
    #prints the stats so the user knows where they are at for decision making
    stat()
    #used to check if the users luck has run out
    if karma <= 0:
        #kills player
        health = 0
        print("A person decided you were their next victim.")

    #used to check if the user can afford to eat
    if money <= 0:
        #kills player
        health = 0
        print("You no longer can afford to eat.")
    # if the user survives, another choice is presented, other wise they have to restart the game
    if health > 0:
        mainChoice()
    else:
        # restart game logic with default values
        rstcmd = input('You have died. To play again type /restart: ')
        while rstcmd != "/restart":
            rstcmd = input("Invalid Command.\nTo play again type /restart: ")
        #resets stats
        money = 200
        karma = 50
        health = 100
        stat()
        mainChoice()
# prints the stats
def stat():
    print(f"Current Stats:\nMoney = {money}\nKarma = {karma}\nHealth = {health}")
# used for the inital start of the game
def startGame():
    #greeting message
    print(f"Welcome to Adventure Simulator ({version})")
    while True:
        # used to check what the default values are or to start the game
        choice = input('To start type "/start", to check your stats, type "/stat": ')
        if choice == "/start":
            mainChoice()
        elif choice == "/stat":
            stat()
        else:
            print("Invalid Command.")
#used for the good options starting with the prompt then the options with their values in vector3 coorelating to stats
goodOptions = [
    ["You are driving down the road and see a lemonade stand.", {"Keep Driving": Vector3(0, -10, 0), "Buy Lemonade": Vector3(-10, 5, 25)}],
    ["You are driving down the road and see a person standing on the side of the road.", {"Help Them": Vector3(50, 10, 0), "Keep Driving": Vector3(0, -5, 0)}]
]
#used for the bad options starting with the prompt then the options with their values in vector3 coorelating to stats
badOptions = [
    ["Your vehicle has broken down and needs to be towed.", {"Call Tow Truck": Vector3(-150, 10, 0), "Start Walking": Vector3(0, -40, -50)}],
    ["A tornado has occurred.", {"Keep Driving": Vector3(0, -100, -100), "Find Shelter": Vector3(-100, 20, 0)}]
]
#used to start the game
startGame()