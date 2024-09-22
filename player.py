"""
All player variables and functions are stored here.
Most global variables can be added to the Player class.
"""
class Player:
    def __init__(self, name, description, current_room, max_mass, current_mass) -> None:
        self.name = name
        self.description = description
        self.current_room = current_room
        self.max_mass = max_mass
        self.current_mass = current_mass
        self.inventory = []
        self.health = 100
        self.alive = True
        self.antidote = 0
    
    def take_item(self, item):
        if item.mass + self.current_mass <= self.max_mass:
            self.inventory.append(item.id)
            self.current_mass += item.mass
            return True
        else:
            return False
    
    def drop_item(self, item):
        self.inventory.remove(item.id)
        self.current_mass -= item.mass
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False
        return self.alive
    
    def use_antidote(self):
        print("You use the antidote and feel much better.")
        self.antidote = 1
        pass # add code for extending game timer here

    def __str__(self) -> str:
        return f"{self.name}\n{self.current_room}\nCarrying: {self.inventory}\nHealth: {self.health}\nAlive: {self.alive}"

player_kwargs = {
    "name": "Professor Kirill's Wayward Student", 
    "description": "You.", 
    "current_room": None,
    "max_mass": 3,
    "current_mass": 0
}

player = Player(**player_kwargs)