# CodeWord

CodeWord is a Python-based Wordle-style guessing game focused on programming-related words.

The player tries to guess a randomly selected 5-letter programming word within a limited number of attempts. The game includes three difficulty levels, a hint system, color-coded feedback, a scoring system, and saved statistics.

## Features

- Randomly selects a 5-letter programming word
- Offers three difficulty levels:
  - Easy: 7 attempts, 70 base points
  - Medium: 6 attempts, 100 base points
  - Hard: 5 attempts, 150 base points
- Accepts case-insensitive guesses
- Checks that guesses contain exactly 5 letters
- Prevents duplicate guesses
- Provides Wordle-style letter feedback:
  - 🟩 Correct letter and position
  - 🟨 Correct letter, wrong position
  - ⬜ Letter is not in the word
- Displays guess history during the game
- Allows one hint per game
- Provides programming word definitions after winning or losing
- Awards bonus points for unused attempts
- Tracks total score
- Tracks games played and games won
- Calculates win rate
- Calculates average guesses per game
- Tracks current winning streak
- Tracks best winning streak
- Saves statistics between program sessions using a text file
- Allows the player to start another game

## Programming Concepts Used

This project helped me practice:

- Functions
- `while` loops
- `for` loops
- Lists
- Dictionaries
- Conditionals
- Nested conditionals
- User input
- String methods
- String indexing
- `random.choice()`
- Global variables
- Returning values from functions
- File handling
- Reading and writing text files
- `os.path.exists()`
- Score calculations
- Basic game statistics

## How It Works

1. The program displays the game instructions.
2. The player chooses a difficulty level: Easy, Medium, or Hard.
3. The program randomly selects a programming word.
4. The player enters a 5-letter guess.
5. The program checks whether the guess is valid and has not already been used.
6. The player can type `HINT` to receive a clue without using an attempt.
7. Each letter is compared with the secret word.
8. The program displays feedback using 🟩, 🟨, and ⬜.
9. The player's guesses and feedback are displayed as guess history.
10. The game ends when the player guesses the word or uses all available attempts.
11. The definition of the secret word is displayed.
12. Points are awarded for winning, with bonus points for unused attempts.
13. Game statistics, including total score, win rate, average guesses, and streaks, are updated.
14. Statistics are saved to `codeword_stats.txt` so they can be loaded the next time the program runs.
15. The player can choose to play another game.

## Example Words

The current word list includes programming-related words such as:

`ARRAY`, `ERROR`, `CLASS`, `LOOPS`, `BYTES`, `STACK`, `QUEUE`, `DEBUG`, `INPUT`, `PRINT`, `FLOAT`, `LOGIC`, `INDEX`, `CACHE`, `PARSE`, and `TOKEN`.

## Technologies

- Python
- Python `random` module
- Python `os` module
- Text file storage

## What I Learned

Through this project, I practiced building an interactive program from scratch and gradually adding new features.

I learned how to organize code into reusable functions, use lists and dictionaries to manage game information, validate user input, compare strings and individual characters, and use conditionals to control gameplay.

I also learned how to implement a scoring system, read and write text files, and save statistics between program sessions. This project helped me improve my problem-solving skills and understand how different Python concepts work together in a larger program.

## Future Improvements

Some features I may add in the future include:

- Adding more programming-related words
- Expanding the word list
- Improving the user interface
- Adding more detailed feedback
- Displaying a leaderboard
- Improving input validation to accept only words from the programming word list
- Adding a graphical interface
