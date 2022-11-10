



# Create a list of sleuth cards
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


# Create a dictionary of wanted names and values
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


# Create a thief class
# thief has name, wanted value, captured status, additional crimes, location
class thief:
    def __init__(self, name, location):
        self.name = name
        self.captured_status = False
        self.additional_crimes = 0
        self.succesful_escapes = 0
        self.location = location
        self.final_bounty = 0
        self.arresting_detective = "None"
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other


# Create a player class
# player has a detective name, list of held cards, current winnings, arrested thieves list
class player:
    def __init__(self, name):
        self.name = name
        self.held_cards = []
        self.winnings = 0
        self.arrested_thieves = []
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other






def main():
    # Begin a new game
    new_game()
    # Begin a new round of the game
    new_round()





def new_game():
    # Ask for the number of players
    players = int(input("How many players?"))
    # Each player chooses a detective ID



# def new_round():
#     # Pick a random thief




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