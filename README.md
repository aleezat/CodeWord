# CodeWord

CodeWord is a Python-based Wordle-style guessing game focused on programming-related words.

The player tries to guess a randomly selected 5-letter programming word within a limited number of attempts. The game includes three difficulty levels, a hint system, color-coded feedback, a scoring system, player statistics, and a leaderboard.

## Features

- Randomly selects a 5-letter programming word
- Allows the player to enter their name
- Offers three difficulty levels:
  - Easy: 7 attempts, 70 base points
  - Medium: 6 attempts, 100 base points
  - Hard: 5 attempts, 150 base points
- Provides color-coded feedback for each guess:
  - 🟩 Correct letter and position
  - 🟨 Correct letter, wrong position
  - ⬜ Letter not included in the word
- Allows one hint per game without using an attempt
- Displays guess history
- Reveals the programming word's definition after the game
- Awards bonus points for unused attempts when the player wins
- Tracks games played and games won
- Calculates win rate and average guesses
- Tracks current and best winning streaks
- Tracks total score
- Displays a leaderboard of the top five winning scores
- Validates player names and difficulty selections
- Prevents repeated guesses
- Allows the player to replay the game

## Programming Concepts Used

- Functions
- Variables and data types
- Lists and dictionaries
- `while` and `for` loops
- Conditional statements (`if`, `elif`, and `else`)
- Nested conditionals
- User input and input validation
- String methods and indexing
- Random selection using `random.choice()`
- Returning values from functions
- Global variables
- List sorting
- Duplicate-letter handling
- Score calculations
- Basic statistics

## How It Works

1. The player enters their name.
2. The game displays the instructions.
3. The player selects a difficulty level.
4. The program randomly selects a programming word.
5. The player enters a 5-letter guess.
6. The game displays feedback showing which letters are correct or misplaced.
7. The player can request one hint without losing an attempt.
8. The game ends when the player guesses the word or runs out of attempts.
9. The program reveals the word's definition and displays the game statistics.
10. Winning scores are added to the leaderboard.
11. The player can choose to play again.

## Example Words

The current word list includes:

`ARRAY`, `ERROR`, `CLASS`, `LOOPS`, `BYTES`, `STACK`, `QUEUE`, `DEBUG`, `INPUT`, `PRINT`, `FLOAT`, `LOGIC`, `INDEX`, `CACHE`, `PARSE`, and `TOKEN`.

## Technologies

- Python
- Python `random` module

## Future Improvements

- Add more programming-related words
- Validate guesses against the programming word list
- Save statistics and leaderboard scores between sessions
- Store cumulative scores for individual players
