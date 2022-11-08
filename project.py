import sys

class thief
class detective
class sleuth_card
class board
class scanner





current_thief = {
  "name": name,
  "value": 0,
  "location": "null",
  "crimes": 1,
}







def main():
    ...






def begin_new_round()
    rand(thief)
    rand(crime_location)
    building_name = building_name(crime_location)
    print(f"A crime was committed in Building {Building name}")






def building_name(location)
    




def thief_move():
    while True
        random_direction = rand(N/NE/E/SE/S/SW/W/NW)
        if random_direction location is valid
            update thief.location
            play location sound
            if new_location is crime
                update thief.crimes
            if new_location is subway
                exit_station at rand(station)
                update thief.location









def attempt_arrest(location):
    if location invalid
        print(f"Detective {detective.name}, you are docked $1000 for making a False Arrest! Check your notes and be more careful next time.")
        play false_arrest_sound
        return False
    rand(arrest/flee)
    if arrest
        print(f"You're gonna pay {thief.name}")
        return True
    else
        print("You won't catch me copper!")
        moves = 
        for (var moves = rand(4 to 6); moves > 0; moves--) {
            thief_move();
        }
        return False



def draw_card():
    rand(cards)
    return card






if __name__ == "__main__":
    main()