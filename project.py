import random

# Standard inputs for AREPL, remove or comment out when compiling
standard_input = ["3", "clue"]



# List of sleuth cards
sleuth_cards = [
    'Take another Turn',
    'Take another Turn',
    'Take another Turn',
    'Lose a turn',
    'Lose a turn',
    'Lose a turn',
    'Move Anywhere',
    'Move Anywhere',
    'Move 3 Extra Spaces',
    'Move 4 Extra Spaces',
    'Move 4 Extra Spaces',
    'Move 5 Extra Spaces',
    'Move 6 Extra Spaces',
    'Free Tip',
    'Free Tip',
    'Free Tip',
    'Free Tip',
    'Buy a Tip for $50',
    'Buy a Tip for $50',
    'Buy a Tip for $50',
    'Buy a Tip for $100',
    'Buy a Tip for $100',
    'Get 3 Extra Clues',
    'Get 4 Extra Clues',
    'Get 5 Extra Clues',
    'Get 6 Extra Clues',
    'Collect $100 from another Detective',
    'Collect $100 from another Detective',
    'Collect $200 from another Detective',
    'Collect $200 from another Detective',
    'Back to the Acme Detective Agency (You or another Detective)',
    'Back to the Acme Detective Agency (You or another Detective)',
    ]

# List of detective IDs
detective_ids = [
    "Mavis Marvel",
    "Kent Ketchum",
    "Harley Hand",
    "Carrie Badger",
    "Rosa Subrosa",
    "Sheerluck Holmes",
    "Lester Lose O'",
    "Nanny Harrow",
    ]

# Ddictionary of wanted names and values
wanted_list = {
    "Armand Slinger": 900,
    "Bunny & Clod": 1000,
    "Emil 'The Cat' Donovan": 800,
    "Felicia Field": 900,
    "Hans Offe": 900,
    "John Doe": 800,
    "Luke Warm": 1000,
    "Ruby Diamond": 800,
    "Saul Teen": 1000,
    "The Brain": 1000,
    }


# Player move list
move_list = ["clue", "roll", "arrest", "use sleuth card", "end turn"]


# Thief class - has name, wanted value, captured status, additional crimes, location
class thief:
    def __init__(self, name, location):
        self.name = name
        self.captured_status = False
        self.additional_crimes = 0
        self.succesful_escapes = 0
        self.location = location
        self.bounty = 0
        self.arresting_detective = None
    def __str__(self):
        return self.name
    # Increase bounty by amount
    def increase_bounty(self, amount):
        self.bounty += amount
    # Increase crime count
    def increase_crimes(self):
        self.additional_crimes += 1
    # Increase escape count
    def increase_escapes(self):
        self.succesful_escapes += 1
    # Set location
    def set_location(self, location):
        self.location = location
    # Set captured status
    def set_captured_status(self, status):
        self.captured_status = status
    # Set arresting detective
    def set_arresting_detective(self, detective):
        self.arresting_detective = detective
    # Get current bounty
    def get_bounty(self):
        return self.bounty
    # Get crime count
    def get_crimes(self):
        return self.additional_crimes
    # Get escape count
    def get_escapes(self):
        return self.succesful_escapes
    # Get current location
    def get_location(self):
        return self.location
    # Get captured status
    def get_captured_status(self):
        return self.captured_status
    # Get arresting detective
    def get_arresting_detective(self):
        return self.arresting_detective


# Player class - has a detective name, list of held cards, current winnings, arrested thieves list
class player:
    def __init__(self, name):
        self.name = name
        self.held_cards = []
        self.winnings = 0
        self.arrested_thieves = []
    def __str__(self):
        return self.name



def main():
    # Begin a new game
    new_game()
    # Begin a new round of the game
    new_round()
    # Game loop
    while True:
        # Check if thief is captured or not
        # If thief is captured, end round
        # If thief is not captured, continue
        # Loop through each player
        for player in players:
            # Call player turn function
            player_turn(player)
            # Check if thief is captured or not
            # If thief is captured, end round
            # If thief is not captured, continue




def new_game():
    # Ask for the number of players
    players = int(input("How many players?"))
    print("There are " + str(players) + " players.")
    # Loop through each player choosing a detective ID and add to a player list
    for i in range(players):
        # Choose a detective ID
        detective = random.choice(detective_ids)
        # Remove detective ID from list
        detective_ids.remove(detective)
        # Create a new player
        new_player = player(detective)
        # Add new player to player list
        players.append(new_player)
        # Print new player
        print("Player " + str(i + 1) + ": " + new_player.name)
        print("Winnings: " + str(new_player.winnings))
        print("Arrested Thieves: " + str(new_player.arrested_thieves))
        print("Held Cards: " + str(new_player.held_cards))



def new_round():
    # Create a new thief from the wanted list
    new_thief = thief(random.choice(list(wanted_list.keys())), "placeholder_location")
    print("The new thief is " + new_thief.name + "!")
    print("Name: " + new_thief.name)
    print("Captured Status: " + str(new_thief.captured_status))
    print("Additional Crimes: " + str(new_thief.additional_crimes))
    print("Succesful Escapes: " + str(new_thief.succesful_escapes))
    print("Location: " + new_thief.location)
    print("Current Bounty: " + str(new_thief.bounty))
    print("Arresting Detective: " + str(new_thief.arresting_detective))





def player_turn(player):
    # Ask for player if ready to take their turn
    # ready_check = input("Player " + player.name + ", are you ready for your clue?")
    player_input = input("What would you like to do?")
    print("You chose to " + player_input + ".")
    # If player input is to move
    # If player input is to sleuth
    # If player input is to arrest
    # If player input is to end turn
    # If player input is to end game
    return



#     rand(thief)
#     rand(crime_location)
#     building_name = building_name(crime_location)
#     print(f"A crime was committed in Building {Building name}")

#     # Report thief name, value, and Building
#     print("Thief: " + current_thief["name"])
#     print("Value: " + current_thief["value"])
#     print("Building: " + current_thief["location"])






# def building_name(location):
    




# def thief_move():
#     while True
#         random_direction = rand(N/NE/E/SE/S/SW/W/NW)
#         if random_direction location is valid
#             update thief.location
#             play location sound
#             if new_location is crime
#                 update thief.crimes
#             if new_location is subway
#                 exit_station at rand(station)
#                 update thief.location









# def attempt_arrest(location):
#     if location invalid
#         print(f"Detective {detective.name}, you are docked $1000 for making a False Arrest! Check your notes and be more careful next time.")
#         play false_arrest_sound
#         return False
#     rand(arrest/flee)
#     if arrest
#         print(f"You're gonna pay {thief.name}")
#         return True
#     else
#         print("You won't catch me copper!")
#         moves = 
#         for (var moves = rand(4 to 6); moves > 0; moves--) {
#             thief_move();
#         }
#         return False



# def draw_card():
#     rand(cards)
#     return card






if __name__ == "__main__":
    main()