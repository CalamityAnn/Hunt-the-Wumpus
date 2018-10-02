from classes import *
import time
from tkinter import *


introPhrases = ["Welcome to Hunt the Wumpus!", "This was originally a very early game, designed and written by Gregory Yob in 1975.", "This version was written by Cameron Skubik-Peplaski, and features a few changes.", "Firstly, it's written in Python. Second, the map is different. Third, it has a couple new obstacles. These will be explained soon.", "The goal of the game is to find and kill the Wumpus, which is somewhere in its lair.", "You will be able to move through the lair and shoot arrows at the wumpus.", "If you hit it, you win. If you miss, the wumpus will startle and move one room.", "\nHere, the lair consists of a 5 by 4 rectangular map.", "The map will be shown on game start.", "The lair contains 4 kinds of obstacles besides the wumpus itself.", "The Wumpus and the Pitfalls will kill the player if encountered.", "Superbats will place the player in a random unoccupied room.", "The ice room will slide the player to the next room over.", "The cockroaches will scatter (leaving the map) and startle the wumpus when encountered.", "Each of these obstacles has a hint dialogue when the player is in a room next to them.", "They are as follows;", " Wumpus: I can smell the beast!\n Superbat: I can hear flapping.\n Pitfall: I can feel a breeze. \n Ice Room: It's a bit chilly in here. \n Cockroaches: I hear chittering.", "The ice room and cockroaches are optional, and will only be added if you decide to.", "\nThe map will display once generation is complete, but you will have to close it in order to continue with the game. \nIt will show you the grid and your starting position, but take a screenshot if you want to use it as a reference."]

for n in introPhrases:
    print(n)
    time.sleep(4)

input("\nPlease press enter to continue when you are ready.")

again = 0

while again is 0:
    print("Starting...")
    top = Tk(None, None, "hunt the wumpus")
    bkg = PhotoImage(file="assets/cave.gif")
    height, width = bkg.height(), bkg.width()
    
    map = Map(top, height, width)
    print("Generating map...")
    print("You will need to close out of the map to continue.")
    time.sleep(2)
    map.generate()
    
    win = 2
    round = 1
    action = ""
    
    print("\n\nYou have reached the cave of the dreaded Wumpus...")
    while win not in [-1, 1]:
        map.checkLocation()
        while action is not "m" and action is not "s":
            if round is 1:
                print('What will you do? Move (enter "m")? Shoot (enter "s")?')
            else:
                print('What will you do? Move? Shoot?')
            
            action = input("  => ")
        
        if action is "m":
            map.move()
        elif action is "s":
            map.shoot()
        
        win = map.checkCondition()
        action = ""
        round += 1
    
    if win is 1:
        print("You've killed the Wumpus! Hurrah!", "\nYou've won!")
    elif win is -1:
        print("You've either died or been killed. Poor you.", "\n You've lost.")
       
    choice = "x"
    while choice is not "y" and choice is not "n":
        print("Game Over! Would you like to play again? Enter y for yes, n for no.")
        choice = input("  => ")
        
    if choice is "n":
        again = 1
