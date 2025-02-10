# Post apocalyptic zombie game

# Class Player defines players.
class Player:
    def __init__(self, name, max_health, health, dead):
        self.name = name
        self.max_health = 100
        self.health = 100
        self.is_dead = False

    def __repr__(self):
        # Printing player will tell you it's name, and how much health is remaining.
        return "Player name is {name}. {name} has {health} life points until death.".format(name = self.name, health =
                                                                                            self.health)

    def gain_health(self, amount):
        # Using a first aid item will add 10 points to player's health.  First aid items are limited so use wisely.
        self.is_dead = False
        if self.health > 0:
            self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print("{name} received 10 life points to health.".format(name = self.name))

    def dead(self):
        self.is_dead = True
        print("{name} is dead!".format(name = self.name))
        sys.exit()



    def lose_health(self, amount):
        self.health -= amount
        if self.health == 0:
            self.dead()




class Enemies:
    def __init__(self, type, max_health, health, strength, dead):
        self.type = type
        self.max_health = 100
        self.health = 100
        self.strength = strength
        self.is_dead = False



# Class Items defines items
class Items:
    def __init__(self, Glock, Shotgun, first_aid, key):
        self.Glock = pistol
        self.Shotgun = shotgun
        self.first_aid = 10
        self.has_key = False
