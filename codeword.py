# Aleeza Freshman Project
import random
import os
# Game statistics
games_played = 0
games_won = 0
total_guesses = 0
current_streak = 0
best_streak = 0
total_score = 0
# Load saved statistics
if os.path.exists("codeword_stats.txt"):
    with open("codeword_stats.txt", "r") as file:
        data = file.readlines()
        if len(data) > 0:
            games_played = int(data[0])
        if len(data) > 1:
            games_won = int(data[1])
        if len(data) > 2:
            total_guesses = int(data[2])
        if len(data) > 3:
            best_streak = int(data[3])
        if len(data) > 4:
            current_streak = int(data[4])
        if len(data) > 5:
            total_score = int(data[5])
# Programming words
words = ["ARRAY", "ERROR", "CLASS", "LOOPS", "BYTES",
    "STACK", "QUEUE", "DEBUG", "INPUT", "PRINT",
    "FLOAT", "LOGIC", "INDEX", "CACHE", "PARSE",
    "TOKEN"]
# Word definitions
definitions = { "ARRAY": "A collection of values stored together.",
    "ERROR": "A mistake in a program that causes a problem.",
    "CLASS": "A blueprint used to create objects in programming.",
    "LOOPS": "Code that repeats instructions.",
    "BYTES": "A unit of digital information.",
    "STACK": "A data structure that follows Last In, First Out.",
    "QUEUE": "A data structure that follows First In, First Out.",
    "DEBUG": "Finding and fixing errors in code.",
    "INPUT": "Data entered into a program.",
    "PRINT": "A command that displays information.",
    "FLOAT": "A number that contains a decimal.",
    "LOGIC": "Rules used to make decisions in a program.",
    "INDEX": "A position of an item in a sequence.",
    "CACHE": "Temporary storage used for faster access.",
    "PARSE": "To analyze and interpret data or code.",
    "TOKEN": "A meaningful unit of code or text." }
# Hints
hints = { "ARRAY": "Stores multiple values in one variable.",
    "ERROR": "Something went wrong in your code.",
    "CLASS": "Used in object-oriented programming.",
    "LOOPS": "Repeats code.",
    "BYTES": "Related to digital storage.",
    "STACK": "Think of a pile of plates.",
    "QUEUE": "Think of a line of people waiting.",
    "DEBUG": "What programmers do when code fails.",
    "INPUT": "Information given to a program.",
    "PRINT": "Displays output in Python.",
    "FLOAT": "A Python data type for decimals.",
    "LOGIC": "Used with AND, OR, and NOT.",
    "INDEX": "Tells you an item's position.",
    "CACHE": "Helps computers access data faster.",
    "PARSE": "Breaks down and analyzes information.",
    "TOKEN": "A small meaningful piece of code." }
def show_instructions():
    print("\n========== CODEWORD ==========")
    print("Guess the hidden 5-letter programming word.")
    print("Green = Correct letter and position.")
    print("Yellow = Correct letter, wrong position.")
    print("White = Letter is not in the word.")
    print("You can ask for one hint per game.")
    print("Hints do not use an attempt.")
    print("Good luck!\n")
def get_feedback(guess, target):
    feedback = ["⬜"] * 5
    remaining = list(target)
    # Find correct letters in correct positions
    for i in range(5):
        if guess[i] == target[i]:
            feedback[i] = "🟩"
            remaining[i] = None
    # Find correct letters in wrong positions
    for i in range(5):
        if feedback[i] != "🟩" and guess[i] in remaining:
            feedback[i] = "🟨"
            remaining.remove(guess[i])
    return "".join(feedback)
def show_history(guesses, feedback_history):
    print("\n========== GUESS HISTORY ==========")
    for i in range(len(guesses)):
        print(guesses[i], feedback_history[i])
def show_stats():
    print("\n========== YOUR STATISTICS ==========")
    print("Games played:", games_played)
    print("Games won:", games_won)
    print("Total score:", total_score)
    if games_played > 0:
        win_rate = round((games_won / games_played) * 100, 2)
        average_guesses = round(total_guesses / games_played, 2)
        print("Win rate:", str(win_rate) + "%")
        print("Average guesses:", average_guesses)
    print("Current streak:", current_streak)
    print("Best streak:", best_streak)
    print("====================================")
def play_game():
    global games_played, games_won, total_guesses
    global current_streak, best_streak, total_score
    show_instructions()
    # Choose difficulty
    while True:
        difficulty = input(
            "Choose difficulty (Easy, Medium, Hard): "
        ).upper()
        if difficulty == "EASY":
            max_attempts = 7
            points = 70
            break
        elif difficulty == "MEDIUM":
            max_attempts = 6
            points = 100
            break
        elif difficulty == "HARD":
            max_attempts = 5
            points = 150
            break
        else:
            print("Invalid difficulty. Please try again.")
    target = random.choice(words)
    guesses = []
    feedback_history = []
    count = 0
    hint_used = False
    won = False
    print("\nDifficulty:", difficulty)
    print("You have", max_attempts, "attempts.")
    print("Type HINT to reveal a clue.\n")
    while count < max_attempts:
        guess = input("Enter your 5-letter guess: ").upper()
        # Hint system
        if guess == "HINT":
            if not hint_used:
                print("Hint:", hints[target])
                hint_used = True
            else:
                print("You already used your hint.")
            continue
        # Validate guess length
        if len(guess) != 5:
            print("Your guess must be exactly 5 letters.")
            continue
        # Prevent repeated guesses
        if guess in guesses:
            print("You already guessed that word.")
            continue
        # Count valid guesses
        count += 1
        guesses.append(guess)
        feedback = get_feedback(guess, target)
        feedback_history.append(feedback)
        print(feedback)
        print("Attempts remaining:", max_attempts - count)
        if guess == target:
            won = True
            print("\nCorrect! You guessed the word!")
            break
    # Show results
    show_history(guesses, feedback_history)
    if won:
        print("\nYou won!")
        print("Definition:", definitions[target])
        bonus = (max_attempts - count) * 10
        score_earned = points + bonus
        print("Base points:", points)
        print("Bonus points:", bonus)
        print("Points earned:", score_earned)
        total_score += score_earned
    else:
        print("\nGame over!")
        print("The correct word was:", target)
        print("Definition:", definitions[target])
        print("No points earned this game.")
    # Update statistics
    games_played += 1
    total_guesses += count
    if won:
        games_won += 1
        current_streak += 1
        if current_streak > best_streak:
            best_streak = current_streak
    else:
        current_streak = 0
    # Save statistics
    with open("codeword_stats.txt", "w") as file:
        file.write(str(games_played) + "\n")
        file.write(str(games_won) + "\n")
        file.write(str(total_guesses) + "\n")
        file.write(str(best_streak) + "\n")
        file.write(str(current_streak) + "\n")
        file.write(str(total_score) + "\n")
    show_stats()
# Main game loop
while True:
    play_game()
    again = input("\nWould you like to play again? (Yes/No): ").upper()
    if again != "YES":
        print("\nThanks for playing CodeWord!")
        break