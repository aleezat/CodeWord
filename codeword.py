# Aleeza Freshman Project
import random
games_played = 0 
games_won = 0
total_guesses = 0
current_streak = 0
best_streak = 0
words = ["ARRAY", "ERROR", "CLASS", "LOOPS", "BYTES",
         "STACK", "QUEUE", "DEBUG", "INPUT", "PRINT",
         "FLOAT", "LOGIC", "INDEX", "CACHE", "PARSE",
         "TOKEN", "WHILE", "MERGE", "BREAK", "VALUE",
         "TRACE", "SCOPE", "NODES", "GRAPH", "BLOCK",
         "EVENT", "FILES", "FINAL", "SHORT"]
definitions = {
    "ARRAY": "A collection of values stored in order.",
    "ERROR": "A problem that occurs while a program is running.",
    "CLASS": "A blueprint used to create objects in programming.",
    "LOOPS": "A way to repeat a section of code.",
    "BYTES": "A unit used to store digital data.",
    "STACK": "A data structure that follows last in, first out.",
    "QUEUE": "A data structure that follows first in, first out.",
    "DEBUG": "The process of finding and fixing problems in code.",
    "INPUT": "Data given to a program.",
    "PRINT": "A command used to display information.",
    "FLOAT": "A number that can contain a decimal.",
    "LOGIC": "Rules used to make decisions in a program.",
    "INDEX": "A position used to access an item in a sequence.",
    "CACHE": "Stored data that helps a computer access information faster.",
    "PARSE": "To analyze information so a program can understand it.",
    "TOKEN": "A small piece of information used by a programming language.",
    "WHILE": "A loop that repeats while a condition is true.",
    "MERGE": "To combine two things into one.",
    "BREAK": "A command used to stop a loop.",
    "VALUE": "The actual data stored in a variable.",
    "TRACE": "To follow the steps of a program to understand what it does.",
    "SCOPE": "The part of a program where a variable can be accessed.",
    "NODES": "Individual elements in a data structure such as a graph.",
    "GRAPH": "A data structure made of connected nodes.",
    "BLOCK": "A group of code treated as one section.",
    "EVENT": "An action that a program can respond to.",
    "FILES": "Collections of data stored on a computer.",
    "FINAL": "A keyword or concept used to indicate something should not change.",
    "SHORT": "A data type used for smaller integer values in some languages."
}
hints = {
    "ARRAY": "A group of values stored in order.",
    "ERROR": "Something went wrong in a program.",
    "CLASS": "A blueprint for creating objects.",
    "LOOPS": "Used to repeat code.",
    "BYTES": "A unit of digital data.",
    "STACK": "A data structure where the last item added is removed first.",
    "QUEUE": "A data structure where the first item added is removed first.",
    "DEBUG": "Finding and fixing problems in code.",
    "INPUT": "Information given to a program.",
    "PRINT": "Used to display information.",
    "FLOAT": "A number that can have a decimal.",
    "LOGIC": "Rules used to make decisions.",
    "INDEX": "A position used to access an item.",
    "CACHE": "Stored information that helps data load faster.",
    "PARSE": "To analyze information so a program can understand it.",
    "TOKEN": "A small piece of a program or command.",
    "WHILE": "A loop that runs while a condition is true.",
    "MERGE": "To combine two things together.",
    "BREAK": "Used to stop a loop.",
    "VALUE": "The data stored in a variable.",
    "TRACE": "Following the steps of a program.",
    "SCOPE": "Where a variable can be accessed.",
    "NODES": "Individual points in a data structure.",
    "GRAPH": "A structure made of connected nodes.",
    "BLOCK": "A group of code treated as one section.",
    "EVENT": "An action that a program can respond to.",
    "FILES": "Collections of data stored on a computer.",
    "FINAL": "Something that is meant to stay unchanged.",
    "SHORT": "A type used for smaller integer values in some languages."
}
def show_instructions():
    print("Welcome to CodeWord!")
    print("Guess the 5-letter programming word.")
    print("You have 7 attempts.")
    print("You can use 1 hint per game.")    
    print("🟩 = correct letter and position")
    print("🟨 = correct letter, wrong position")
    print("⬜ = letter is not in the word")
def get_feedback(guess, secret_word):
    remaining = list(secret_word)
    feedback = ["⬜"] * len(secret_word)
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            feedback[i] = "🟩"
            remaining.remove(guess[i])
    for i in range(len(secret_word)):
        if feedback[i] == "⬜" and guess[i] in remaining:
            feedback[i] = "🟨"
            remaining.remove(guess[i])
    return feedback
def show_history(guesses, feedback_history):
    print("Guess history:")
    for i in range(len(guesses)):
        print(str(i + 1) + ".", guesses[i], end="  ")
        for j in range(len(feedback_history[i])):
            print(feedback_history[i][j], end=" ")
        print()
def show_stats():
    average_guesses = round(total_guesses / games_played, 2)
    win_rate = round((games_won / games_played) * 100)

    print("--- Stats ---")
    print("Games played:", games_played)
    print("Games won:", games_won)
    print("Win rate:", win_rate, "%")
    print("Average guesses:", average_guesses)
    print("Current streak:", current_streak)
    print("Best streak:", best_streak)
def play_game():
    show_instructions()
    global games_played, games_won, total_guesses
    global current_streak, best_streak
    count = 0
    won = False
    hint_used = False
    guesses = []
    feedback_history = []
    secret_word = random.choice(words)
    while count < 7:
        guess = input("Guess the programming word: ").upper()
        if guess == "HINT":
            if hint_used:
                print("You already used your hint!")
            else:
                print("Hint:", hints[secret_word])
                hint_used = True
            continue
        if len(guess) != 5:
            print("Your guess must be 5 letters!")
            continue
        if guess in guesses:
            print("You already guessed that word!")
            continue
        guesses.append(guess)
        count += 1
        feedback = get_feedback(guess, secret_word)
        feedback_history.append(feedback)
        show_history(guesses, feedback_history)
        if guess == secret_word:
            print("You got it!")
            print("Definition:", definitions[secret_word])
            won = True
            break
        else:
            print("Not quite!")
        if count == 7:
            print("Game over!")
            print("The word was:", secret_word)
            print("Definition:", definitions[secret_word])
    games_played += 1
    total_guesses += count
    if won:
        games_won += 1
        current_streak += 1
        if current_streak > best_streak:
            best_streak = current_streak
    else:
        current_streak = 0
    show_stats()
while True:
    play_game()
    again = input("Play again? (yes/no): ").upper()
    if again != "YES":
        break