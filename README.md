# CodeWord

CodeWord is a Python-based Wordle-style guessing game focused on programming-related words.

The player has **7 attempts** to guess a randomly selected 5-letter programming word. After each valid guess, the game provides feedback using colored emojis to show which letters are correct, misplaced, or not included in the word.

## Features

* Randomly selects a 5-letter programming word
* Gives the player 7 attempts per game
* Accepts case-insensitive guesses
* Checks that guesses contain exactly 5 letters
* Prevents duplicate guesses
* Provides Wordle-style letter feedback:

  * 🟩 Correct letter and position
  * 🟨 Correct letter, wrong position
  * ⬜ Letter is not in the word
* Displays guess history during the game
* Tracks games played and games won
* Calculates win rate
* Calculates average guesses per game
* Tracks current winning streak
* Tracks best winning streak
* Allows the player to start another game

## Programming Concepts Used

This project helped me practice:

* Functions
* `while` loops
* `for` loops
* Lists
* Conditionals
* User input
* String methods
* String indexing
* `random.choice()`
* Global variables
* Basic game statistics

## How It Works

1. The program randomly chooses a programming word from a list.
2. The player enters a 5-letter guess.
3. The program checks whether the guess is valid and has not already been used.
4. Each letter is compared with the secret word.
5. The program displays feedback using 🟩, 🟨, and ⬜.
6. The player's guesses and feedback are saved and displayed as guess history.
7. The game ends when the player guesses the word or uses all 7 attempts.
8. After the game, statistics such as win rate, average guesses, and streaks are displayed.
9. The player can choose to play another game.

## Example Words

The current word list includes programming-related words such as:

`ARRAY`, `ERROR`, `CLASS`, `LOOPS`, `BYTES`, `STACK`, `QUEUE`, `DEBUG`, `INPUT`, `PRINT`, `FLOAT`, `LOGIC`, `INDEX`, `CACHE`, `PARSE`, and `TOKEN`.

## Technologies

* Python
* Python `random` module

## What I Learned

Through this project, I practiced building a small interactive program from scratch. I learned how to organize code into functions, use loops and lists to manage game information, validate user input, compare strings and individual characters, and keep track of statistics across multiple games.

## Future Improvements

Some features I may add in the future include:

* Adding more programming-related words
* Adding difficulty levels
* Adding a larger word list
* Improving the user interface
* Adding more detailed feedback
* Saving statistics between program sessions
* Adding a graphical interface
