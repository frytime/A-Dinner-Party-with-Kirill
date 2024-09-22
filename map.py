"""
TO ADD A ROOM:

Create a dictionary for it
Make sure the dictionary contains every key e.g. name (look at others and copy template)
Copy format for instancing room in the rooms dictionary

TO EDIT A ROOM:

Edit the dictionary for it
If you need to add a new variable, make sure you add it to the dictionary and the __init__ function
If it is only used for one room, add the default case to the __init__ function line 16 (looks like this: variable=None)

"""
from player import *

class Room:
    def __init__(self, name, description, exits, items=None, key_required=None, file_name=None):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = items or []
        self.key_required = key_required
        self.file_name = file_name

    def unlock(self, inventory):
        if self.key_required in inventory:
            self.key_required = None
        if self.key_required == None:
            return True
        return False
        
    def remove_item(self, item):
        self.items.remove(item.id)
        return
    
    def add_item(self, item):
        self.items.append(item.id)
        return

    def __str__(self):
        return self.name



# BASEMENT ROOMS
room_labs = {
    "name": "The Laboratory",

    "description":
    """
    You enter the labs. It is very cloudly inside. You feel youself getting \n
    dizzy very quickly. You must get rid of this posion to survive.
    """,

    "exits": {"east": "room_basementroom", "north": "room_mainstaircase"},

    "items": [],

    "key_required": "item_labkey",

    "file_name":None,
}

room_basementroom = {
    "name": "The Basement Room",

    "description":
    """
    There appears to be a living room here, and it is in good condition \n
    You find a note from an anonymous writer on the floor which may give \n
    a clue towards what is going on.
    """,

    "exits":  {"west": "room_labs", "south": "room_basementbedroom"},

    "items": ["item_mysteriousnote"],

    "key_required": None,
    "file_name":None
}

room_basementbedroom = {
    "name": "The Basement Bedroom",

    "description":
    """
    You enter the basement bedroom. The door says 'Stuart Allen', whoever \n
    he is. \n
    In the depths of what was once a magnificent mansion, lies a basement bedroom \n
    now marred by the relentless passage of time and the unforgiving touch of destruction. \n
    This room, a former bastion of comfort and elegance, is now in ruins \n
    """,

    "exits": {"west": "room_labs", "north": "room_basementroom", "south": "room_mainstaircase"},

    "items": [],

    "key_required": None,
    "file_name":None
}

room_basementstaircase = {
    "name": "The Basement Hallway",

    "description":
    """
    You are at the basement staircase. You must decide where to go in \n
    the basement.
    """,

    "exits": {"west": "room_labs", "east": "room_basementbedroom", "up": "room_mainstaircase"},

    "items": [],

    "key_required": None,
    "file_name":None
}

# GROUND FLOOR ROOMS

room_library = {
    "name": "The Library",

    "description":
    """
    Within the once-majestic confines of a grand mansion, there lies a library, \n
    now a poignant relic of former intellectual splendor. What was once a haven for \n
    knowledge and refined aesthetics has been reduced to a somber scene of destruction.
    There is nothing of use in here.
    """,

    "exits": {"south": "room_livingroom", "east": "room_conservatory"},

    "items": [],

    "key_required": None,

    "file_name":None
}

room_conservatory = {
    "name": "The Conservatory",

    "description":
    """
    You enter the conservatory. Two windows are open to the north side of the room, \n
    too small for you to enter. There is also a door there, but it is locked. \n
    Inside of the room are two worn-out \n
    recliners, and a TV that appears to looping a video on Albert Enstein. A \n
    quote by Thomas Edison that states 'I have not failed. I've just found 10,000 \n
    ways that won't work.' There is a controller, a brick and a packet of crisps, \n
    as well as an iris flower pot.
    """,

    "exits": {"west": "room_library", "north": "room_gardenarea", "east": "room_basementstaircase", "south": "room_kitchen"},

    "items": ["item_controller", "item_brick", "item_crisps", "item_iris"],

    "key_required": None,

    "file_name":None

}
room_livingroom = {
    "name": "The Living Room",

    "description":
    """
    The living room in the mansion, now in ruins, stands as a haunting tableau \n
    of devastation. Once an epitome of luxury and comfort, it is marred by \n
    collapsed ceilings, shattered windows, and a disarray of splintered furniture, \n
    casting a poignant contrast to its former opulence. \n
    As you search the room, you discover a log burner \n
    behind a set of webs that still holds a few blocks of wood.
    """,

    "exits": {"north": "room_library", "east": "room_kitchen"},

    "items": ["item_woodblocks"],

    "key_required": None,
    "file_name":None
}

room_kitchen = {
    "name": "The Kitchen",

    "description":
    """
    The kitchen is in a decrepit state. It is as if the \n
    room has not been cleaned in years. You look inside the fridge and you \n
    find: expired chicken breasts, a bottle of lemonade and a pack of 6 apples. \n
    You look inside the freezer and find: a pack of ice, one ice cream and \n
    frozen pork. Other things inside the room include a knife and a pan. 
    """,

    "exits": {"north": "room_conservatory", "east": "room_mainstaircase", "west": "room_livingroom"},

    "items": ["item_lemonade", "item_apples", "item_icecream", "item_pork", "item_knife", "item_pan"],

    "key_required": None,
    "file_name":None
}

room_mainstaircase = {
    "name": "The Main Staircase",

    "description":
    """
    You are at the bottom of the main staircase. You must choose a room \n
    to enter
    """,

    "exits": {"south": "room_kitchen", "north": "room_conservatory", "up": "room_firststaircase", "down": "room_basementstaircase"},

    "items": [],

    "key_required": None,
    "file_name":None
}


# GARDEN ROOMS

room_gardenarea = {
    "name": "The Garden Area",

    "description":
    """
    You have entered the garden. The main area is pretty dull and all of the grass \n
    has seemingly died. There are three areas to the garden: The Flower Bed (west), \n
    the Pond (north) and the Shed (east). 
    """,

    "exits": {"south": "room_conservatory", "north": "room_pond", "east": "room_shed", "west": "room_flowerbed"},

    "items": [],

    "key_required": "item_gardenkey",
    "file_name":None
}

room_flowerbed = {
    "name": "The Flower Bed",

    "description":
    """
    There is a flower bed here. Amongst the flowers you see a note. \n
    The flower bed contains Orchids, \n
    Roses, Tulips, Daisys, Daffodils and Buttercups. There is also broken \n
    glass and a blood sample here.
    """,

    "exits": {"east": "room_gardenarea"},

    "items": ["item_orchids", "item_roses", "item_tulips", "item_daffodils", "item_daisys", "item_buttercups", "item_shatteredglass", "item_blood", "item_flowerbednote"],

    "key_required": None,

    "file_name":None
}
room_pond = {
    "name": "The Pond",

    "description":
    """
    You go to the pond. There is a small bridge that intersects the pond, \n
    full of moss and dirt. The pool goes very deep but there doesn't seem \n
    to be anything here.
    """,

    "exits": {"south": "room_gardenarea"},

    "items": [],

    "key_required": None,
    "file_name":None
}

room_shed = {
    "name": "The Shed",

    "description":
    """
    A weathered shed, nestled amidst overgrown foliage, stands as a testament to \n
    time's gentle yet persistent touch. Its sun-faded wood and rusted roof tell stories of \n
    years gone by, offering a quiet sanctuary for memories and forgotten treasures.
    Once inside, you notice a laptop there \n
    This could become very useful \n
    at some point. There us also a key named 'Gallery'
    """,

    "exits": {"west" : "room_gardenarea"},

    "items": ["item_laptop", "item_gallerykey"],

    "key_required": "item_shedkey",

    "file_name":"ascii-shed"
}


# FIRST FLOOR ROOMS

room_masterbedroom = {
    "name": "The Master Bedroom",

    "description":
    """
    Unlike much of the mansion, the master bedroom in the mansion \n
    is a grand oasis of luxury and sophistication. Spacious and elegantly adorned, \n
    it boasts a king-sized bed, opulent furnishings, and large windows that invite \n
    natural light, creating a haven of comfort and refinement. \n
    In the room, you find a book \n
    titled 'Property of Kirril Sidorov'. \n
    You also find a key labelled 'shed key'
    
    """,
        "exits": {"south": "room_gallery", "north": "room_mainstaircase", "east": "room_mainbathroom"},

        "items": ["item_book", "item_shedkey"],

        "key_required": None,
        
        "file_name":"bed"
}

room_sparebedroom = {
    "name": "The Spare Bedroom",

    "description":
    """
    The well-worn spare bedroom exudes an air of nostalgia. Faded wallpaper, \n
    creaky floorboards, and vintage furnishings paint a picture of a room that \n
    has witnessed countless dreams and whispered secrets. \n
   You see a sign that states that \n
    the room was property of 'Christopher Wallbridge'. He probably \n
    isn't important to the plot. Here, you find a key labelled \n
    'gallery' but it is destroyed. Nothing else is here.
    """,

        "exits": {"north": "room_mainbathroom", "west": "room_gallery"},

        "items": [],

        "key_required": None,
        "file_name": None
}

room_gallery = {
    "name": "The Gallery",

    "description":
    """
    The gallery in the mansion, now reduced to ruin, is a shattered \n
    space of lost artistry. Once a hall of cultural treasures and grandeur, \n
    it is characterized by crumbling walls, broken sculptures, and the forlorn \n
    remnants of once-cherished masterpieces, echoing the passage \n
    of time and the decay of opulence. There are bodies of \n
    people who have tried to solve this mystery, but have failed. \n
    Amongst the debris is a note, you probably want to read it. There is also a key called 'Lab'
    """,

        "exits": {"north": "room_masterbedroom", "east": "room_sparebedroom"},

        "items": ["item_gallerynote", "item_labkey"],

        "key_required": "item_gallerykey",

        "file_name":"ascii-painting"
}

room_firststaircase = {
    "name": "First Floor Staircase",

    "description": 
    """
    You are at the staircase of the first floor. You must \n
    decide where to go from here
    """,

        "exits": {"east": "room_masterbedroom", "west": "room_mainbathroom", "down": "room_mainstaircase"},

        "items": [],

        "key_required": None,
        "file_name":None
}

room_mainbathroom = {
    "name": "The Main Bathroom",

    "description": 
    """The destroyed bathroom, a scene of chaos and devastation, bears the scars \n
      of an unforeseen catastrophe. Shattered tiles, ruptured pipes, and a once-pristine \n
      mirror shattered into fragments, create an unsettling tableau of disarray and broken tranquility. \n
    Amongst the debris, you are able to grab a note from one of the victims.
    """,

        "exits": {"north": "room_mainstaircase", "east": "room_masterbedroom", "south": "room_sparebedroom"},

        "items": ["item_victimnote"],

        "key_required": None,
        "file_name":None
}

rooms = {
    "room_labs": Room(**room_labs),
    "room_basementroom": Room(**room_basementroom),
    "room_basementbedroom": Room(**room_basementbedroom),
    "room_basementstaircase": Room(**room_basementstaircase),
    "room_conservatory": Room(**room_conservatory),
    "room_mainstaircase": Room(**room_mainstaircase),
    "room_gardenarea": Room(**room_gardenarea),
    "room_sparebedroom": Room(**room_sparebedroom),
    "room_gallery": Room(**room_gallery),
    "room_mainbathroom": Room(**room_mainbathroom),
    "room_library": Room(**room_library),
    "room_livingroom": Room(**room_livingroom),
    "room_kitchen": Room(**room_kitchen),
    "room_masterbedroom": Room(**room_masterbedroom),
    "room_firststaircase": Room(**room_firststaircase),
    "room_flowerbed": Room(**room_flowerbed),
    "room_pond": Room(**room_pond),
    "room_shed": Room(**room_shed),
}