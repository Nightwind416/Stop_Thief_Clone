import random
import csv


# def standard_input():
#     yield 3
#     yield 1
#     yield 1
#     yield 1
#     yield 1


# Player move list
options_list = [
    "Clue",
    "Tip",
    "Attempt Arrest",
    "End Game"
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

valid_moves_dict = {}
with open('thief_valid_moves_list.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        self.valid_moves_dict[row['space_number']] = row

# Thief class - name, wanted value, captured status, additional crimes, current location
class Thief:
    def __init__(self, name, space_number):
        self._name = name
        self._bounty = thief_list.get(name)
        self._additional_crimes = 0
        self._succesful_escapes = 0
        self._current_space = space_number
        self._previous_space = "0"
        self._clue_list = []
    def __str__(self):
        return self._name
    # Increase bounty due to extra crimes and arrest escapes
    def increase_bounty(self, amount):
        self._bounty += amount
    # Increase crime count
    def increase_crimes(self):
        self._additional_crimes += 1
    # Increase escape count
    def increase_escapes(self):
        self._succesful_escapes += 1
    # Add clue to list
    def add_to_clue_list(self, clue_type):
        if len(self._clue_list) < 10:
            self._clue_list.append(clue_type)
        else:
            self._clue_list.append(clue_type)
            self._clue_list.pop(0)
    # Get previous space
    def set_previous_space(self):
        self._previous_space = _current_space
    # Get original wanted bounty
    def get_bounty(self):
        return self._bounty
    # Get additional crime count
    def get_crimes(self):
        return self._additional_crimes
    # Get escape count
    def get_escapes(self):
        return self._succesful_escapes
    # Get general location (Building/Street Number)
    def get_general_location(self):
        return self.valid_moves_dict[str(self.space_number)]['location']
    # Get current location type
    def get_location_type(self):
        return self.valid_moves_dict[str(self.space_number)]['space_type']
    # Get exact location
    def get_exact_location(self):
        return self._space_number
    # Get clue list
    def get_clue_list(self):
        return self._clue_list
    # Get previous location
    def get_previous_space(self):
        return self._previous_space


def main():
    while True:
        choice = input("Do you want to start a new game? (y/n)").lower()
        if choice == 'y':
            # Begin a new game
            play_game()
        elif choice == 'n':
            # Quit game
            print("Quitting game...")
            sys.exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def play_game():
    # Create a new thief from the wanted list and set the starting crime space
    with open("thief_valid_moves_list.csv", 'r') as f:
        reader = csv.DictReader(f)
        crime_locations = [row['space_number'] for row in reader if row['space_type'] == 'Crime']
        crime_locations.remove('709')
    global new_thief
    new_thief = Thief(random.choice(list(thief_list.keys())), random.choice(crime_locations))
    new_thief.add_to_clue_list("Crime")
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
        elif turn_choice == 'Attempt Arrest':
            arrest_attempt()
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
    new_thief.add_to_clue_list(clue_type)
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


if __name__ == "__main__":
    main()