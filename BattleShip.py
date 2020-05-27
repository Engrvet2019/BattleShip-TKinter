import random
from tkinter import *
import time
from tkinter import Tk, Label, Button

root = Tk()

# Menu makes widget so that option such as 'New', 'Open', and 'Exit' to be accessed while playing the game.  This menu is labeled as File and becomes a drop down for those options listed above.  Since we couldnt connect a built in command for 'New' or 'Open' game we had to leave it out.
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
# filemenu.add_command(label='New')
# filemenu.add_command(label='Open')
# filemenu.add_separator()
# Menu bar option 'Exit' + Command allows to exit game

# Command root.quit gives the player manual exit of the game. Which we connected this command built-in function to work with the 'Exit' Label in File menu.
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
# menu.add_cascade(label='Help', menu=helpmenu)
# helpmenu.add_command(label='About')


# --------------------------------------

# Global list of the coordinates the bot has chosen
botHitList = []
# The global list of the current sunken ships in the game
currentSunkenShips = []


# Create the base game

#   #Create a way for each player to choose a spot on the grid
#   #Add a list of battleships each player has
#   #Add game mechanics such as hit or miss a ship
#   #Keep track of each coordinate the players chooses
#   #Implement end game mechanics where person whose all ships are gone loses

# This is a function that is called when the bot or player loses all of their ships
def endGame():
    print("The game will exit in 10 seconds!")
    # This will pause the program for 10 seconds
    time.sleep(10)
    print("The game will now exit!")
    # This will quit out of the game
    root.quit()


# Checks whether or not a ship already has a specific coordinate or not
def checkShips(coordinate):
    # Creates a list of all the current global ship objects
    shipOjectList = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10, ship11, ship12]
    # Creates an empty coordinate list to add the coordinates of the ships into
    coordList = []
    # This loop iterates through each ship object and adds it's coordinate to the coord list, list
    for ship in shipOjectList:
        coordList.append(ship.getCoords())
    # This loop iterates through the coordinate list
    for coordGroup in coordList:
        for newCoordinate in coordGroup:
            if coordinate == newCoordinate:
                return True
    return False


# This function checks if the coordinate given is equal to one of the bot's ship's coordinates. If it is equal then it adds a damage to the ship
def checkButtonShips(coordinate):
    # Creates a list of all the current global ship objects
    shipOjectList = [ship1, ship2, ship3, ship4, ship5, ship6]
    # Creates an empty coordinate list to add the coordinates of the ships into
    coordList = []
    # This loop iterates through each ship object and adds it's coordinate to the coord list, list
    for ship in shipOjectList:
        coordList.append(ship.getCoords())

    # The count variable is corresponding to each ship in the object list. The 0 index is ship1, the first index is ship2 and so on
    count = -1

    # This loop goes through each group of coordinates that correspond with each ship
    for coordGroup in coordList:
        # Count is added each time through the loop to go with each ship's group coordinates
        # For example, the first time this loop is called count is 0 which is ship1
        count += 1
        # Loops through the coordinates in each index of the coordList array
        for newCoordinate in coordGroup:
            # If the coordinate is equal to the current coordinate selected in the loop
            if coordinate == newCoordinate:
                # Depending on the count number, add a damage to the ship if the coordinate given to this function is equal to one of the ship's coordinate
                if count == 0:
                    ship1.addDamage(1)
                    return True
                elif count == 1:
                    ship2.addDamage(1)
                    return True
                elif count == 2:
                    ship3.addDamage(1)
                    return True
                elif count == 3:
                    ship4.addDamage(1)
                    return True
                elif count == 4:
                    ship5.addDamage(1)
                    return True
                elif count == 5:
                    ship6.addDamage(1)
                    return True

    return False


# This function checks if the coordinate given is equal to one of the player's ship's coordinates. If it is equal then it adds a damage to the ship
def hitOrMiss(coord):
    # Puts the player's ships coordinates into a list
    shipCoordList = [ship7.getCoords(), ship8.getCoords(), ship9.getCoords(), ship10.getCoords(), ship11.getCoords(),
                     ship12.getCoords()]

    # The count variable is corresponding to each ship in the object list. The 0 index is ship7, the first index is ship8 and so on
    count = -1

    # This loop goes through each group of coordinates that correspond with each ship
    for coordGroup in shipCoordList:

        # Count is added each time through the loop to go with each ship's group coordinates
        # For example, the first time this loop is called count is 0 which is ship7
        count += 1
        for currentCoord in coordGroup:
            # If the coordinate given is equal to the coordinate in the loop, add a damage to the ship that corresponds with the count number. Then the function returns true.
            if coord == currentCoord:
                if count == 0:
                    ship7.addDamage(1)
                    return True
                elif count == 1:
                    ship8.addDamage(1)
                    return True
                elif count == 2:
                    ship9.addDamage(1)
                    return True
                elif count == 3:
                    ship10.addDamage(1)
                    return True
                elif count == 4:
                    ship11.addDamage(1)
                    return True
                elif count == 5:
                    ship12.addDamage(1)
                    return True

    # If the coordinate given does not equal any of the ship's coordinates then the function returns false.
    return False


# Creates the coordinates for all of the ships
def placeShips(currentShip, alphabet):
    # Gets a random number from 1-2
    randNum = random.randrange(1, 3)
    # If the number is one, it will create coordinates that flow vertically
    if randNum == 1:
        # Choose a random number between 1,11-the current ships length
        numChoice = random.randrange(1, 10 - currentShip.getShipLength())
        # Choose a random letter of the alphabet A-J
        letterChoice = random.choice(alphabet)
        # Creates a coordinate by merging the random num and letter. Ex: 6A
        coord = str(numChoice) + letterChoice
        # Gets the ship length from global ship object
        shipLength = currentShip.getShipLength()
        # Creates an empty list that the ships coords will be stored
        allCoords = []
        # Check whether checkShips is true
        if checkShips(coord):
            # If it is a true, then placeShips is run again, creating a new coordinate
            return placeShips(currentShip, alphabet)
        # If checkShips return false, the coordinate is added to the allCoords list
        allCoords.append(coord)
        # Creates a loop that runs 0 to the the ship length-1
        for i in range(shipLength - 1):
            # Adds one to the numChoice random number between 1,10
            numChoice += 1
            # If that coordinate is already taken
            # then run placeShips again
            if checkShips(str(numChoice) + letterChoice):
                return placeShips(currentShip, alphabet)
                # If the number is less than 10 and isn't already taken, then add that number plus the letter to the coordinate list
            allCoords.append(str(numChoice) + letterChoice)
        # Once the coords of the ship are all created and checked, the coordinates are returned and added to the global ship value's coordinates
        return allCoords
    # If the number is not one, it will create coordinates that flow horizontally
    else:
        # Choose a random number between 1,10
        numChoice = random.randrange(1, 10)
        # Choose a random index number between 0 and 10 minus the current ship's length
        newIndex = random.randrange(10 - currentShip.getShipLength())
        # Makes the letter choice a letter from the alphabet with the new index found
        letterChoice = alphabet[newIndex]
        # Creates a coordinate by merging the random num and letter. Ex: 6A
        coord = str(numChoice) + letterChoice
        # Gets the ship length from global ship object
        shipLength = currentShip.getShipLength()
        # Creates an empty list that the ships coords will be stored
        allCoords = []
        # Check whether checkShips is true
        if checkShips(coord):
            # If it is a true, then placeShips is run again, creating a new coordinate
            return placeShips(currentShip, alphabet)
        # If checkShips return false, the coordinate is added to the allCoords list
        allCoords.append(coord)
        # Creates a loop that runs 0 to the the ship length-1
        for i in range(shipLength - 1):
            # Gets the current index of the letter choice variable in alphabet and adds one to it
            letterIndex = alphabet.index(letterChoice) + 1
            # Reassign letter choice to a letter in the alphabet with the new letter index
            letterChoice = alphabet[letterIndex]
            # If that coordinate is already taken
            # then run placeShips again
            if checkShips(str(numChoice) + letterChoice):
                return placeShips(currentShip, alphabet)
                # If the isn't already taken, then add that number plus the letter to the coordinate list
            allCoords.append(str(numChoice) + letterChoice)
        # Once the coords of the ship are all created and checked, the coordinates are returned and added to the global ship value's coordinates
        return allCoords


# This function starts the game
def startGame():
    # Creates a list of ship names
    shipList = ["BattleShip", "Cruiser", "Destroyer", "Submarine", "Carrier", "Ptboat"]
    # Creates the alphabet A-J for the coordinates and buttons
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    print(
        "Welcome to Battleship! Your current ships will be listed below. The screen you are seeing is the board where your opponent's ships are! Try to destroy the opponent's ships before yours get destroyed!  Click a button to choose the coordinate to fire at. If the button turns blue, then you missed! If the button turns red, then you've hit one of the bot's ships!")
    # this loops through all the current ship names
    for ship in shipList:
        # Checks what the ship name is
        if ship == "BattleShip":
            # Sets the global ship object's name to the looped ship and sets the coords using the placeShips function
            ship1.setCoords(placeShips(ship1, alphabet))
        if ship == "Cruiser":
            ship2.setCoords(placeShips(ship2, alphabet))
        if ship == "Destroyer":
            ship3.setCoords(placeShips(ship3, alphabet))
        if ship == "Submarine":
            ship4.setCoords(placeShips(ship4, alphabet))
        if ship == "Carrier":
            ship5.setCoords(placeShips(ship5, alphabet))
        if ship == "Ptboat":
            ship6.setCoords(placeShips(ship6, alphabet))
    # this loops through all the current ship names
    for ship in shipList:
        # Checks what the ship name is
        if ship == "BattleShip":
            # Sets the global ship object's name to the looped ship and sets the coords using the placeShips function
            ship7.setCoords(placeShips(ship7, alphabet))
        if ship == "Cruiser":
            ship8.setCoords(placeShips(ship8, alphabet))
        if ship == "Destroyer":
            ship9.setCoords(placeShips(ship9, alphabet))
        if ship == "Submarine":
            ship10.setCoords(placeShips(ship10, alphabet))
        if ship == "Carrier":
            ship11.setCoords(placeShips(ship11, alphabet))
        if ship == "Ptboat":
            ship12.setCoords(placeShips(ship12, alphabet))

    # Puts all the ship objects into a list
    currentShips = [ship7, ship8, ship9, ship10, ship11, ship12]
    # Prints the current player ships and their coordinates
    print("Here are your ships:")
    for ship in currentShips:
        print("Ship: {} at coords: {}".format(ship.getShipName(), ship.getCoords()))


# This function checks and updates the list of the current sunken ships list
def checkSunkenShips():
    # Gets the currentSunkenShips list
    global currentSunkenShips

    # Puts all the ship objects into a list
    currentShips = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10, ship11, ship12]
    # For each ship in the currentShips list, it checks if the ship is sunk and is not currently in the currentSunkenShips list. If true, then it adds the ship to the list and prints that is had been sunk
    for ship in currentShips:
        if ship.checkIfSunk() and ship not in currentSunkenShips:
            currentSunkenShips.append(ship)
            print("The", ship.getStatus() + "'s", ship.getShipName(), "has sunk!")


# This function handles the bot's turn
def botTurn():
    # Gets the coordinates the bot has hit
    global botHitList
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    randomNum = random.randrange(1, 11)
    randomLetter = random.choice(alphabet)
    coord = str(randomNum) + randomLetter
    # Generates a random coord by getting a random letter from the list and a random number 1-10

    # if the coordinate is already in the botHitList then create a new coordinate
    while coord in botHitList:
        randomNum = random.randrange(1, 11)
        randomLetter = random.choice(alphabet)
        coord = str(randomNum) + randomLetter
    # Then add the coord to the botHitList
    botHitList.append(coord)

    # Checks if the coordinate hit's or misses the player's ships
    if hitOrMiss(coord):
        print("Bot chose", coord + "...", "it was a hit!")
    else:
        print("Bot chose", coord + "...", "it was a miss!")


# This function checks whether the bot or player has won.
def checkWinner():
    # Two lists are created. One with 6 true or false statements corresponding with if the player ships have sunk, and one with 6 true or false statements corresponding with the if the bot's ships have sunk
    currentPlayerShips = [ship7.checkIfSunk(), ship8.checkIfSunk(), ship9.checkIfSunk(), ship10.checkIfSunk(),
                          ship11.checkIfSunk(), ship12.checkIfSunk()]
    currentBotShips = [ship1.checkIfSunk(), ship2.checkIfSunk(), ship3.checkIfSunk(), ship4.checkIfSunk(),
                       ship5.checkIfSunk(), ship6.checkIfSunk()]

    # Count1 keeps track of each true statement in the currentPlayerShips. If the list contains all 6 true statements, then it prints that the bot won and calls the end game method
    count1 = 0
    for ship in currentPlayerShips:
        if ship == True:
            count1 += 1
    if count1 == 6:
        print("All of your ships have sunk! The bot wins!")
        # Stop game function here
        endGame()

    # Count2 keeps track of each true statement in the currentBotShips. If the list contains all 6 true statements, then it prints that the player won and calls the end game method
    count2 = 0
    for ship in currentBotShips:
        if ship == True:
            count2 += 1
    if count2 == 6:
        print("All of the bot's ships have sunk! You win!")
        # Stop game function here
        endGame()


#   A   B   C   D   E   F   G   H   I   J
# 1  1A  1B  1C  1D  1E  1F  1G  1H  1I  1J
# 2  2A  2B  2C  2D  2E  2F  2G  2H  2I  2J
# 3  3A  3B  3C  3D  3E  3F  3G  3H  3I  3J
# 4  4A  4A  4C  4D  4E  4F  4G  4H  4I  4J
# 5  5A  5A  5C  5D  5E  5F  5G  5H  5I  5J
# 6  6A  6A  6C  6D  6E  6F  6G  6H  6I  6J
# 7  7A  7A  7C  7D  7E  7F  7G  7H  7I  7J
# 8  8A  8A  8C  8D  8E  8F  8G  8H  8I  8J
# 9  9A  9A  9C  9D  9E  9F  9G  9H  9I  9J
# 10 10A 10A 10C 10D 10E 10F 10G 10H 10I 10J


# Import photos
explosion = PhotoImage(file="explosion.png")
water = PhotoImage(file='water.png')
# Allows photos to be used in GUI label
my_explosion = Label(root, image=explosion)
my_water = Label(root, image=water)


# A def to place the explosion photo in the grid
def ExplosionImageCall():
    my_explosion.grid(row=15, column=15)
    if my_water.winfo_exists() == 1:
        my_water.grid_forget()
    else:
        pass


# A def to place the water photo in the grid
def WaterImageCall():
    my_water.grid(row=15, column=15)
    if my_explosion.winfo_exists() == 1:
        my_explosion.grid_forget()
    else:
        pass


# A def that will turn a button red on hit and calls the explosion photo
def Red_Button(button):
    button.configure(bg="red")  # bg=background
    button['state'] = DISABLED
    ExplosionImageCall()


# A def that will turn a button blue on miss and calls the water explosion photo
def Blue_Button(button):
    button.configure(bg="blue")
    button['state'] = DISABLED
    WaterImageCall()


# Class used to house all the buttons and locations for GUI
class ButtonLayout():

    def __init__(self, size):
        self.size = size

    def LetterRow(self):
        # Row one Labels
        letterHeadingA = Label(root, text="A", padx=self.size, pady=self.size)
        letterHeadingB = Label(root, text="B", padx=self.size, pady=self.size)
        letterHeadingC = Label(root, text="C", padx=self.size, pady=self.size)
        letterHeadingD = Label(root, text="D", padx=self.size, pady=self.size)
        letterHeadingE = Label(root, text="E", padx=self.size, pady=self.size)
        letterHeadingF = Label(root, text="F", padx=self.size, pady=self.size)
        letterHeadingG = Label(root, text="G", padx=self.size, pady=self.size)
        letterHeadingH = Label(root, text="H", padx=self.size, pady=self.size)
        letterHeadingI = Label(root, text="I", padx=self.size, pady=self.size)
        letterHeadingJ = Label(root, text="J", padx=self.size, pady=self.size)

        # Places Labels on a grid
        letterHeadingA.grid(row=1, column=2, padx=self.size, pady=self.size)
        letterHeadingB.grid(row=1, column=3, padx=self.size, pady=self.size)
        letterHeadingC.grid(row=1, column=4, padx=self.size, pady=self.size)
        letterHeadingD.grid(row=1, column=5, padx=self.size, pady=self.size)
        letterHeadingE.grid(row=1, column=6, padx=self.size, pady=self.size)
        letterHeadingF.grid(row=1, column=7, padx=self.size, pady=self.size)
        letterHeadingG.grid(row=1, column=8, padx=self.size, pady=self.size)
        letterHeadingH.grid(row=1, column=9, padx=self.size, pady=self.size)
        letterHeadingI.grid(row=1, column=10, padx=self.size, pady=self.size)
        letterHeadingJ.grid(row=1, column=11, padx=self.size, pady=self.size)

    def NumRow(self):
        # create first column Labels
        Number1 = Label(root, text="1", padx=self.size, pady=self.size)
        Number2 = Label(root, text="2", padx=self.size, pady=self.size)
        Number3 = Label(root, text="3", padx=self.size, pady=self.size)
        Number4 = Label(root, text="4", padx=self.size, pady=self.size)
        Number5 = Label(root, text="5", padx=self.size, pady=self.size)
        Number6 = Label(root, text="6", padx=self.size, pady=self.size)
        Number7 = Label(root, text="7", padx=self.size, pady=self.size)
        Number8 = Label(root, text="8", padx=self.size, pady=self.size)
        Number9 = Label(root, text="9", padx=self.size, pady=self.size)
        Number10 = Label(root, text="10", padx=self.size, pady=self.size)

        # number location column
        Number1.grid(row=2, column=1, padx=self.size, pady=self.size)
        Number2.grid(row=3, column=1, padx=self.size, pady=self.size)
        Number3.grid(row=4, column=1, padx=self.size, pady=self.size)
        Number4.grid(row=5, column=1, padx=self.size, pady=self.size)
        Number5.grid(row=6, column=1, padx=self.size, pady=self.size)
        Number6.grid(row=7, column=1, padx=self.size, pady=self.size)
        Number7.grid(row=8, column=1, padx=self.size, pady=self.size)
        Number8.grid(row=9, column=1, padx=self.size, pady=self.size)
        Number9.grid(row=10, column=1, padx=self.size, pady=self.size)
        Number10.grid(row=11, column=1, padx=self.size, pady=self.size)

    def B1uttonRow1(self):
        # Row 1 Buttons
        button1A = Button(root, text="1A", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button1A), botTurn(), checkSunkenShips(), checkWinner()])
        button1B = Button(root, text="1B", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button1B), botTurn(), checkSunkenShips(), checkWinner()])
        button1C = Button(root, text="1C", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button1C), botTurn(), checkSunkenShips(), checkWinner()])
        button1D = Button(root, text="1D", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button1D), botTurn(), checkSunkenShips(), checkWinner()])
        button1E = Button(root, text="1E", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button1E), botTurn(), checkSunkenShips(), checkWinner()])
        button1F = Button(root, text="1F", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button1F), botTurn(), checkSunkenShips(), checkWinner()])
        button1G = Button(root, text="1G", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button1G), botTurn(), checkSunkenShips(), checkWinner()])
        button1H = Button(root, text="1H", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button1H), botTurn(), checkSunkenShips(), checkWinner()])
        button1I = Button(root, text="1I", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button1I), botTurn(), checkSunkenShips(), checkWinner()])
        button1J = Button(root, text="1J", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button1J), botTurn(), checkSunkenShips(), checkWinner()])

        button1A.grid(row=2, column=2, padx=self.size, pady=self.size)
        button1B.grid(row=2, column=3, padx=self.size, pady=self.size)
        button1C.grid(row=2, column=4, padx=self.size, pady=self.size)
        button1D.grid(row=2, column=5, padx=self.size, pady=self.size)
        button1E.grid(row=2, column=6, padx=self.size, pady=self.size)
        button1F.grid(row=2, column=7, padx=self.size, pady=self.size)
        button1G.grid(row=2, column=8, padx=self.size, pady=self.size)
        button1H.grid(row=2, column=9, padx=self.size, pady=self.size)
        button1I.grid(row=2, column=10, padx=self.size, pady=self.size)
        button1J.grid(row=2, column=11, padx=self.size, pady=self.size)

    def B2uttonRow2(self):
        # Row 2 buttons
        button2A = Button(root, text="2A", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button2A), botTurn(), checkSunkenShips(), checkWinner()])
        button2B = Button(root, text="2B", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button2B), botTurn(), checkSunkenShips(), checkWinner()])
        button2C = Button(root, text="2C", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button2C), botTurn(), checkSunkenShips(), checkWinner()])
        button2D = Button(root, text="2D", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button2D), botTurn(), checkSunkenShips(), checkWinner()])
        button2E = Button(root, text="2E", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button2E), botTurn(), checkSunkenShips(), checkWinner()])
        button2F = Button(root, text="2F", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button2F), botTurn(), checkSunkenShips(), checkWinner()])
        button2G = Button(root, text="2G", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button2G), botTurn(), checkSunkenShips(), checkWinner()])
        button2H = Button(root, text="2H", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button2H), botTurn(), checkSunkenShips(), checkWinner()])
        button2I = Button(root, text="2I", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button2I), botTurn(), checkSunkenShips(), checkWinner()])
        button2J = Button(root, text="2J", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button2J), botTurn(), checkSunkenShips(), checkWinner()])

        button2A.grid(row=3, column=2, padx=self.size, pady=self.size)
        button2B.grid(row=3, column=3, padx=self.size, pady=self.size)
        button2C.grid(row=3, column=4, padx=self.size, pady=self.size)
        button2D.grid(row=3, column=5, padx=self.size, pady=self.size)
        button2E.grid(row=3, column=6, padx=self.size, pady=self.size)
        button2F.grid(row=3, column=7, padx=self.size, pady=self.size)
        button2G.grid(row=3, column=8, padx=self.size, pady=self.size)
        button2H.grid(row=3, column=9, padx=self.size, pady=self.size)
        button2I.grid(row=3, column=10, padx=self.size, pady=self.size)
        button2J.grid(row=3, column=11, padx=self.size, pady=self.size)

    def B3uttonRow3(self):
        # Row 3 buttons
        button3A = Button(root, text="3A", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button3A), botTurn(), checkSunkenShips(), checkWinner()])
        button3B = Button(root, text="3B", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button3B), botTurn(), checkSunkenShips(), checkWinner()])
        button3C = Button(root, text="3C", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button3C), botTurn(), checkSunkenShips(), checkWinner()])
        button3D = Button(root, text="3D", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button3D), botTurn(), checkSunkenShips(), checkWinner()])
        button3E = Button(root, text="3E", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button3E), botTurn(), checkSunkenShips(), checkWinner()])
        button3F = Button(root, text="3F", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button3F), botTurn(), checkSunkenShips(), checkWinner()])
        button3G = Button(root, text="3G", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button3G), botTurn(), checkSunkenShips(), checkWinner()])
        button3H = Button(root, text="3H", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button3H), botTurn(), checkSunkenShips(), checkWinner()])
        button3I = Button(root, text="3I", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button3I), botTurn(), checkSunkenShips(), checkWinner()])
        button3J = Button(root, text="3J", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button3J), botTurn(), checkSunkenShips(), checkWinner()])

        button3A.grid(row=4, column=2, padx=self.size, pady=self.size)
        button3B.grid(row=4, column=3, padx=self.size, pady=self.size)
        button3C.grid(row=4, column=4, padx=self.size, pady=self.size)
        button3D.grid(row=4, column=5, padx=self.size, pady=self.size)
        button3E.grid(row=4, column=6, padx=self.size, pady=self.size)
        button3F.grid(row=4, column=7, padx=self.size, pady=self.size)
        button3G.grid(row=4, column=8, padx=self.size, pady=self.size)
        button3H.grid(row=4, column=9, padx=self.size, pady=self.size)
        button3I.grid(row=4, column=10, padx=self.size, pady=self.size)
        button3J.grid(row=4, column=11, padx=self.size, pady=self.size)

    def B4uttonRow4(self):
        # Row 4 buttons
        button4A = Button(root, text="4A", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button4A), botTurn(), checkSunkenShips(), checkWinner()])
        button4B = Button(root, text="4B", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button4B), botTurn(), checkSunkenShips(), checkWinner()])
        button4C = Button(root, text="4C", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button4C), botTurn(), checkSunkenShips(), checkWinner()])
        button4D = Button(root, text="4D", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button4D), botTurn(), checkSunkenShips(), checkWinner()])
        button4E = Button(root, text="4E", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button4E), botTurn(), checkSunkenShips(), checkWinner()])
        button4F = Button(root, text="4F", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button4F), botTurn(), checkSunkenShips(), checkWinner()])
        button4G = Button(root, text="4G", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button4G), botTurn(), checkSunkenShips(), checkWinner()])
        button4H = Button(root, text="4H", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button4H), botTurn(), checkSunkenShips(), checkWinner()])
        button4I = Button(root, text="4I", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button4I), botTurn(), checkSunkenShips(), checkWinner()])
        button4J = Button(root, text="4J", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button4J), botTurn(), checkSunkenShips(), checkWinner()])

        button4A.grid(row=5, column=2, padx=self.size, pady=self.size)
        button4B.grid(row=5, column=3, padx=self.size, pady=self.size)
        button4C.grid(row=5, column=4, padx=self.size, pady=self.size)
        button4D.grid(row=5, column=5, padx=self.size, pady=self.size)
        button4E.grid(row=5, column=6, padx=self.size, pady=self.size)
        button4F.grid(row=5, column=7, padx=self.size, pady=self.size)
        button4G.grid(row=5, column=8, padx=self.size, pady=self.size)
        button4H.grid(row=5, column=9, padx=self.size, pady=self.size)
        button4I.grid(row=5, column=10, padx=self.size, pady=self.size)
        button4J.grid(row=5, column=11, padx=self.size, pady=self.size)

    def B5uttonRow5(self):
        # Row 5 buttons
        button5A = Button(root, text="5A", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button5A), botTurn(), checkSunkenShips(), checkWinner()])
        button5B = Button(root, text="5B", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button5B), botTurn(), checkSunkenShips(), checkWinner()])
        button5C = Button(root, text="5C", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button5C), botTurn(), checkSunkenShips(), checkWinner()])
        button5D = Button(root, text="5D", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button5D), botTurn(), checkSunkenShips(), checkWinner()])
        button5E = Button(root, text="5E", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button5E), botTurn(), checkSunkenShips(), checkWinner()])
        button5F = Button(root, text="5F", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button5F), botTurn(), checkSunkenShips(), checkWinner()])
        button5G = Button(root, text="5G", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button5G), botTurn(), checkSunkenShips(), checkWinner()])
        button5H = Button(root, text="5H", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button5H), botTurn(), checkSunkenShips(), checkWinner()])
        button5I = Button(root, text="5I", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button5I), botTurn(), checkSunkenShips(), checkWinner()])
        button5J = Button(root, text="5J", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button5J), botTurn(), checkSunkenShips(), checkWinner()])

        button5A.grid(row=6, column=2, padx=self.size, pady=self.size)
        button5B.grid(row=6, column=3, padx=self.size, pady=self.size)
        button5C.grid(row=6, column=4, padx=self.size, pady=self.size)
        button5D.grid(row=6, column=5, padx=self.size, pady=self.size)
        button5E.grid(row=6, column=6, padx=self.size, pady=self.size)
        button5F.grid(row=6, column=7, padx=self.size, pady=self.size)
        button5G.grid(row=6, column=8, padx=self.size, pady=self.size)
        button5H.grid(row=6, column=9, padx=self.size, pady=self.size)
        button5I.grid(row=6, column=10, padx=self.size, pady=self.size)
        button5J.grid(row=6, column=11, padx=self.size, pady=self.size)

    def B6uttonRow6(self):
        # Row 6 Buttons
        button6A = Button(root, text="6A", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button6A), botTurn(), checkSunkenShips(), checkWinner()])
        button6B = Button(root, text="6B", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button6B), botTurn(), checkSunkenShips(), checkWinner()])
        button6C = Button(root, text="6C", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button6C), botTurn(), checkSunkenShips(), checkWinner()])
        button6D = Button(root, text="6D", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button6D), botTurn(), checkSunkenShips(), checkWinner()])
        button6E = Button(root, text="6E", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button6E), botTurn(), checkSunkenShips(), checkWinner()])
        button6F = Button(root, text="6F", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button6F), botTurn(), checkSunkenShips(), checkWinner()])
        button6G = Button(root, text="6G", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button6G), botTurn(), checkSunkenShips(), checkWinner()])
        button6H = Button(root, text="6H", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button6H), botTurn(), checkSunkenShips(), checkWinner()])
        button6I = Button(root, text="6I", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button6I), botTurn(), checkSunkenShips(), checkWinner()])
        button6J = Button(root, text="6J", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button6J), botTurn(), checkSunkenShips(), checkWinner()])

        button6A.grid(row=7, column=2, padx=self.size, pady=self.size)
        button6B.grid(row=7, column=3, padx=self.size, pady=self.size)
        button6C.grid(row=7, column=4, padx=self.size, pady=self.size)
        button6D.grid(row=7, column=5, padx=self.size, pady=self.size)
        button6E.grid(row=7, column=6, padx=self.size, pady=self.size)
        button6F.grid(row=7, column=7, padx=self.size, pady=self.size)
        button6G.grid(row=7, column=8, padx=self.size, pady=self.size)
        button6H.grid(row=7, column=9, padx=self.size, pady=self.size)
        button6I.grid(row=7, column=10, padx=self.size, pady=self.size)
        button6J.grid(row=7, column=11, padx=self.size, pady=self.size)

    def B7uttonRow7(self):
        # Row 7 buttons
        button7A = Button(root, text="7A", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button7A), botTurn(), checkSunkenShips(), checkWinner()])
        button7B = Button(root, text="7B", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button7B), botTurn(), checkSunkenShips(), checkWinner()])
        button7C = Button(root, text="7C", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button7C), botTurn(), checkSunkenShips(), checkWinner()])
        button7D = Button(root, text="7D", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button7D), botTurn(), checkSunkenShips(), checkWinner()])
        button7E = Button(root, text="7E", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button7E), botTurn(), checkSunkenShips(), checkWinner()])
        button7F = Button(root, text="7F", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button7F), botTurn(), checkSunkenShips(), checkWinner()])
        button7G = Button(root, text="7G", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button7G), botTurn(), checkSunkenShips(), checkWinner()])
        button7H = Button(root, text="7H", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button7H), botTurn(), checkSunkenShips(), checkWinner()])
        button7I = Button(root, text="7I", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button7I), botTurn(), checkSunkenShips(), checkWinner()])
        button7J = Button(root, text="7J", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button7J), botTurn(), checkSunkenShips(), checkWinner()])

        button7A.grid(row=8, column=2, padx=self.size, pady=self.size)
        button7B.grid(row=8, column=3, padx=self.size, pady=self.size)
        button7C.grid(row=8, column=4, padx=self.size, pady=self.size)
        button7D.grid(row=8, column=5, padx=self.size, pady=self.size)
        button7E.grid(row=8, column=6, padx=self.size, pady=self.size)
        button7F.grid(row=8, column=7, padx=self.size, pady=self.size)
        button7G.grid(row=8, column=8, padx=self.size, pady=self.size)
        button7H.grid(row=8, column=9, padx=self.size, pady=self.size)
        button7I.grid(row=8, column=10, padx=self.size, pady=self.size)
        button7J.grid(row=8, column=11, padx=self.size, pady=self.size)

    def B8uttonRow8(self):
        # Row 8 Buttons
        button8A = Button(root, text="8A", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button8A), botTurn(), checkSunkenShips(), checkWinner()])
        button8B = Button(root, text="8B", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button8B), botTurn(), checkSunkenShips(), checkWinner()])
        button8C = Button(root, text="8C", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button8C), botTurn(), checkSunkenShips(), checkWinner()])
        button8D = Button(root, text="8D", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button8D), botTurn(), checkSunkenShips(), checkWinner()])
        button8E = Button(root, text="8E", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button8E), botTurn(), checkSunkenShips(), checkWinner()])
        button8F = Button(root, text="8F", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button8F), botTurn(), checkSunkenShips(), checkWinner()])
        button8G = Button(root, text="8G", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button8G), botTurn(), checkSunkenShips(), checkWinner()])
        button8H = Button(root, text="8H", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button8H), botTurn(), checkSunkenShips(), checkWinner()])
        button8I = Button(root, text="8I", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button8I), botTurn(), checkSunkenShips(), checkWinner()])
        button8J = Button(root, text="8J", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button8J), botTurn(), checkSunkenShips(), checkWinner()])

        button8A.grid(row=9, column=2, padx=self.size, pady=self.size)
        button8B.grid(row=9, column=3, padx=self.size, pady=self.size)
        button8C.grid(row=9, column=4, padx=self.size, pady=self.size)
        button8D.grid(row=9, column=5, padx=self.size, pady=self.size)
        button8E.grid(row=9, column=6, padx=self.size, pady=self.size)
        button8F.grid(row=9, column=7, padx=self.size, pady=self.size)
        button8G.grid(row=9, column=8, padx=self.size, pady=self.size)
        button8H.grid(row=9, column=9, padx=self.size, pady=self.size)
        button8I.grid(row=9, column=10, padx=self.size, pady=self.size)
        button8J.grid(row=9, column=11, padx=self.size, pady=self.size)

    def B9uttonRow9(self):
        # Row 9 button
        button9A = Button(root, text="9A", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button9A), botTurn(), checkSunkenShips(), checkWinner()])
        button9B = Button(root, text="9B", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button9B), botTurn(), checkSunkenShips(), checkWinner()])
        button9C = Button(root, text="9C", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button9C), botTurn(), checkSunkenShips(), checkWinner()])
        button9D = Button(root, text="9D", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button9D), botTurn(), checkSunkenShips(), checkWinner()])
        button9E = Button(root, text="9E", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button9E), botTurn(), checkSunkenShips(), checkWinner()])
        button9F = Button(root, text="9F", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button9F), botTurn(), checkSunkenShips(), checkWinner()])
        button9G = Button(root, text="9G", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button9G), botTurn(), checkSunkenShips(), checkWinner()])
        button9H = Button(root, text="9H", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button9H), botTurn(), checkSunkenShips(), checkWinner()])
        button9I = Button(root, text="9I", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button9I), botTurn(), checkSunkenShips(), checkWinner()])
        button9J = Button(root, text="9J", padx=self.size, pady=self.size,
                          command=lambda: [checkButtonPos(button9J), botTurn(), checkSunkenShips(), checkWinner()])

        button9A.grid(row=10, column=2, padx=self.size, pady=self.size)
        button9B.grid(row=10, column=3, padx=self.size, pady=self.size)
        button9C.grid(row=10, column=4, padx=self.size, pady=self.size)
        button9D.grid(row=10, column=5, padx=self.size, pady=self.size)
        button9E.grid(row=10, column=6, padx=self.size, pady=self.size)
        button9F.grid(row=10, column=7, padx=self.size, pady=self.size)
        button9G.grid(row=10, column=8, padx=self.size, pady=self.size)
        button9H.grid(row=10, column=9, padx=self.size, pady=self.size)
        button9I.grid(row=10, column=10, padx=self.size, pady=self.size)
        button9J.grid(row=10, column=11, padx=self.size, pady=self.size)

    def B10uttonRow10(self):
        # Row 10 buttons
        button10A = Button(root, text="10A", padx=self.size, pady=self.size,
                           command=lambda: [checkButtonPos(button10A), botTurn(), checkSunkenShips(), checkWinner()])
        button10B = Button(root, text="10B", padx=self.size, pady=self.size,
                           command=lambda: [checkButtonPos(button10B), botTurn(), checkSunkenShips(), checkWinner()])
        button10C = Button(root, text="10C", padx=self.size, pady=self.size,
                           command=lambda: [checkButtonPos(button10C), botTurn(), checkSunkenShips(), checkWinner()])
        button10D = Button(root, text="10D", padx=self.size, pady=self.size,
                           command=lambda: [checkButtonPos(button10D), botTurn(), checkSunkenShips(), checkWinner()])
        button10E = Button(root, text="10E", padx=self.size, pady=self.size,
                           command=lambda: [checkButtonPos(button10E), botTurn(), checkSunkenShips(), checkWinner()])
        button10F = Button(root, text="10F", padx=self.size, pady=self.size,
                           command=lambda: [checkButtonPos(button10F), botTurn(), checkSunkenShips(), checkWinner()])
        button10G = Button(root, text="10G", padx=self.size, pady=self.size,
                           command=lambda: [checkButtonPos(button10G), botTurn(), checkSunkenShips(), checkWinner()])
        button10H = Button(root, text="10H", padx=self.size, pady=self.size,
                           command=lambda: [checkButtonPos(button10H), botTurn(), checkSunkenShips(), checkWinner()])
        button10I = Button(root, text="10I", padx=self.size, pady=self.size,
                           command=lambda: [checkButtonPos(button10I), botTurn(), checkSunkenShips(), checkWinner()])
        button10J = Button(root, text="10J", padx=self.size, pady=self.size,
                           command=lambda: [checkButtonPos(button10J), botTurn(), checkSunkenShips(), checkWinner()])

        button10A.grid(row=11, column=2, padx=self.size, pady=self.size)
        button10B.grid(row=11, column=3, padx=self.size, pady=self.size)
        button10C.grid(row=11, column=4, padx=self.size, pady=self.size)
        button10D.grid(row=11, column=5, padx=self.size, pady=self.size)
        button10E.grid(row=11, column=6, padx=self.size, pady=self.size)
        button10F.grid(row=11, column=7, padx=self.size, pady=self.size)
        button10G.grid(row=11, column=8, padx=self.size, pady=self.size)
        button10H.grid(row=11, column=9, padx=self.size, pady=self.size)
        button10I.grid(row=11, column=10, padx=self.size, pady=self.size)
        button10J.grid(row=11, column=11, padx=self.size, pady=self.size)


# Ship class that contains all information for the ship objects
class Ships():
    # Creates the ships fields such as its type, the coordinates, the damage it has taken, if it has sunk, and the status. The status is whether it's controlled by a player or a bot
    def __init__(self, shipType, status, coordinates=[]):
        self.shipList = ["BattleShip", "Cruiser", "Destroyer", "Submarine", "Carrier", "Ptboat"]
        self.shipType = self.shipList[self.shipList.index(shipType)]
        self.coordinates = coordinates
        self.damage = 0
        self.sunk = False
        self.status = status

    # Battleships' length's determined by connon rules, added an extra ship "Destroyer".  This module returns number value of ships length based on the name of the ship.
    def getShipLength(self):
        if self.shipType == "BattleShip":
            return 4
        elif self.shipType == "Cruiser":
            return 3
        elif self.shipType == "Destroyer":
            return 4
        elif self.shipType == "Submarine":
            return 3
        elif self.shipType == "Carrier":
            return 5
        elif self.shipType == "Ptboat":
            return 2
        else:
            return 0
            # Battleship = 4 spots taken
        # Cruiser = 3 spots taken
        # Carrier = 5 spots taken
        # Destroyer = 4 spots taken
        # Submarine = 3 spots taken
        # Ptboat = 2 spots taken

    # This function sets the ship name to the parameter
    def setShipName(self, shipName):
        self.shipType = shipName

    # This function returns the ship name
    def getShipName(self):
        return self.shipType

    # This function sets the ship type to the parameter
    def setShip(self, shipType):
        self.shipType = shipType

    # This function returns the coordinates of the ship
    def getCoords(self):
        return self.coordinates

    # This function sets the ship's coordinataes to the parameter
    def setCoords(self, coordList):
        self.coordinates = coordList

    # This function adds 1 damage to the ship
    def addDamage(self, damage):
        self.damage += damage

    # This function checks whether the ship has sunk or not
    def checkIfSunk(self):
        # If the ships damage is equal to it's length, then it has been sunk
        if self.damage == self.getShipLength():
            self.sunk = True
            return self.sunk
        else:
            return self.sunk

    # This function returns the status of the ship
    def getStatus(self):
        return self.status

    # This function is the string function for the ship
    def __str__(self):
        return self.shipType


# This function checks the position and coordinates of a button
def checkButtonPos(button):
    # Get a coordinate, ex: 9C, from the button's text
    coords = button.cget('text')
    # Passes the coordinate through the checkButtonShips method
    if checkButtonShips(coords):
        # If the function finds that the coordinate is equal to one of the ship's coordinates then it calls the Red_Button method for that button
        Red_Button(button)
    else:
        # If the coordinate is not one of the ship's coordinates then it calls the Blue_Button function
        Blue_Button(button)


# Creates Bot Ship Objects (1-6)
ship1 = Ships("BattleShip", "bot")
ship2 = Ships("Cruiser", "bot")
ship3 = Ships("Destroyer", "bot")
ship4 = Ships("Submarine", "bot")
ship5 = Ships("Carrier", "bot")
ship6 = Ships("Ptboat", "bot")
# Creates Human Player Ship Objects (7-12)
ship7 = Ships("BattleShip", "player")
ship8 = Ships("Cruiser", "player")
ship9 = Ships("Destroyer", "player")
ship10 = Ships("Submarine", "player")
ship11 = Ships("Carrier", "player")
ship12 = Ships("Ptboat", "player")

# Creates button layout object
grid = ButtonLayout(5)  # number(5) changes the size of buttons in GUI
# Calls Methods from ButtonLayout class
grid.LetterRow()
grid.NumRow()
grid.B1uttonRow1()
grid.B2uttonRow2()
grid.B3uttonRow3()
grid.B4uttonRow4()
grid.B5uttonRow5()
grid.B6uttonRow6()
grid.B7uttonRow7()
grid.B8uttonRow8()
grid.B9uttonRow9()
grid.B10uttonRow10()

# Calls startGame function to initiate rules for Battleship, assigns coordinates to global ship objects and prints out player's ships
startGame()

# ----------------------------------

root.mainloop()

