import random
from tkinter import *
random.seed(None)


def findIn(n, s):
    """Takes a list n and returns the index of s, if it exists; returns -1 if not"""
    for k in range(n):
        if n[k] is s:
            return k
        
    return -1


class Room(object):
    """A Room is one of the squares on the map"""
    
    def __init__(self, name):
        """Create a Room with given name and exit.
        
        Name: A string, name of the room.
        """
        self.name = name
        self.entity = None
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        
    def add_entity(self, entity):
        """Adds an entity to a Room.
        
        If a player is added to a room with an obstacle, it will call the action of that obstacle.
        """
        if self.entity is None:
            if entity.room is not None:
                entity.room.entity = None
            entity.room = self
            self.entity = entity
        else:
            if isinstance(entity, Player):
                if self.entity.is_obstacle:
                    self.entity.action()
                
    def __str__(self):
        return self.name
             
                
class Entity(object):
    """An Entity is the base class for the player and all obstacles."""
    
    is_obstacle = False
    
    def __init__(self, room=None, gameMap=None):
        """Create entity with starting place and map."""
        self.room = room
        self.gameMap = gameMap
        
    def action(self):
        """Action performed when entity is activated."""

    # modeled after code from ants.py in hw4
    def __repr__(self):
        cname = type(self).__name__
        return '{0} in room {1}'.format(cname, self.room)
    

class Player(Entity):
    """This is the player"""
    dead = False
    direction = None
    
    def move(self):
        options = {'up': 1, 'left': 2, 'down': 3, 'right': 4}
        moved = False

        while moved is False:
            choice = ""
            while True:
                choice = input('Please enter "up" to go up, "down" to go down, "left" to go left, or "right" to go right. \n  => ')
                if choice not in ('up', 'down', 'left', 'right'):
                    print('That is not a valid direction.')
                    continue
                else:
                    break
                    
            moveSide = options[choice]
    
            if moveSide is 1:
                if self.room.up is not None:
                    moved = True
                    self.direction = "up"
                    self.room.up.add_entity(self)
                else:
                    print('That room doesn\'t exist, please choose again.')
            elif moveSide is 2:
                if self.room.left is not None:
                    moved = True
                    self.direction = "left"
                    self.room.left.add_entity(self)
                else:
                    print('That room doesn\'t exist, please choose again.')
            elif moveSide is 3:
                if self.room.down is not None:
                    moved = True
                    self.direction = "down"
                    self.room.down.add_entity(self)
                else:
                    print('That room doesn\'t exist, please choose again.')
            elif moveSide is 4:
                if self.room.right is not None:
                    moved = True
                    self.direction = "right"
                    self.room.right.add_entity(self)
                else:
                    print('That room doesn\'t exist, please choose again.')
            else:
                print('That is not a valid choice, please choose again.')
                
    def shoot(self):
        options = {'up': 1, 'left': 2, 'down': 3, 'right': 4}
        shot = False
        hit = False
    
        while shot is False:
            choice = ""
            while True:
                choice = input('Please enter "up" to shoot up, "down" to shoot down, "left" to shoot left, or "right" to shoot right. \n  => ')
                if choice not in ('up', 'down', 'left', 'right'):
                    print('That is not a valid direction.')
                    continue
                else:
                    break
                
            shootSide = options[choice]
            currRoom = self.room
        
            if shootSide is 1:
                if self.room.up is not None:
                    shot = True
                    currRoom = currRoom.up
                    
                    for n in range(3):
                        if isinstance(currRoom.entity, Wumpus):
                            self.gameMap.wumpus.dead = True
                            hit = True
                            break
                        
                        if currRoom.up is not None:
                            currRoom = currRoom.up
                        else:
                            break
                else:
                    print('That room doesn\'t exist, please choose again.')
                    
            elif shootSide is 2:
                if self.room.left is not None:
                    shot = True
                    currRoom = currRoom.left
                    
                    for n in range(3):
                        if isinstance(currRoom.entity, Wumpus):
                            self.gameMap.wumpus.dead = True
                            hit = True
                            break
                        
                        if currRoom.left is not None:
                            currRoom = currRoom.left
                        else:
                            break
                else:
                    print('That room doesn\'t exist, please choose again.')
                    
            elif shootSide is 3:
                if self.room.down is not None:
                    shot = True
                    currRoom = currRoom.down
                    
                    for n in range(3):
                        if isinstance(currRoom.entity, Wumpus):
                            self.gameMap.wumpus.dead = True
                            hit = True
                            break
                        
                        if currRoom.down is not None:
                            currRoom = currRoom.down
                        else:
                            break
                else:
                    print('That room doesn\'t exist, please choose again.')
                    
            elif shootSide is 4:
                if self.room.right is not None:
                    shot = True
                    currRoom = currRoom.right
                    
                    for n in range(3):
                        if isinstance(currRoom.entity, Wumpus):
                            self.gameMap.wumpus.dead = True
                            hit = True
                            break
                        
                        if currRoom.right is not None:
                            currRoom = currRoom.right
                        else:
                            break
                else:
                    print('That room doesn\'t exist, please choose again.')
                    
            else:
                print('That is not a valid choice, please choose again.\n')

        if not hit:
            print('You missed, and the sound startled the wumpus!\n')
            self.gameMap.wumpus.startle()


class Obstacle(Entity):
    """An obstacle is the base class for all specific obstacles."""
    
    is_obstacle = True
    
    def giveClue(self):
        """Prints out a clue when player is adjacent to obstacle, called from map"""
        
    
class Wumpus(Obstacle):
    """The Wumpus itself.
    
    If the player encounters it, they will die.
    """
    dead = False
    
    def startle(self):
        currRoom = self.room
        
        # moving when startled, 1 is up, 2 is left, 3 is down, 4 is right
        while self.room is currRoom:
            moveSide = random.randint(1, 5)
            
            if moveSide is 1:
                if self.room.up is not None:
                    self.room.up.add_entity(self)
            elif moveSide is 2:
                if self.room.left is not None:
                    self.room.left.add_entity(self)
            elif moveSide is 3:
                if self.room.down is not None:
                    self.room.down.add_entity(self)
            elif moveSide is 4:
                if self.room.right is not None:
                    self.room.right.add_entity(self)
    
    def action(self):
        print('You have stumbled into the wumpus itself!')
        self.gameMap.player.dead = True
    
    def giveClue(self):
        print("I can smell the beast!")
    
    
class SuperBat(Obstacle):
    """There are 2 super bats per map.
    
    If the player encounters them, the player is dropped into a random room.
    """
    
    def action(self):
        print('You were carried off by bats!')
        spot = random.randint(1, 20)
        while self.gameMap.rooms[spot].entity is not None:
            spot = random.randint(1, 20)
        
        self.gameMap.rooms[spot].add_entity(self.gameMap.player)
        self.gameMap.player.moved = True
    
    def giveClue(self):
        print("I can hear flapping.")
    
    
class PitFall(Obstacle):
    """There are 2 pitfalls per map.
    
    If the player encounters one, they will die.
    """
    
    def action(self):
        print('You have fallen into an endless pit.')
        self.gameMap.player.dead = True
    
    def giveClue(self):
        print('I can feel a breeze.')
    
    
class IceRoom(Obstacle):
    """There is 1 ice room per map.
    
    If the player encounters this, they will be forced into the room across from the one they entered from, if possible.
    """
    
    def action(self):
        print('You slipped on the ice, headed straight for the next room!')
        oldRoom = self.gameMap.player.room
        ways = self.gameMap.player.direction
        
        if ways is "up":
            if self.room.up is not None:
                self.room.up.add_entity(self.gameMap.player)
        elif ways is "left":
            if self.room.left is not None:
                self.room.left.add_entity(self.gameMap.player)
        elif ways is "down":
            if self.room.down is not None:
                self.room.down.add_entity(self.gameMap.player)
        elif ways is "right":
            if self.room.right is not None:
                self.room.right.add_entity(self.gameMap.player)
                
        if self.gameMap.player.room is oldRoom:
            print('You hit the wall of the room, you remain here')
            
        self.gameMap.player.moved = True
    
    def giveClue(self):
        print("It's a bit chilly in here.")

    
class Roaches(Obstacle):
    """There are two roach rooms per map.
    
    If the player encounters one, the roaches will scuttle away and startle the Wumpus, causing it to move 1 room.
    """
    
    def action(self):
        print("The roaches' chittering as they flee from you has startled the wumpus!\n")
        self.gameMap.wumpus.startle()
        self.gameMap.player.room.entity = None
        self.gameMap.player.room = self.room
        self.room.entity = self.gameMap.player
    
    def giveClue(self):
        print("I hear chittering.")


class Map(object):
    """A Map is the map itself.
    It contains:
        - a dictionary of all rooms
        - the player object
        - all obstacle objects
        - functions to check for adjacent obstacles and check end conditions
    """
    tkObj = None
    canvas = None
    rooms = {}
    roomPadding = 137
    
    def __init__(self, tk, height=1000, width=10000):
        self.tkObj = tk
        self.height = height
        self.width = width

        self.player = Player(None, self)
        self.wumpus = Wumpus(None, self)
        self.bats = [SuperBat(None, self), SuperBat(None, self)]
        self.pits = [PitFall(None, self), PitFall(None, self)]
        self.ice = IceRoom(None, self)
        self.roaches = [Roaches(None, self), Roaches(None, self)]
        self.entities = [self.player, self.wumpus, self.bats[0], self.bats[1], self.pits[0], self.pits[1], self.ice, self.roaches[0], self.roaches[1]]
        
    def move(self):
        self.player.move()

    def shoot(self):
        self.player.shoot()

    def move_player(self, x_move, y_move):
        self.canvas.move(self.play, x_move, y_move)

    def generate(self):
        """Generates the map by creating rooms and attaching them to those around them."""
        self.canvas = Canvas(self.tkObj, height=self.height, width=self.width)

        bkg = PhotoImage(file="assets/cave.gif")
        ply = PhotoImage(file="assets/Player.gif")

        self.canvas.pack(expand=1, fill=BOTH)
        self.backing = self.canvas.create_image(0, 0, anchor=NW, image=bkg)
        self.play = self.canvas.create_image(85, 70, anchor=NW, image=ply)
        
        for n in range(1, 21):
            self.rooms[n] = Room("Room " + str(n))
            
            # after top row, set ups
            # use items below others to set up item's down
            if n > 5:
                self.rooms[n].up = self.rooms[n - 5]
                self.rooms[n - 5].down = self.rooms[n]
            
            # no very left items should have a left room
            # use items to right to set left item's right value
            if n % 5 != 1:
                self.rooms[n].left = self.rooms[n - 1]
                self.rooms[n - 1].right = self.rooms[n]
            
        # entity placement
        # player first, so anything else can't spawn on top
        spot = random.randint(1, 20)
        self.rooms[spot].add_entity(self.player)
        temp = spot
        xShift = 0
        yShift = 0
        while temp > 5:
            yShift += 1
            temp -= 5
            
        while temp > 1:
            xShift += 1
            temp -= 1
            
        self.move_player(self.roomPadding * xShift, self.roomPadding * yShift)
        
        spot = random.randint(1, 20)
        while self.rooms[spot].entity is not None:
            spot = random.randint(1, 20)
        self.rooms[spot].add_entity(self.wumpus)

        spot = random.randint(1, 20)
        while self.rooms[spot].entity is not None:
            spot = random.randint(1, 20)
        self.rooms[spot].add_entity(self.bats[0])

        spot = random.randint(1, 20)
        while self.rooms[spot].entity is not None:
            spot = random.randint(1, 20)
        self.rooms[spot].add_entity(self.bats[1])

        spot = random.randint(1, 20)
        while self.rooms[spot].entity is not None:
            spot = random.randint(1, 20)
        self.rooms[spot].add_entity(self.pits[0])

        spot = random.randint(1, 20)
        while self.rooms[spot].entity is not None:
            spot = random.randint(1, 20)
        self.rooms[spot].add_entity(self.pits[1])

        choice = "x"
        while choice is not "y" and choice is not "n":
            choice = input('Please enter y to add the Ice and Roach rooms, or n to continue without.\n  => ')

        if choice is "y":
            spot = random.randint(1, 20)
            while self.rooms[spot].entity is not None:
                spot = random.randint(1, 20)
            self.rooms[spot].add_entity(self.ice)
    
            spot = random.randint(1, 20)
            while self.rooms[spot].entity is not None:
                spot = random.randint(1, 20)
            self.rooms[spot].add_entity(self.roaches[0])
    
            spot = random.randint(1, 20)
            while self.rooms[spot].entity is not None:
                spot = random.randint(1, 20)
            self.rooms[spot].add_entity(self.roaches[1])

        print("Displaying map...", "\n (The window may be hidden behind your active window.)")
        self.tkObj.mainloop()

    def checkLocation(self):
        """Outputs any clues that are around the player"""
        checked = self.player.room
        
        if checked.up is not None:
            if checked.up.entity is not None:
                checked.up.entity.giveClue()
                
        if checked.left is not None:
            if checked.left.entity is not None:
                checked.left.entity.giveClue()
                
        if checked.down is not None:
            if checked.down.entity is not None:
                checked.down.entity.giveClue()
        
        if checked.right is not None:
            if checked.right.entity is not None:
                checked.right.entity.giveClue()
    
    def checkCondition(self):
        if self.player.dead:
            return -1
        elif self.wumpus.dead:
            return 1
        else:
            return 0
