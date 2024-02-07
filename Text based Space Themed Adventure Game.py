# Erik Desilets Space Text Adventure Game
# Dictionary for linking rooms to others.
import time                              # used later to see the ending code without the program closing

rooms = {
    'Docking Bay': {'North': 'Crew Quarters', 'item': 'Sight'},
    'Crew Quarters': {'North': 'Galley', 'East': 'Med Bay', 'South': 'Docking Bay', 'West': 'Engine Room',
                      'item': 'Grip'},
    'Galley': {'South': 'Crew Quarters', 'item': 'Trigger'},
    'Engine Room': {'North': 'Cargo Hold', 'East': 'Crew Quarters', 'item': 'Barrel'},
    'Cargo Hold': {'South': 'Engine Room', 'item': 'Magazine'},
    'Med Bay': {'West': 'Crew Quarters', 'North': 'Weapons Bay', 'item': 'Receiver'},
    'Weapons Bay': {'North': 'Bridge', 'South': 'Med Bay', 'item': 'Buttstock'},
    'Bridge': {'South': 'Weapons Bay', 'West': 'Officer Quarters', 'item': 'Handguard'},
    'Officer Quarters': {'East': 'Bridge', 'item': 'None'}  # boss room
}


# definition to show initial information and rules to the game
def show_instructions():
    print('Welcome to a Space based text adventure game.')
    print('\n')
    print('As a part of the Earth Federation Space Corps (EFSC) your task is to find and assemble an energy rifle.')
    print('Current reports state that the ship has been attacked by a Sentinel Infiltrator looking to steal the rifle.')
    print('Once the rifle is assembled you can take this ammunition to defend yourself against the Sentinel threat.')
    print('The rifle was stripped and 8 pieces have been scattered across the ship to hide it from the Infiltrator.')
    print('\n')
    print('To navigate the ship use commands: go South, go North, go East, go West')
    print("To add an item to your inventory: get 'item name'")
    print('To quit the game at any point use command: exit')
    print('-' * 60)  # line break


# Definition to show player status
def show_status():
    print('You are in the', currentRoom)
    print('Inventory:', player_invent)


# A way to measure against a full inventory for the boss fight
full_invent = ['Ammunition', 'Barrel', 'Buttstock', 'Grip', 'Handguard', 'Magazine', 'Receiver', 'Sight', 'Trigger']

# Current inventory status
player_invent = ['Ammunition']

directions = ['go North', 'go South', 'go East', 'go West']
get_item = ['get Barrel', 'get Buttstock', 'get Grip', 'get Handguard', 'get Magazine', 'get Receiver', 'get Sight',
            'get Trigger']

# Starting player in a starting room
currentRoom = 'Docking Bay'

show_instructions()

# Loop forever until user enters exit's or finishes the game
while currentRoom != 'exit':
    print('\n')
    show_status()
    if currentRoom != 'Officer Quarters':                        # loop to test the final room
        if rooms[currentRoom]['item'] != 'None':
            print('You see a', rooms[currentRoom]['item'])
            print('-' * 30)
        else:
            print('-' * 30)
        print('Enter your move:')  # prompts user for command
        user_command = input()  # captures user command
        if user_command == 'exit' or user_command == 'Exit':  # exit sequence
            currentRoom = 'exit'
            print('\n')  # spacing between command and feedback
            print('Thanks for playing, see you next time')
            time.sleep(10)
            print()
        else:  # Movement between rooms loop  and verification of valid statement
            if user_command in directions:
                user_command = user_command.split()
                user_command = user_command[1]
                if user_command in rooms[currentRoom]:
                    currentRoom = rooms[currentRoom][user_command]  # Assigns new room value to currentRoom to be looped
                else:  # if direction is not in the rooms nested dict
                    print("You can't go that way")
                    print('\n')
            elif user_command in get_item:       # loop to acquire item and update player inventory
                user_command = user_command.split()
                user_command = user_command[1]
                player_invent.append(rooms[currentRoom]['item'])
                print(rooms[currentRoom]['item'], 'Acquired')
                if rooms[currentRoom]['item'] in player_invent:
                    del (rooms[currentRoom]['item'])
                    rooms[currentRoom]['item'] = 'None'
                    full_invent.sort()
                    player_invent.sort()
                    if player_invent == full_invent:        # once all items are acquired inventory turns into Rifle
                        player_invent = "Energy Rifle"
            else:  # if user does not give a valid movement command
                print('Invalid move!')
    else:                                 # Outcome if player has the Energy Rifle
        if player_invent == 'Energy Rifle':
            print('The Sentinel Infiltrator senses you and starts to charge you')
            time.sleep(3)
            print('You send a round through its chassis and disabled the Infiltrator')
            time.sleep(3)
            print('Congratulations on completing the rifle and dispatching the threat!!')
            time.sleep(3)
            currentRoom = 'exit'
        elif player_invent != 'Energy Rifle':  # Outcome if player doesn't have the Energy Rifle
            print('The Sentinel Infiltrator senses your presence and charges you')
            time.sleep(3)
            print('Unfortunately you have nothing to defend yourself with and are exterminated')
            time.sleep(3)
            print('Nice job, the Sentinels will now have our technology, John Connor was right')
            time.sleep(3)
            currentRoom = 'exit'
