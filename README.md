# Stop Thief Clone

<details open><summary>Table of Contents</summary>

- [Stop Thief Clone](#stop-thief-clone)
  - [Video Demo](#video-demo)
  - [Description](#description)
  - [Considerations while coding](#considerations-while-coding)
  - [Files](#files)
  - [Code Breakout](#code-breakout)
    - [Imported libraries](#imported-libraries)
    - [Initial variables and program configurations](#initial-variables-and-program-configurations)
    - [main function](#main-function)
    - [play\_game function](#play_game-function)
    - [player\_turn function](#player_turn-function)
    - [thief\_move function](#thief_move-function)
    - [get\_tip function](#get_tip-function)
    - [attempt\_arrest function](#attempt_arrest-function)
    - [debug\_print function](#debug_print-function)
  - [Installation/Usage](#installationusage)
  - [Support/Roadmap/Project Status](#supportroadmapproject-status)
  - [Authors and Acknowledgment](#authors-and-acknowledgment)

</details>

## Video Demo

[Stop Thief Digital Crime Scanner Demo](https://vimeo.com/822862316?share=copy)

## Description

This is a digital recreation of the *Electronic Crime Scanner* handheld battery device from the old board game [Stop Thief](https://en.wikipedia.org/wiki/Stop_Thief) from Parker Brothers.
The *Electronic Crime Scanner* is used to track and give clues as a thief *covertly* moves about the game board.
It did so via a simple 3-digit LED display screen and sound clues, as well as several push buttons for interactions.
The program faithfully recreates the capabilities of the *Electronic Crime Scanner* in a digital version.

## Considerations while coding

- **Thief Move Matrix** -- Creating the move matrix was just...time consuming. Using a copy of the physical board, I started with an excel file to easily create a table of all the spaces and their valid moves. From there, it's easy enough to save a simple excel table as a CSV file. I considered keeping the move matrix as an external CSV due to it's size. It is 184 lines in a CSV or 920 lines as a python dictionary, more than half the total python program code. Unfortunately, I was struggling with properly opening, using, and closing the csv file via python code any time I needed to access the move matrix, or to initially build the dictionary in a way i felt i could understand/manage. Ultimately, going the way of simply 'hard coding' the move matrix as a dictionary exactly how i envisioned was a short/long cut that allowed me to better conceptualize the data and how I was accessing it later in my code. If I ever return to this program, extracting out the move matrix to a csv would be *one* of my goals.
- **Sounds** -- I wasn't going to have any audio and instead just have this be a simple text based program. Before tossing the idea completely, I did some quick searching and discovered just how easy it can be. For this *educational* program, I went ahead and recorded the actual sound effects from the device itself. If I ever return to this code for greater sharing, I would need to swap out the audio for open source or properly licensed files.
- **GUI** -- For the same reasons as sound, I initially did not even consider a GUI based program, thinking that would just compound the difficulty and complexity of the program if I was to continue by myself. I had completed what I would estimate to be about 60% of the *core code* of the game quite quickly, all text/terminal based interactions. As it was going so well, I spent some extra time and did some searching on 'simple python GUI' implementation and was directed to...PySimpleGUI. It, like sound, was quite easy to implement in the simple way I was intending to use it. Even learned to use various buttons and have the windows dynamically update. Conveniently, I was able to keep and refactor some of my original 'print' messages as 'debug' related.
- **Thief Turn Function** -- This is the code that caused me the most time and stress. On it's face, it's easy. The move matrix is set based on the layout of the physical game board. Having the thief randomly move about and report the space type is *easy*. What got difficult was the 'extra little rules' that needed to be considered. Things like:
  1. Thief cannot return to the direct previous space, but can within 2 moves (ie, a triangle move, following board spaces)
  2. Once a crime is committed, it cannot be done again *unless/until* the thief leaves and reenters the building. This one caused me issues for a while. Had to figure out a way to best **temporarily** change a spaces type. Then, when the thief had left a building, change it back. For a while, I kept creating and tracking additional variables within the Thief class. Then realized...just change the dictionary item directly. This could leave the dictionary in an 'unknown' state at the end of the game if you played again without closing, so the thief class copies the move dictionary and then just modifies it's copy.
  3. If the thief comes within 1 space of an uncommitted Crime space, they will always move there next.
  4. When on a subway space, the thief will always choose to use it but, is allowed to return to the same space.
- **Tip Function** -- Once I had become comfortable with them, I decided I could take advantage of the PySimpleGUI popup windows to ensure that the 'Tip' would only be seen by the player it is intended for. It took a little extra checking to make sure I had the multiple windows and popups interacting properly, but turned out perfect.

## Files

I kept this one to a single python program file, apart from the few sound effects in the **audio_files** folder.
The audio samples are direct recordings from an actual **Crime Scanner** device. As I do not intend to share this program commercially or more publicly than with the CS50 course, I feel their reproduction and use here fall under *fair use*.

## Code Breakout

### Imported libraries

- from **pygame** import *mixer* -- used for audio playback
- import **PySimpleGUI** as *sg* -- used for simple gui windows and popups
- import **random** -- used for a few random selections
- import **sys** -- used for debugging and closing the script early (quitting)

### Initial variables and program configurations

- The **valid_moves_dict** is a dictionary of each numbered space's valid moves as well as its general location (building/street) and specific location (Crime/Floor/Street/etc) references
- The **audio_files** is a dictionary of the audio files to easily reference later in the code
- The **thief_list** is a dictionary of known thieves and their starting reward values
- The **subway_spaces** is a list of all Subway spaces (where Thief can 'teleport' around board)
- The **thief_starting_crime_spaces** is a list of all starting crime spaces (where a thief can begin)
- The **Thief class object** holds the a move dictionary copy, name, wanted value, additional crimes, escapes, current location, and move history for the currently active thief and numerous functions on manipulating those values

### main function

- Initial popup asking if you want to start a new game. This is where the program returns after there is a winner.
- Create/display the main game gui window. Includes a note on one rule that is different from the physical board game.
- Allow user to select the number of players and begin (or quit) the game.

### play_game function

- Creates a new random thief and sets their starting space.
- Create and display a popup with the new thief details.
- Loops through the players taking their turns, repeating until there is a winner or the game is closed.

### player_turn function

- Create/display player turn gui window.
- Displays thief location type history.
- There is a debug capability that will show exact thief move history.
- Give player options for getting a Clue, receiving a Tip, attempting an Arrest, and ending (or skipping) their turn.

### thief_move function

- Runs through the thief's possible moves, making various adjustments based on current game/thief status.
- Chance the thief 'does nothing' on a turn. Currently set to 5%.
- Removes previous space from valid moves list, as thief is not allowed to directly backtrack.
- Check if there are any Crime spaces within the valid moves and make that the priority
- Randomly chooses and/or executes the new move.
- Create and display a popup message of how the thief just moved.

### get_tip function

- When a Tip is requested, create and display a popup message with the thief's exact location details.
- Layer this behind an initial warning that only the player requesting the Tip should view the info about to be displayed.

### attempt_arrest function

- When attempting an arrest, will first check to see if the space is valid then attempt if true.
  - Popup message if the player input the wrong location, informing them of such and that they lose a turn.
  - Popup message if the thief escapes arrest. Thief gets 5-6 'free' moves.
- Thief has a possibility of escaping, giving the thief several 'free' moves to get away.

### debug_print function

- To assist with testing, I moved print to it's own *debug* function and activated with a terminal command when starting the program.

## Installation/Usage

- May need to install pygame and/or PySimpleGUI for proper function.
- Run the main 'project.py' script *or* Run the project.exe located in the dist folder (created using pyinstaller).
- To turn on *debug mode*, run from terminal with option argument 'debug' as such: `project.py debug`

## Support/Roadmap/Project Status

- There will be no further updates or support to this release.
- Project is considered **Complete**
- 30 April 2023

## Authors and Acknowledgment

- Christopher E Lorr
- Created as the final project for [CS50x](https://learning.edx.org/course/course-v1:HarvardX+CS50+X/home)
