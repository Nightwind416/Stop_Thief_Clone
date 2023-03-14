import random
import csv


def standard_input():
    yield 3
    yield 1
    yield 1
    yield 1
    yield 1

# Dictionary of sleuth cards
sleuth_cards = {
    'Take another Turn': 3,
    'Lose a turn': 3,
    'Move Anywhere': 2,
    'Move 3 Extra Spaces': 1,
    'Move 4 Extra Spaces': 2,
    'Move 5 Extra Spaces': 1,
    'Move 6 Extra Spaces': 1,
    'Free Tip': 4,
    'Buy a Tip for $50': 3,
    'Buy a Tip for $100': 2,
    'Get 3 Extra Clues': 1,
    'Get 4 Extra Clues': 1,
    'Get 5 Extra Clues': 1,
    'Get 6 Extra Clues': 1,
    'Collect $100 from another Detective': 2,
    'Collect $200 from another Detective': 2,
    'Back to the Acme Detective Agency (You or another Detective)': 2,
}


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


# Dictionary of thief names and wanted values
thief_list = {
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
player_move_list = [
    "Free Clue",
    "Roll Dice",
    "Attempt Arrest",
    "Use Sleuth Card",
    "Last 10 Clues",
    "End Turn"
    ]


# Thief class - name, wanted value, captured status, additional crimes, current location
class Thief:
    def __init__(self, name, space_number):
        self.name = name
        self.captured_status = False
        self.additional_crimes = 0
        self.succesful_escapes = 0
        self.space_number = space_number
        self.bounty = thief_list.get(name)
        self.arresting_detective = None
        self.clue_list = []
        self.previous_space = "0"
        self.valid_moves_dict = {}
        with open('thief_valid_moves_list.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.valid_moves_dict[row['space_number']] = row
    def __str__(self):
        return self.name
    # Set
    def set_location(self, space_number):
        self.space_number = space_number
    def increase_bounty(self, amount):
        self.bounty += amount
    # Increase crime count
    def increase_crimes(self):
        self.additional_crimes += 1
    # Increase escape count
    def increase_escapes(self):
        self.succesful_escapes += 1
    # Set captured status
    def set_captured_status(self, status):
        self.captured_status = status
    # Set arresting detective
    def set_arresting_detective(self, detective):
        self.arresting_detective = detective
    def set_clue_list(self, clue_type):
        if len(self.clue_list) < 10:
            self.clue_list.append(clue_type)
        else:
            self.clue_list.append(clue_type)
            self.clue_list.pop(0)
    def set_previous_space(self, space_number):
        self.previous_space = space_number
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
    def get_general_location(self):
        return self.valid_moves_dict[str(self.space_number)]['location']
    def get_location_type(self):
        return self.valid_moves_dict[str(self.space_number)]['space_type']
    def get_exact_location(self):
        return self.space_number
    # Get captured status
    def get_captured_status(self):
        return self.captured_status
    # Get arresting detective
    def get_arresting_detective(self):
        return self.arresting_detective
    def get_clue_list(self):
        return self.clue_list
    def get_previous_space(self):
        return self.previous_space


# Player class - detective name, list of held cards, current cash, arrested thieves list
class Player:
    def __init__(self, player_number, name):
        self.player_number = player_number
        self.name = name
        self.held_cards = []
        self.cash = 300
        self.arrested_thieves = []
    def __str__(self):
        return self.name


def main():
    # Game setup, like player number
    game_setup()
    # Begin a new game with current setup
    play_game()
    # Show Results
    results()
    # Play again?
    play_again()
    # Quit game
    end_game()


def game_setup():
    # Ask for the number of players
    global number_players
    number_players = int(input("How many players?"))
    print("There are " + str(number_players) + " players.")
    # Loop through each player asking to choose one of the detective IDs from the list
    global player_list
    player_list = []
    for i in range(number_players):
        # Create a numbered list of detective IDs
        id_list = "\n".join([f"{j+1}. {id}" for j, id in enumerate(detective_ids)])
        # Ask player to choose a detective ID
        detective_choice = int(input(f"Player {i+1}, choose a detective ID by entering the corresponding number:\n{id_list}\n")) - 1
        # Remove detective ID from list
        chosen_id = detective_ids.pop(detective_choice)
        # Create a new player
        new_player = Player(i + 1, chosen_id)
        # Add new player to player list
        player_list.append(new_player)
    # Print Welcome message
    detective_names = ", ".join([str(p.name) for p in player_list[:-1]]) + ", and " + str(player_list[-1].name)
    print("Detectives " + detective_names + " have joined the hunt.")
    print("Each detective has been given $" + str(player_list[-1].cash) + " starting cash.")
    return


def play_game():
    # Create a new thief from the wanted list and set the starting crime space
    with open("thief_valid_moves_list.csv", 'r') as f:
        reader = csv.DictReader(f)
        crime_locations = [row['space_number'] for row in reader if row['space_type'] == 'Crime']
        crime_locations.remove('709')
    global new_thief
    new_thief = Thief(random.choice(list(thief_list.keys())), random.choice(crime_locations))
    new_thief.set_clue_list("Crime")
    print("A new thief named " + new_thief.name + " has been detected committing a crime somehwere in " + new_thief.get_general_location())
    print("Their current arrest reward is: " + str(new_thief.bounty))
    # Take turns until thief arrested
    player_number = 1
    print("Player number: " + str(player_number) + "   Number of players: " + str(number_players))
    while True:
        # player turn
        print("Player " + str(player_number) + ", it is your turn.")
        player_turn(player_number)
        # next player
        player_number += 1
        print("Player number: " + str(player_number) + "   Number of players: " + str(number_players))
        if player_number > number_players:
            player_number = 1
        print("Next player up, player " + str(player_number) + ", it is your turn.")
    return


def player_turn(player_number):
    end_turn = False
    turn_move_list = player_move_list.copy()
    global new_thief
    while end_turn == False:
        # Create a numbered list of player turn options
        turn_options = "\n".join([f"{i+1}. {move}" for i, move in enumerate(turn_move_list)])
        # Ask player pick an option
        turn_choice_number = int(input(f"Pick an option by entering the corresponding number:\n{turn_options}\n")) - 1
        turn_choice = turn_move_list[turn_choice_number]
        if turn_choice == 'Free Clue':
            free_clue = get_clue(1)
            # Update choice list for this turn
            # free_clue = "Free Clue Received this turn: " + str(free_clue) + "    Use a Sleuth Card to receive more clues."
            # turn_move_list[0] = free_clue
        elif turn_choice == 'Roll Dice':
            dice_roll = random.randint(1, 6)
            print("You rolled a", dice_roll)
            # Update choice list for this turn
            roll_reminder = "Rolled this turn: " + str(dice_roll) + "    Use a Sleuth Card to roll again."
            turn_move_list[1] = roll_reminder
        elif turn_choice == 'Attempt Arrest':
            arrest_attempt()
        elif turn_choice == 'Use Sleuth Card':
            use_sleuth_card()
        elif turn_choice == 'Last 10 Clues':
            print(new_thief.get_clue_list())
        elif turn_choice == 'End Turn':
            print("End Turn")
            end_turn == True
            break
        else:
            print("Invalid move choice, please try again.")
    return


def get_clue(number):
    while number > 0:
        # Random chance thief does nothing
        if random.randint(1, 100) < 20:
            print("The theif doesn't make a move")
            clue_type = "No Movement"
            number -= 1
        else:
            clue_type = thief_move()
            number -= 1
    return clue_type


def thief_move():
    global new_thief
    print("Thief current space: " + new_thief.get_exact_location())
    print("Thief previous space: " + new_thief.get_previous_space())
    with open("thief_valid_moves_list.csv", 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['space_number'] == str(new_thief.get_exact_location()):
                valid_moves = [row['valid_move_{}'.format(i)] for i in range(1, 9) if row['valid_move_{}'.format(i)] != '']
                print("Valid moves: " + str(valid_moves))
                if new_thief.get_previous_space() in valid_moves:
                    valid_moves.remove(new_thief.get_previous_space())
                    print("Amended valid moves: " + str(valid_moves))
                new_location = random.choice(valid_moves)
                new_thief.set_previous_space(new_thief.get_exact_location())
                new_thief.set_location(new_location)
                break
    print("Thief new space: " + new_thief.get_exact_location())
    print("Thief new space type: " + new_thief.get_general_location())
    clue_type = new_thief.get_location_type()
    new_thief.set_clue_list(clue_type)
    # print("Clue type: " + str(clue_type))
    return clue_type


def arrest_attempt():
    ...
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


def use_sleuth_card():
    ...


if __name__ == "__main__":
    main()