# CodeWord

CodeWord is a Python-based Wordle-style guessing game focused on programming-related words.

The player has **7 attempts** to guess a randomly selected 5-letter programming word. After each valid guess, the game provides feedback using colored emojis to show which letters are correct, misplaced, or not included in the word. Players can also use **one hint per game** and learn the definition of the word after the game ends.

## Features

- Randomly selects a 5-letter programming word
- Gives the player 7 attempts per game
- Accepts case-insensitive guesses
- Checks that guesses contain exactly 5 letters
- Prevents duplicate guesses
- Provides Wordle-style letter feedback:
  - 🟩 Correct letter and position
  - 🟨 Correct letter, wrong position
  - ⬜ Letter is not in the word
- Displays guess history during the game
- Allows the player to use one hint per game
- Displays a hint based on the secret word
- Shows the word's definition after winning or losing
- Tracks games played and games won
- Calculates win rate
- Calculates average guesses per game
- Tracks current winning streak
- Tracks best winning streak
- Allows the player to start another game

## Programming Concepts Used

This project helped me practice:

- Functions
- `while` loops
- `for` loops
- Lists
- Dictionaries
- Conditionals
- User input
- String methods
- String indexing
- `random.choice()`
- Global variables
- Returning values from functions
- Basic game statistics

## How It Works

1. The program randomly chooses a programming word from a list.
2. The player enters a 5-letter guess.
3. The program checks whether the guess is valid and has not already been used.
4. The player can type `HINT` to receive a clue about the secret word.
5. Each letter is compared with the secret word.
6. The program displays feedback using 🟩, 🟨, and ⬜.
7. The player's guesses and feedback are saved and displayed as guess history.
8. The game ends when the player guesses the word or uses all 7 attempts.
9. The definition of the secret word is displayed after the game ends.
10. Statistics such as win rate, average guesses, and streaks are displayed.
11. The player can choose to play another game.

## Example Words

The current word list includes programming-related words such as:

`ARRAY`, `ERROR`, `CLASS`, `LOOPS`, `BYTES`, `STACK`, `QUEUE`, `DEBUG`, `INPUT`, `PRINT`, `FLOAT`, `LOGIC`, `INDEX`, `CACHE`, `PARSE`, and `TOKEN`.

## Technologies

- Python
- Python `random` module

## What I Learned

Through this project, I practiced building an interactive program from scratch. I learned how to organize code into smaller functions, use loops and lists to manage game information, use dictionaries to store hints and definitions, validate user input, compare strings and individual characters, and keep track of statistics across multiple games.

I also improved the organization and readability of my code by separating different parts of the game into reusable functions.

## Future Improvements

Some features I may add in the future include:

- Adding more programming-related words
- Adding difficulty levels
- Adding a larger word list
- Improving the user interface
- Adding more detailed feedback
- Saving statistics between program sessions
- Adding a graphical interface
- Improving input validation to accept only words from the programming word list
