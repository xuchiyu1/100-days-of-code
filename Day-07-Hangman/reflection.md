## Problem Definition

Build a command-line Hangman game where:

- A random word is selected
- The player guesses letters
- The game tracks lives
- The game ends on win or loss
## Game Logic Breakdown

1. Choose a random word
2. Initialize game state:
   - lives = 6
   - display = ["_"] * word_length
   - end_of_game = False
3. Enter while loop
4. Ask user for a letter
5. Check:
   - If letter in word → update display
   - Else → reduce lives
6. Print hangman stage
7. Check win / lose condition
## State Management

The game state is controlled by:

- lives (int)
- display (list)
- end_of_game (boolean)

The loop continues based on a boolean flag.
## Key Concepts Used

- While loop for continuous game control
- List mutation for updating guessed letters
- For-loop iteration over word positions
- Conditional branching for flow control
- Boolean flags for state termination
## Reflection

What I learned:

- How to structure a small project
- How to control program state
- Why mutable vs immutable matters
- How flow control determines program behavior

What I struggled with:

- Managing loop termination
- Handling repeated guesses
## Possible Improvements

- Track guessed letters
- Input validation
- Refactor into functions
- Separate logic from UI
