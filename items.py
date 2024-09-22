"""
TO ADD AN ITEM:

Create a dictionary for it
Make sure the dictionary contains every key required by the type of class that it is
Copy format for instancing room in the rooms dictionary, use ** to unpack the dictionary

TO EDIT AN ITEM:

Edit the dictionary for it
If you need to add a new variable, make sure you add it to the dictionary and the __init__ function
If variable is only used for one item, add the default case to the __init__ function line 16 (looks like this: variable=None)

"""
from map import rooms

class Item:
    def __init__(self, name, description, item_id,  mass, file_name=None):
        self.name = name
        self.description = description
        self.id = item_id
        self.mass = mass
        self.file_name = file_name

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description
    
    def getFileName(self):
        return self.file_name
    
    def __str__(self):
        return self.name


class Weapon(Item):
    def __init__(self, name, description, item_id, mass, damage, uses, file_name=None):
        super().__init__(name, description, item_id, mass)
        self.damage = damage
        self.uses = uses

    def getDamage(self):
        return self.damage

    def setDamage(self, damage):
        self.damage=damage

class Key(Item):
    def __init__(self, name, description, item_id, mass, room_to_unlock, file_name=None):
        super().__init__(name, description, item_id, mass)
        self.room_to_unlock = room_to_unlock

    def use(self):
        print(self.name + " has been used.")
        self.room_to_unlock.unlock()

class Herb(Item):
    def __init__(self, name, description, item_id, mass, file_name=None):
        super().__init__(name, description, item_id, mass)

    def add(self, player):
        if player.current_room == "room_lab":
            lab = rooms["room_lab"]
            if len(lab.items) < 3:
                lab.items.append(self.id)
                player.inventory.remove(self.id)
                print(f"You have added {self.name} to the concoction")
            else:
                print("The cauldron is full, you cannot add any more ingredients")
            if len(lab.items) == 3:
                print("You have added all the ingredients to the concoction")
                if "item_tulips" in lab.items and "item_daffodils" in lab.items and "item_iris" in lab.items:
                    player.use_antidote()
                    print("You have created the antidote")
                    lab.items = []
                    # trigger boss fight here
                elif "item_buttercups" in lab.items and "item_daisys" in lab.items and "item_roses" in lab.items:
                    player.add_item(items["item_poison"])
                    print("You have created a strong poison")
                    lab.items = []
                else:
                    print("The concoction is not right, the cauldron boils over leaving a thick goopy ash in its wake.")
                    print("It seems to worsen the effects of the poison.")
                    print("you begin to suffocate you, you have died.")
                    player.health = 0
                    player.alive = False


class Healing(Item):
    def __init__(self, name, description, item_id, mass, healing, file_name=None):
        super().__init__(name, description, item_id, mass)
        self.healing = healing
    
    def heal(self, player):
        if player.health == 100:
            print("You are already at full health")
            return False
        player.health += self.healing
        if player.health > 100:
            player.health = 100
        if self.id in player.inventory:
            player.inventory.remove(self.id)
        print(f"You have healed yourself by {self.healing} points")
        print("Your health is now " + str(player.health))
        print(f"The {self.name} was lost in the process")
        return True
    
class Note(Item):
    def __init__(self, name, description, item_id, mass, file_name=None):
        super().__init__(name, description, item_id, mass)
        self.description = description
        self.file_name = file_name
    
    def read(self):
        print(f"You read the {self.name}\n")
        print(self.description)

item_laptop = {

    "name": "Laptop",

    "mass": 1.5,

    "description":
    "It has seen better days. At least it has a WiFi card!",

    "item_id": "item_laptop",
    "file_name":"laptop"
}

item_letter = {
    
    "name": "Letter",

    "mass": 0.05,

    "description": """
    It is the letter you recieved from Kirril. \n
    it says: \n
    "Dear Visitor,\n\
        I am working on a great project, one sure to bring glory to the Kingdom.\n\
        You are aware of the recent food shortages, yes? The price of guano has\n\
        drastically risen in recent times, and with it, so has the price of food.\n\
        The King cannot simply order lower prices, as the loss of earning would\n\
        render farmers too poor to order more guano. Subsidising the guano\n\
        purchases is not feasible either, not with these prices. Fortunately, I\n\
        believe I have come up with an alternative to guano, one that would\n\
        revolutionise agriculture. Come to my manor, I am sure you would appreciate\n\
        my work.\n\
        \n\
        Yours sincerely,\n\
        Professor Kirill.\n"
        """,
        
    "item_id": "item_letter",
    "file_name":"note"
}


item_mysteriousnote = {
    
    "name": "Mysterious Note",

    "mass": 0.05,

    "description": 
    """
    It is a note you found in the basement bedroom. \n
    It says:
    □︎◻︎♏︎■︎ ⧫︎♒︎♏︎ ⬧︎♒︎♏︎♎︎ ⧫︎□︎ ♐︎♓︎■︎♎︎ ⧫︎♒︎♏︎ ♑︎♋︎●︎●︎♏︎❒︎⍓︎ 🙵♏︎⍓︎📬︎ \n
    ♓︎■︎ ⧫︎♒︎♏︎ ♑︎♋︎●︎●︎♏︎❒︎⍓︎📪︎ ♏︎❖︎♏︎❒︎⍓︎⧫︎♒︎♓︎■︎♑︎ ⬥︎♓︎●︎●︎ ♌︎♏︎ ⬧︎♋︎♓︎♎︎ \n
    You probably need to translate this to English. Perhaps there \n
    is something somewhere to help you.
    """,

    "item_id": "item_mysteriousnote",
    "file_name":"note"
}

item_controller = {
    
    "name": "Controller",

    "mass": 0.4,

    "description": """
    A TV controller for the TV in the conservatory \n
    It doesn't seem to work.
    """,

    "item_id": "item_controller",

    "damage": 10,

    "uses": 1,
    "file_name":None
}

item_brick = {
    
    "name": "Brick",

    "mass": 1.15,

    "description": """
    A brick you found in the conservatory. \n
    Might come in useful if you have to fight anyone here.
    """,

    "item_id": "item_brick",

    "damage": 20,

    "uses": 1,
    "file_name":None
}

item_crisps = {
    
    "name": "Packet of Crisps",

    "mass": 0.1,

    "description": "A packet of crisps. May be handly if you become hungry",

    "item_id": "item_crisps",
    "file_name":None

}

item_woodblocks = {
    
    "name": "Wood Block",

    "mass": 2,

    "description": """
    A bunch of wood blocks. Might be useful if 
    you want to start a fire.
    """,

    "item_id": "item_woodblocks",

    "damage": 15,

    "uses": 1,
    "file_name":None
}

item_kitchennote = {
    
    "name": "Kitchen Note",

    "mass": 0.05,

    "description": """
    A note you found in the kitchen. \n
    It says: \n
    Please, go to the flower bed, it was \n
    the only place I could place the note without \n
    getting caught
    """,

    "item_id": "item_kitchennote",
    "file_name":"note"
}

item_flowers = {
    
    "name": "Flowers",

    "mass": 0.5,

    "description": "500g of flowers. Might be good for neutralising poison",

    "item_id": "item_flowers",
    "file_name":"ascii-flower"
}

item_glass = {
    
    "name": "Shattered Glass",

    "mass": 0.2,

    "description": "Broken glass. May come handy in a fight",

    "item_id": "item_shatteredglass",

    "damage": 30,

    "uses": 1,

    "file_name":None
}

item_bloodsample = {
    
    "name": "Blood sample",

    "mass": 0.4,

    "description": """
    A sample of blood. You have no idea why this is here \n
    and how it got here.
    """,

    "item_id": "item_blood",
    "file_name":None
}

item_flowerbednote = {
    
    "name": "Flower Bed Note",

    "mass": 0.05,

    "description": """
    A note you found in the flower bed. \n
    It says: The basement bedroom contains a secret. \n
    You should probably follow what is says. \n
    """,


    "item_id": "item_flowerbednote",
    "file_name":None
}

item_book = {
    
    "name": "Book",

    "mass": 0.1,

    "description": """
    A book made by Kirril. It seems to have translations \n
    from wingdings to English.
    It reads:
    a = ♋︎ b = ♌︎ d = ♎︎ e = ♏︎ f = ♐︎ g = ♑︎ h = ♒︎ i = ♓︎ k = & \n
    l = ●︎ n = ■︎ o = □︎ p = ◻︎ r = ❒︎ s = ⬧︎ t = ⧫︎ v = ❖︎ w = ⬥︎ y = ⍓︎
    """,

    "item_id": "item_book",
    "file_name":"book-art"
}

item_victimnote = {
    
    "name": "Victim Note",

    "mass": 0.05,

    "description": """
    A note from one of the victims. It reads: \n
    There were no murders. The poison, it must be stopped \n
    at all costs. 
    """,

    "item_id": "item_victimnote",
    "file_name":"note"
}


item_gallerynote = {
    
    "name": "Gallery Note",

    "mass": 0.05,

    "description": """
    A note you found in the gallery - made by Christoper Wallbridge. \n
    It reads: \n
    This note explains everything about what has happened. \n
    The royal scientist, Kirill Sidorov, has created this awful \n
    poison which kills anyone in the mansion in 45 minutes. As his \n
    assistant, I was scared to do anything, so I did not stop the posion. \n
    If you are reading this note, you have the ability to stop this. \n
    There is a cure to the poison, but \n
    you have limited time before the posion kills you. Combine tulips, \n
    daffodils and iris from the flower bed to stop the poison, located \n
    in the labatory in the basement. You can stop these \n
    killings for good. \n
    However, Kirill will be alerted as soon as you stop the posion, so \n
    you will have to defeat him.
    """,

    "item_id": "item_gallerynote",
    "file_name":"note"
}

item_gardenkey  = {

    "name": "Garden Key",

    "description": "A key to the garden. Can be accessed through the Conservatory",

    "mass": 0,

    "item_id": "item_gardenkey",

    "room_to_unlock": "room_gardenarea",
    "file_name":"keys"
}

item_labkey = {

    "name": "Lab Key",

    "description": "A key to the lab in the basement",

    "mass": 0,

    "item_id": "item_labkey",

    "room_to_unlock": "room_labs",
    "file_name":"keys"
}

item_shedkey = {

    "name": "Shed Key",

    "description": "A key to the shed in the garden.",

    "mass": 0,

    "item_id": "item_shedkey",

    "room_to_unlock": "room_shed",
    "file_name":"keys"

}

item_gallerykey = {

    "name": "Gallery Key",

    "description": "A key to the gallery on the first floor",

    "mass": 0,

    "item_id": "item_gallerykey",

    "room_to_unlock": "room_gallery",

    "file_name":"keys"
}

item_lemonade = {

    "name" : "Lemonade Bottle",

    "description" : "Lemonade. Good to mix with Vodka.",

    "mass": 0.2,

    "item_id": "item_lemonade",

    "healing" : 25,

    "file_name":None

}

item_apples = {

    "name": "Apples",

    "description": "Pink Lady Apples. They taste awful.",

    "mass": 0.2,

    "item_id": "item_apples",

    "healing": 10,
    "file_name":None
}

item_icecream = {

    "name": "Ice Cream",

    "description": "Ice Cream. Everyone likes ice cream",

    "mass": 0.05,

    "item_id": "item_icecream",

    "healing": 35,
    "file_name":None
}


item_pork = {

    "name": "Porkchop",

    "description": "Frozen pork. Somehow edible.",

    "mass": 0.1,

    "item_id": "item_pork",

    "healing" : 50,
    "file_name":None
}

item_knife = {

    "name": "Knife",

    "description": "A knife. Will come in useful if you need to fight anyone.",

    "mass" : 0.2,

    "item_id": "item_knife",

    "damage": 35,

    "uses": 10,
    "file_name":None
}

item_pan = {

    "name": "Pan",

    "description": "A pan. You can cook with this, but you dont have any oil.",

    "mass": 0.5,

    "item_id": "item_pan",

    "damage": 20,

    "file_name":None,
    
    "uses": 2
}

item_iris = {

    "name": "Iris",

    "description": "Iris flowers. Good for herbs!",

    "mass": 0.05,

    "item_id": "item_iris",
    "file_name":None
}

item_orchids = {

    "name": "Orchids",

    "description": "Orchid flowers found on the flower bed.",

    "mass": 0.05,

    "item_id": "item_orchids",
    "file_name":None
}

item_roses = {

    "name": "Roses",

    "description": "Roses found on the flower bed",

    "mass": 0.05,

    "item_id": "item_roses",
    "file_name":None
}

item_tulpis = {

    "name": "Tulips",

    "description": "Tulips found on the flower bed.",

    "mass": 0.05,

    "item_id": "item_tulips",
    "file_name":None
}

item_daffodils = {

    "name" : "Daffodils",

    "description" : "Daffodils found on the flower bed",

    "mass": 0.05,

    "item_id": "item_daffodils",
    "file_name":None
}

item_daisys = {

    "name": "Daisys",

    "description": "Daisys found on the flower bed",

    "mass": 0.05,

    "item_id": "item_daisys",
    "file_name":None
}

item_buttercups = {

    "name": "Buttercups",

    "description": "Buttercups found on the flower bed",

    "mass": 0.05,

    "item_id": "item_buttercups",
    "file_name":None
}

item_poison = {
    "name": "Poison",

    "description": "Poison you made in Kirill's lab, it  could be dangerous",

    "mass": 0.05,

    "item_id": "item_poison",

    "damage": 100,

    "uses": 1,

    "file_name":None
}

items = { 
    # General Items
    "item_laptop": Item(**item_laptop),
    "item_crisps": Item(**item_crisps),
    "item_blood": Item(**item_bloodsample),
    
    # Notes
    "item_letter": Note(**item_letter),
    "item_mysteriousnote": Note(**item_mysteriousnote),
    "item_kitchennote": Note(**item_kitchennote),
    "item_victimnote": Note(**item_victimnote),
    "item_flowerbednote": Note(**item_flowerbednote),
    "item_book": Note(**item_book),
    "item_gallerynote": Note(**item_gallerynote),
    # Weapons
    "item_controller": Weapon(**item_controller),
    "item_brick": Weapon(**item_brick),
    "item_woodblocks": Weapon(**item_woodblocks),
    "item_shatteredglass": Weapon(**item_glass),
    "item_knife": Weapon(**item_knife),
    "item_pan": Weapon(**item_pan),
    "item_glass": Weapon(**item_glass),
    # Herbs
        # Not working herbs
    "item_orchids": Herb(**item_orchids),
    "item_daisys": Herb(**item_daisys),
    "item_buttercups": Herb(**item_buttercups),
    "item_roses": Herb(**item_roses),
        # Herbs that cure the posion
    "item_tulips": Herb(**item_tulpis),
    "item_daffodils": Herb(**item_daffodils),
    "item_iris": Herb(**item_iris),
    
    # Keys
    "item_gardenkey": Key(**item_gardenkey),
    "item_labkey": Key(**item_labkey),
    "item_shedkey": Key(**item_shedkey),
    "item_gallerykey": Key(**item_gallerykey),
    # Healing
    "item_lemonade": Healing(**item_lemonade),
    "item_apples": Healing(**item_apples),
    "item_icecream": Healing(**item_icecream),
    "item_pork": Healing(**item_pork)
}
