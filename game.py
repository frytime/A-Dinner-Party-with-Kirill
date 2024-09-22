# Importing our classes and functions from other files.
from map import *
from player import player
from items import *
from gameparser import *

# Importing modules for use in game.
import random # For random number generation.
import time # For time-related functions.
import sys
import os

"""
HOW THE INVENTORIES / ITEMS WORK:

Inventories for both the player and all rooms contain item IDs. These IDs are used to access the item dictionary in items.py.
If you want to access the item and its variables from the inventory of the player or a room, you must use the get_item_from_id function.
this will return the item as it is constructed in the class, with all variables and methods.
"""
mass = 0.1 # Initialise mass variable & set to mass of player's starting inventory (more efficient to set value manually).
score = 0
doskiptext = False

# Data for player & boss to be used mostly for boss fight. Should work in tandem with playerdata.py.
boss = {"name": "Professor Kirill", "description": "The end of your world.", "health": 200, "alive": True} # Is the description too dramatic?
boss_fight_time = False # Check boolean in main game loop. Call function specifcally for boss fight if boolean set to True.
boss_fight_phase = 0 # Allows for different phases of boss fight (could just print different messages). Consider replacing above boolean with this.
boss_fight_action_taken = False # To be set to true when an action is taken during a boss fight to allow for turn-based fight while forgiving input errors.
boss_self_heals = 3 # Number of self-healing charges boss has. Used up for each self-healing.

def clearscreen(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')

def slowtype(text,delay_time): 
  for character in text:      
    sys.stdout.write(character) 
    sys.stdout.flush()
    time.sleep(delay_time)

def load_file(fileName):
    f = open("ascii_art/"+fileName+".txt", "r",encoding="utf8")
    lines = []
    for x in f:
        #x = x.replace("\n","")
        lines.append(x)
    return lines

def print_art(lines):
    for x in range(len(lines)):
        print('\r' + lines[x], end='\r', flush=True)


def gamestart(name):
    player.name = name
    player.inventory.append("item_letter")
    player.current_room = rooms["room_kitchen"]
    print(r"""
          

   _        ___ _                           ___           _           __    __ _ _   _             _      _ _ _ 
  /_\      /   (_)_ __  _ __   ___ _ __    / _ \__ _ _ __| |_ _   _  / / /\ \ (_) |_| |__     /\ /(_)_ __(_) | |
 //_\\    / /\ / | '_ \| '_ \ / _ \ '__|  / /_)/ _` | '__| __| | | | \ \/  \/ / | __| '_ \   / //_/ | '__| | | |
/  _  \  / /_//| | | | | | | |  __/ |    / ___/ (_| | |  | |_| |_| |  \  /\  /| | |_| | | | / __ \| | |  | | | |
\_/ \_/ /___,' |_|_| |_|_| |_|\___|_|    \/    \__,_|_|   \__|\__, |   \/  \/ |_|\__|_| |_| \/  \/|_|_|  |_|_|_|
                                                              |___/                                             
          
          
          """)
    time.sleep(3)
    slowtype("You approach the mansion. It's hard to make out in the black night, but you know you're at the right address.\n", 0.06)
    time.sleep(0.5)
    slowtype("But before you can think about it too much, a strike of lightning illuminates the building.\n", 0.06)
    time.sleep(1)
    clearscreen()
    print(r"""
⣿⣿⣿⣿⣿⣿⣿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠇⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠘⣿⣿⣿⡿⠛⠛⠛⠛⠛⠛⠉⣠⣦⡈⠙⠛⠛⠛⠛⠛⠻⣿⣿⣿⢿⣿⠁⠀⠀⠀⠀⠹⣿⣿⣿
⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠈⢿⡟⠁⠀⠀⠀⠀⠀⢀⣴⣋⡉⣷⡄⠀⠀⠀⠀⠀⠀⠹⣿⣿⡿⠏⠀⠀⠀⠀⠀⠀⠹⣿⣿
⣿⣿⣿⣟⡃⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⢠⣾⣿⠤⠄⣿⣿⣦⠀⠀⠀⠀⠀⠀⠈⢿⣻⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿
⣿⡏⢉⡭⣽⣿⣿⢿⣿⣯⢭⠉⠀⠀⠀⠀⠀⠀⠰⠿⠿⠿⠷⠶⠿⠿⠿⠷⠀⠀⠀⠀⠀⠀⠈⢭⣽⣿⡿⣿⣿⣯⢭⡉⢹⣿
⣿⡇⢸⠐⠂⣿⡃⡂⣻⡇⡒⢸⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢒⢸⣿⢐⢘⣿⠐⡂⡇⢸⣿
⣿⡇⠸⠴⢦⣿⣧⣧⣿⡧⠶⠜⢸⣿⣿⣿⣿⣿⣿⣫⣽⡏⠀⠀⠘⣿⣏⣿⣿⣿⣿⣿⣿⣿⠳⠴⢼⣿⣴⣴⣿⡴⠦⠇⢸⣿
⣿⣧⣤⣤⣼⣿⣿⣿⣿⣿⣤⡭⠍⣽⣯⣽⣯⣭⣿⠉⣯⡏⠀⠀⠈⣯⡏⢽⡯⣽⣿⣭⣿⠉⠭⣥⣿⣿⣿⣿⣿⣧⣤⣤⣼⣿
⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⣿⣇⣹⣿⣸⣿⠀⣿⡇⠀⠀⠀⣿⡇⣻⣏⣸⣿⣈⣿⡃⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⢸⣿
⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⠀⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⡤⠤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⢸⣿
⣿⡇⢠⠶⠾⣿⣿⣿⣿⣿⠶⢦⣸⣿⣿⣿⣿⣿⣿⣯⣿⡏⠀⠀⢈⣿⣟⣿⣿⣿⣿⣿⣿⣿⣠⠶⢿⣿⣿⣿⣿⡷⠶⢄⢸⣿
⣿⡇⢸⠈⡁⣿⣿⣿⣿⣏⢈⠉⠁⢩⠉⢩⡍⠉⣭⠉⣿⡇⠀⠀⠀⣿⡏⢩⡍⠉⡍⠉⢩⠁⠉⣉⢸⣿⣿⣿⣿⡇⡁⢸⢸⣿
⣿⡇⠘⠒⢲⣿⣿⣿⣿⣷⠒⠒⠀⣿⣇⣸⣯⣨⣿⡀⠿⠇⠀⠀⠀⠿⠇⣸⣇⣸⣿⣀⣿⡅⠑⠒⣾⣿⣿⣿⣿⡗⠒⠚⢸⣿
⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⢸⣿
⣿⣧⣤⣤⣼⣿⣿⣿⣿⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣧⣤⣤⣼⣿
⣿⡇⠀⠀⢸⣿⣿⣿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣿⣿⣿⡇⠀⠀⢸⣿
⣿⡇⠀⣀⣸⣿⣿⣿⡇⢨⣿⣿⣿⣿⣿⣿⣿⣿⠀⣷⣿⣿⣿⣿⣿⣿⣾⡀⣸⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣇⣀⡀⢸⣿
⣿⡇⢸⠡⠌⣿⣿⣿⡇⢸⣿⡏⠤⢹⡯⠠⢹⣿⠀⡏⠀⠀⠀⠀⠀⠀⠈⡇⣿⡏⠄⢹⡏⠤⢹⣿⡇⢸⣿⣿⣿⡏⠄⢱⢸⣿
⣿⡇⠸⣬⣥⣿⣿⣿⡇⢸⣿⣧⣭⣼⣯⣬⣼⣿⠀⡇⠀⠀⠀⠀⠀⠀⠀⡇⣿⣧⣥⣼⣧⣬⣼⣿⡇⢸⣿⣿⣿⣧⣥⡽⢸⣿
⣿⡇⠀⠀⢸⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⡇⠀⠀⠀⠀⠀⠀⠀⡇⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡇⠀ ⢸⣿
⣿⣧⣤⣤⣼⣿⣿⣿⣧⣼⣿⣿⣿⣿⣿⣿⣿⣿⣤⣧⣤⣤⣤⣤⣤⣤⣤⣧⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣧⣤⣤⣼⣿
          
          """
    )
    time.sleep(2)
    slowtype("Hello, " + name + "\n", 0.1)
    time.sleep(0.6)
    slowtype("My name is Kirill" + "\n", 0.1)
    time.sleep(0.6)
    slowtype("It is nice to meet you \n", 0.1)
    time.sleep(0.6)
    slowtype("Please come in to the kitchen", 0.1)
    time.sleep(1.4)
    clearscreen()
    slowtype("""
You enter the kitchen. Kirill explains that everyone else who was invited did not \n
turn up and you are the only one there. The Kitchen is almost completely destroyed \n
and you wonder why you accepted this invitation. Kirill then leaves to get something. \n
While waiting, you spot a key labelled 'garden' as well as a note. This might explain \n
what is going on, so you pick both of them up. Might be useful to use them.
    """, 0.02)
    player.inventory.append("item_gardenkey")
    player.inventory.append("item_kitchennote")


def get_item_from_id(item_id):
    return items[item_id]

def parse_item_input(user_input):
    return str("item_" + user_input.lower())

def print_time(start_time, time_warning):
    max_time = 2400000000000 # 40 minutes in nanoseconds.
    current_time = time.time_ns()
    time_remaining = max_time - (current_time - start_time)
    print("\n")
    if time_remaining <= 0:
        slowtype("You can no longer breathe\n", 0.05)
        time.sleep(1)
        slowtype("You fall to the floor, clutching at your own throat\n", 0.05)
        time.sleep(1)
        slowtype("As your vision begins to fade, you hear the jingle of a key, unlocking the front door\n", 0.05)
        time.sleep(1)
        slowtype("YOU LOSE\n", 0.5)
        time.sleep(5)
        sys.exit()
    elif time_remaining <= 600000000000 and time_warning < 4:
        slowtype("It is difficult to breathe\n", 0.05)
        time.sleep(1)
        slowtype("You are running out of time\n", 0.05)
        time_warning = 3
    elif time_remaining <= 1200000000000 and time_warning < 3:
        slowtype("You begin to have difficulty breathing\n", 0.05)
        time.sleep(1)
        slowtype("The poison is taking effect\n", 0.05)
        time_warning = 2
    elif time_remaining <= 1800000000000 and time_warning < 2:
        slowtype("You begin to feel a little light-headed\n", 0.05)
        time.sleep(1)
        slowtype("You know that you have been poisoned", 0.05)
        time_warning = 1
    elif time_warning < 1:
        slowtype("You feel a little strange.\n", 0.05)
        time.sleep(1)
        slowtype("You feel like there is poison in the air.\n", 0.05)
        time.sleep(1)
        slowtype("Your time is limited.\n", 0.05)
    return time_warning


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names.

    """
    if room.items != []: # Check for empty list.
        if doskiptext == False:
            slowtype("There is:  \n", 0.05)
            time.sleep(0.5)
        else:
            print("There is:  \n", 0.05)
        for item in room.items:
            currentitem = str(get_item_from_id(item))
            print(currentitem)
            if doskiptext == False:
               time.sleep(1)
        if doskiptext == False:
            slowtype("here. \n", 0.05)
            time.sleep(1)
        else:
            print("here. \n")
        print("")


def print_inventory_items(local_items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:
    """
    if local_items != []: # Check for empty list.
        if doskiptext == False:
            slowtype("You have: \n", 0.05)
            time.sleep(1)
        else:
            print("You have: ")
        for item in local_items:
            currentitem = (str(get_item_from_id(item)))
            print(currentitem)
            if doskiptext == False:
                time.sleep(1)
        print("")
    if doskiptext == False:
        time.sleep(1)



def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this).

    """
    print()
    if room.file_name != None:
        lines = load_file(room.file_name)
        print_art(lines)
    if doskiptext == False:
        slowtype(room.name.upper(), 0.05)
        time.sleep(0.6)
    else:
        print(room.name.upper())
    print()
    if doskiptext == False:
        slowtype(room.description, 0.02)
        time.sleep(0.6)
    else:
        print(room.description)
    print()

    if room.items != []:
        print_room_items(room)

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    """
    return rooms[exits[direction]].name


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    """
    print("GO " + direction.upper() + " to " + leads_to)
    if doskiptext == False:
        time.sleep(0.3)


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    if doskiptext == False:
        slowtype("You can: \n", 0.05)
        time.sleep(1)
    else:
        print("You can: \n")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for room_item_id in room_items:
        item = get_item_from_id(room_item_id)
        print("TAKE " + item.id.upper()[5:] + " to take " + item.name)
        if doskiptext == False:
            time.sleep(0.5)
    print("")
    for inv_item_id in inv_items:
        item = get_item_from_id(inv_item_id)
        print("DROP or USE " + item.id.upper()[5:] + " to drop or use " + item.name)
        if doskiptext == False:
            time.sleep(0.5)
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."

    """
    if direction in player.current_room.exits and boss_fight_time == False:
        next_room = rooms[player.current_room.exits[direction]]
        if next_room.unlock(player.inventory) == True:
            player.current_room = next_room
            slowtype("YOU ARE NOW ENTERING: "+ player.current_room.name, 0.05)
            time.sleep(1)
        else:
            slowtype("This is locked, you need to find a key", 0.05)
            time.sleep(1)
    elif boss_fight_time == True:
        slowtype("You cannot do that at this time.", 0.05)
    else:
        slowtype("You cannot go there.", 0.05)
        time.sleep(1)


def execute_take(user_input):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."

    """
    item_id = parse_item_input(user_input)
    try:
        item = get_item_from_id(item_id)
    except KeyError:
        if doskiptext == False:
            slowtype("You cannot take that.", 0.05)
            time.sleep(1)
        else:
            print("You cannot take that.")
        return
    if player.take_item(item) and boss_fight_time == False:
        player.current_room.remove_item(item)
        if doskiptext == False:
            slowtype("You take the " + item.name + ".", 0.05)
            time.sleep(1)
        else:
            print("You take the " + item.name + ".")
    elif boss_fight_time == True:
        if doskiptext == False:
            slowtype("You cannot do that at this time.", 0.05)
            time.sleep(1)
        else:
            print("You cannot do that at this time.")
    else:
        mass_difference = item.mass - (player.max_mass - player.current_mass)
        if doskiptext == False:
            slowtype("You try to lift the " + item.name + ", but your body fails you. The strain is too great.", 0.05)
            time.sleep(1)
            slowtype("You think you might be able to pick something up if you were to drop around " + str(round(mass_difference, 2)) + " kg worth of things.", 0.05)
            time.sleep(1)
        else:
            print("You try to lift the " + item.name + ", but your body fails you. The strain is too great.", 0.05)
            print("You think you might be able to pick something up if you were to drop around " + str(round(mass_difference, 2)) + " kg worth of things.", 0.05)
    return

def execute_drop(user_input):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    
    """
    item_id = parse_item_input(user_input)
    try:
        item = get_item_from_id(item_id)
    except KeyError:
        if doskiptext == False:
            slowtype("You cannot drop that.", 0.05)
            time.sleep(1)
        else:
            print("You cannot drop that.")
        return
    if item_id in player.inventory and boss_fight_time == False:
        player.drop_item(item)
        player.current_room.add_item(item)
        if doskiptext == False:
            slowtype("You drop the " + item.name + ".", 0.05)
            time.sleep(1)
        else:
            print("You drop the " + item.name + ".")
    elif boss_fight_time == True:
        slowtype("You cannot do that at this time.", 0.05)
    else:
        if doskiptext == False:
            slowtype("You cannot drop that.", 0.05)
            time.sleep(1)
        else:
            print("You cannot drop that.")
    return

def execute_use(user_input):
    """This function takes item_id as an argument and checks if the item has a use. If so,
    the function for the use is called from the item's dictionary.
    """
    global boss
    global player
    global boss_fight_action_taken


    item_id = parse_item_input(user_input)
    try:
        item = get_item_from_id(item_id)
    except KeyError:
        if doskiptext == False:
            slowtype("You cannot use that.", 0.05)
            time.sleep(1)
        else:
            print("You cannot use that.")
        print()
        return
    if item_id in player.inventory:
        fileName = item.file_name
        if fileName != None:
            lines = load_file(fileName)
            print_art(lines)
        else:
            print("No fileName")
            print(type(item))
        if type(item) is Weapon:
            if boss_fight_time == True:
                base_damage = item.getDamage()
                if item.uses == 1:
                    print(f"The {item.name} breaks between your hands, but the shrapnel causes extra damage.")
                    base_damage += 10
                    player.inventory.remove(item_id)
                item.uses -= 1
                total_damage = random.randint(base_damage - 2, base_damage + 2)
                boss["health"] -= total_damage
                print("You have dealt", total_damage, "points of damage to Professor Kirill!")
                boss_fight_action_taken = True
            else:
                print("There is no one around to use this weapon on.")
        elif type(item) is Healing:
            if item.heal(player):
                boss_fight_action_taken = True
        elif type(item) is Herb:
            item.add(player)
        elif type(item) is Note:
            item.read()
            input("Press enter to continue")
        else: # Print message if item does not have a use.
            slowtype("Sorry, but you cannot use that item.", 0.05)
            time.sleep(1)
    else:
        slowtype("Sorry, but you do not have that item.", 0.05)


def execute_read(item):
    if item == "letter" and "item_letter" in player.inventory and boss_fight_time == False:
        if doskiptext == False:
            slowtype("You read the letter.", 0.05)
            slowtype("It's contents are as follows:", 0.05)
            time.sleep(1)
        else:
            print("You read the letter.")
            print("It's contents are as follows:")
        item = items["item_letter"]
        item.read()
    elif boss_fight_time == True:
        slowtype("You cannot do that at this time.", 0.05)
    # elif item == "letter":
    #     slowtype("You do not have that item in your inventory.", 0.05)
    #     time.sleep(1)
    else:
        item_id = parse_item_input(item)
        try:
            item = get_item_from_id(item_id)
        except KeyError:
            if doskiptext == False:
                slowtype("You cannot use that.", 0.05)
                time.sleep(1)
            else:
                print("You cannot use that.")
            return
        if type(item) is Note:
            item.read()
            input("Press enter to continue")
        else:
            if doskiptext == False:
                slowtype("Sorry, but you cannot read that.", 0.05)
                time.sleep(1)
            else:
                print("Sorry, but you cannot read that.")



def assess_print(dictionary_to_print):
    """This function is used by execute_assess to print lines relating to assessing someone
    (player or boss).
    """
    if dictionary_to_print == player:
        slowtype("Name: " + dictionary_to_print.name, 0.05)
        print()
        slowtype("Description: " + dictionary_to_print.description, 0.05)
        print()
        slowtype("Health: " + str(dictionary_to_print.health), 0.05)
        print()
        print_inventory_items(player.inventory)
        time.sleep(1)
        print()
        if dictionary_to_print.alive == True:
            print("Alive.")
            time.sleep(1)
        else:
            print("Dead.")
            time.sleep(1)
    else:
        slowtype("Name: " + dictionary_to_print["name"], 0.05)
        print()
        slowtype("Description: " + dictionary_to_print["description"], 0.05)
        print()
        slowtype("Health: " + str(dictionary_to_print["health"]), 0.05)
        time.sleep(1)
        print()
        if dictionary_to_print["alive"] == True:
            print("Alive.")
            time.sleep(1)
        else:
            print("Dead.")
            time.sleep(1)


def execute_assess(entity):
    """This function is designed only to be used during the boss fight. It allows the player
    to check the health of both themselves and the boss.
    """
    global boss_fight_action_taken
    if entity == "me" or entity == "myself" or entity == "yourself" or entity == "boss" or entity == "kirill":
        if boss_fight_time == True:
            boss_fight_action_taken = True
        if entity == "me" or entity == "myself" or entity == "yourself":
            clearscreen()
            slowtype("You assess yourself.", 0.05)
            time.sleep(1)
            print()
            assess_print(player)
        elif (entity == "boss" or entity == "kirill") and boss_fight_time == True:
            clearscreen()
            slowtype("You assess Kirill.", 0.05)
            time.sleep(1)
            print()
            assess_print(boss)
        else:
            slowtype("You cannot do that at this time.", 0.05)
    else:
        slowtype("Sorry, that entity is not recognised.", 0.05)
        time.sleep(1)


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    clearscreen()
    global doskiptext
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            if boss_fight_time == True:
                slowtype("You cannot leave the area!", 0.05)
                time.sleep(1)
            else:
                execute_go(command[1])
        else:
            slowtype("Go where?", 0.05)
            time.sleep(1)
            print()

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            slowtype("Take what?", 0.05)
            time.sleep(1)
            print()

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            slowtype("Drop what?", 0.05)
            time.sleep(1)
            print()

    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1])
        else:
            slowtype("Use what?", 0.05)
            time.sleep(1)
            print()

    elif command[0] == "read":
        if len(command) > 1:
            execute_read(command[1])
        else:
            slowtype("Read what?", 0.05)
            time.sleep(1)
            print()

    elif command[0] == "assess":
        print(command)
        if len(command) > 1:
            execute_assess(command[1])
        else:
            slowtype("Assess what?", 0.05)
            time.sleep(1)
            print()
    
    else:
        slowtype("This makes no sense.", 0.05)
        time.sleep(1)
        print()


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")
    if user_input == "skiptext":
        doskiptext = True
    elif user_input == "slowtext":
        doskiptext = False

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input



    


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:
    """

    # Next room to go to
    return rooms[exits[direction]]


def life_check(): # Function to check whether player is dead & set boss to dead if boss health = 0. If player is dead, quit the game.
    global boss
    if player.alive == False:
        slowtype("The life is seeping out of your body.", 0.05)
        print()
        slowtype("You regret your failure...", 0.1)
        print()
        if boss_fight_time == True:
            slowtype("You were unable to defeat Kirill...", 0.07)
        else:
            slowtype("You cannot help but regret your inability to solve this mystery.", 0.05)
        time.sleep(3)
        sys.exit() # Quit game.
    if boss["health"] <= 0:
        boss["alive"] = False


def boss_menu():
    # Display specialised menu for boss fight.
    global boss_fight_action_taken
    global player
    global boss
    print()
    while boss_fight_action_taken == False:
        if boss["health"] == 200:
            slowtype("You look at Kirill. He seems spotless.", 0.02)
            time.sleep(1)
            print()
        elif boss["health"] >= 180:
            slowtype("You look at Kirill. He seems a little tired, but not significantly worse for wear.", 0.02)
            time.sleep(1)
            print()
        elif boss["health"] >= 150:
            slowtype("You look at Kirill. There are visible marks and bruises.", 0.02)
            time.sleep(1)
            print()
        elif boss["health"] >= 100:
            slowtype("You look at Kirill. The healthiest-looking parts of his skin are a ghostly white.", 0.02)
            time.sleep(1)
            print()
        slowtype("You can:", 0.02)
        print()
        print("ASSESS YOURSELF to see your state")
        time.sleep(0.3)
        print("ASSESS KIRILL to see his state")
        time.sleep(0.3)
        for item in player.inventory:
            currentitem = get_item_from_id(item)
            if type(currentitem) == Weapon:
                print("USE " + currentitem.id.upper()[5:] + " to use " + currentitem.name + ", damaging Kirill")
                time.sleep(0.3)
            elif type(currentitem) == Healing:
                print("USE " + currentitem.id.upper()[5:] + " to use " + currentitem.name + ", healing yourself")
                time.sleep(0.3)
        user_input = input("> ")
        normalised_user_input = normalise_input(user_input)
        execute_command(normalised_user_input) # Boss fight effects will be programmed using item uses.


def boss_action():
    global boss_self_heals
    choice = random.randint(1, 3)
    if choice == 1: # Damage calculation for if Kirill attacks.
        print("Kirill attacks!")
        time.sleep(1)
        if boss["health"] != 200:
            desperation = (200 - boss["health"]) / 40
        else:
            desperation = 0
        base_damage = random.randint(1, 10)
        if desperation > 1:
            total_damage = base_damage * desperation
        else:
            total_damage = base_damage
        player.take_damage(total_damage)
    elif choice == 2: # Give Kirill limited number of self-healing charges.
        if boss_self_heals > 0 and boss["health"] <= 70:
            boss["health"] += 50
            slowtype("Kirill drank something from a flask. He looks a little better.", 0.05)
            print()
            time.sleep(1)
        else:
            slowtype("Kirill looks like he's trying to do something with a flask...but he fails!", 0.05)
            print()
            time.sleep(1)
    else:
        slowtype("Kirill appears to be trying to do something. Is he thinking...?", 0.05)
        print()
        time.sleep(1)


def boss_fight(): # Code for boss fight.
    global boss_fight_action_taken
    clearscreen()
    print("BANG!")
    time.sleep(1)
    print()
    dot = "."
    for i in range(1, 4): # Abstract via function later (maybe as a form of simpler slowtype, or integrate feature into slowtype via branched execution?)
        print(dot * i)
        time.sleep(0.5)
    print()
    for i in range(2):
        print("BANG!")
        time.sleep(0.2)
    slowtype("The laboratory door breaks open.", 0.1)
    print()
    time.sleep(0.1)
    slowtype("Kirill says: \"I see you have ruined my little 'tourist trap', of sorts. Well done.\"", 0.1)
    print()
    time.sleep(0.3)
    slowtype('"But..."', 0.1)
    print()
    time.sleep(0.3)
    slowtype('"A professor has no need for a student who cannot follow basic instructions."', 0.05)
    print()
    time.sleep(1)
    clearscreen()
    while boss["alive"] == True:
        boss_menu()
        boss_fight_action_taken = False # Reset variable for next loop.
        boss_action()
        life_check()
    slowtype("Kirill crumbles in front of you.", 0.1)
    print()
    slowtype("You have...defeated him", 0.1)
    time.sleep(3)
    clearscreen()
    slowtype("Days later...", 0.1)
    time.sleep(3)
    clearscreen()
    slowtype("You are thanked by the Kingdom for your valour.", 0.3)
    time.sleep(3)
    print()
    slowtype("You are awarded the Steel Shield for actions contributing to the safety of the Kingdom.", 0.1)
    print()
    slowtype("You are also awarded the Golden Scythe. Your neutralisation of the poison has aided the Kingdom's agriculture.", 0.1)
    time.sleep(5)
    clearscreen()
    slowtype("It's the end.", 0.5)
    time.sleep(3)
    print()
    slowtype("You feel sleepy...", 0.6)
    time.sleep(3)
    print()
    slowtype("Darkness approaches...", 0.7)
    sys.exit()


# This is the entry point of our program
def main():
    global boss_fight_time
    start_time = time.time_ns()
    time_warning = 0
    clearscreen()
    name = input("Please enter your name >>> ")
    gamestart(name)
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(player.current_room)
        print_inventory_items(player.inventory)

        # Show the menu with possible actions and ask the player
        command = menu(player.current_room.exits, player.current_room.items, player.inventory)

        # Execute the player's command
        execute_command(command)
        life_check()

        time_warning = print_time(start_time, time_warning)

        if player.antidote == 1: # Check for boss fight immediately after executing command, so as to prevent unnecessary printing of text.
            boss_fight_time = True
            boss_fight()

if __name__ == "__main__":
    main()
