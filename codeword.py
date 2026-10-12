
# Aleeza Freshman Project
import random


# -------------------------
# PLAYER NAME
# -------------------------

player_name = input("Enter your player name: ").strip()

while player_name == "":
    player_name = input("Name cannot be empty. Enter your name: ").strip()

print("\nWelcome,", player_name + "!")


# -------------------------
# GAME STATISTICS
# -------------------------

games_played = 0
games_won = 0
total_guesses = 0
current_streak = 0
best_streak = 0
total_score = 0


# -------------------------
# LEADERBOARD
# -------------------------

leaderboard_names = []
leaderboard_scores = []


# -------------------------
# PROGRAMMING WORDS
# -------------------------

words = {
    "ARRAY": {
        "definition": "A collection of values stored together.",
        "hint": "Think of a list."
    },

    "ERROR": {
        "definition": "A problem that occurs while a program runs or is written.",
        "hint": "Something went wrong."
    },

    "CLASS": {
        "definition": "A blueprint used to create objects.",
        "hint": "Used in object-oriented programming."
    },

    "LOOPS": {
        "definition": "Code that repeats a set of instructions.",
        "hint": "Used to repeat code."
    },

    "BYTES": {
        "definition": "A unit of digital information.",
        "hint": "Used to measure computer data."
    },

    "STACK": {
        "definition": "A data structure where the last item added is the first removed.",
        "hint": "Think LIFO."
    },

    "QUEUE": {
        "definition": "A data structure where the first item added is the first removed.",
        "hint": "Think of a line of people."
    },

    "DEBUG": {
        "definition": "The process of finding and fixing problems in code.",
        "hint": "Fixing problems in a program."
    },

    "INPUT": {
        "definition": "Information given to a computer or program.",
        "hint": "Something a user gives the program."
    },

    "PRINT": {
        "definition": "A command used to display information.",
        "hint": "Used to show something on the screen."
    },

    "FLOAT": {
        "definition": "A number that can contain a decimal.",
        "hint": "Example: 3.14."
    },

    "LOGIC": {
        "definition": "Rules used to make decisions in a program.",
        "hint": "Think TRUE and FALSE."
    },

    "INDEX": {
        "definition": "A position used to access an item in a sequence.",
        "hint": "Lists use positions to find items."
    },

    "CACHE": {
        "definition": "A small amount of fast storage used to keep frequently needed data.",
        "hint": "Helps a computer access data faster."
    },

    "PARSE": {
        "definition": "To analyze information so a computer can understand its structure.",
        "hint": "Breaking information into a useful structure."
    },

    "TOKEN": {
        "definition": "A small unit of information used when analyzing code or text.",
        "hint": "A piece of code or text."
    }
}


# -------------------------
# INSTRUCTIONS
# -------------------------

def show_instructions():

    print("\n========== CODEWORD ==========")
    print("Guess the hidden 5-letter programming word.")
    print("🟩 = Correct letter and position.")
    print("🟨 = Correct letter, wrong position.")
    print("⬜ = Letter is not in the word.")
    print("You can ask for one hint per game.")
    print("Hints do not use an attempt.")
    print("Good luck!\n")


# -------------------------
# GET WORD FEEDBACK
# -------------------------

def get_feedback(guess, target):

    feedback = ["⬜", "⬜", "⬜", "⬜", "⬜"]

    remaining = list(target)

    # Check correct letters in correct positions

    for i in range(5):

        if guess[i] == target[i]:

            feedback[i] = "🟩"
            remaining[i] = ""

    # Check correct letters in wrong positions

    for i in range(5):

        if feedback[i] == "⬜":

            for j in range(5):

                if guess[i] == remaining[j] and remaining[j] != "":

                    feedback[i] = "🟨"
                    remaining[j] = ""
                    break

    result = ""

    for i in range(5):
        result = result + feedback[i]

    return result


# -------------------------
# SHOW GUESS HISTORY
# -------------------------

def show_history(guesses, feedback_history):

    print("\n========== GUESS HISTORY ==========")

    for i in range(len(guesses)):

        print(guesses[i], feedback_history[i])


# -------------------------
# SHOW STATISTICS
# -------------------------

def show_stats():

    print("\n========== YOUR STATISTICS ==========")

    print("Games played:", games_played)
    print("Games won:", games_won)
    print("Total score:", total_score)

    if games_played > 0:

        win_rate = (games_won / games_played) * 100
        average_guesses = total_guesses / games_played

        print("Win rate:", round(win_rate, 2), "%")
        print("Average guesses:", round(average_guesses, 2))

    print("Current streak:", current_streak)
    print("Best streak:", best_streak)

    print("====================================")


# -------------------------
# SHOW LEADERBOARD
# -------------------------

def show_leaderboard():

    print("\n========== TOP 5 SCORES ==========")

    if len(leaderboard_scores) == 0:

        print("No scores yet!")

    else:

        # Sort scores from highest to lowest

        for i in range(len(leaderboard_scores)):

            for j in range(i + 1, len(leaderboard_scores)):

                if leaderboard_scores[j] > leaderboard_scores[i]:

                    # Swap scores

                    temporary_score = leaderboard_scores[i]
                    leaderboard_scores[i] = leaderboard_scores[j]
                    leaderboard_scores[j] = temporary_score

                    # Swap names

                    temporary_name = leaderboard_names[i]
                    leaderboard_names[i] = leaderboard_names[j]
                    leaderboard_names[j] = temporary_name

        # Show top 5

        number_to_show = len(leaderboard_scores)

        if number_to_show > 5:
            number_to_show = 5

        for i in range(number_to_show):

            print(
                str(i + 1) + ".",
                leaderboard_names[i],
                "-",
                leaderboard_scores[i],
                "points"
            )

    print("=================================")


# -------------------------
# PLAY GAME
# -------------------------

def play_game():

    global games_played
    global games_won
    global total_guesses
    global current_streak
    global best_streak
    global total_score

    show_instructions()

    # Choose difficulty

    while True:

        print("\nChoose difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        try:

            difficulty = int(input("Enter 1, 2, or 3: "))

            if difficulty == 1:

                difficulty_name = "EASY"
                max_attempts = 7
                points = 70
                break

            elif difficulty == 2:

                difficulty_name = "MEDIUM"
                max_attempts = 6
                points = 100
                break

            elif difficulty == 3:

                difficulty_name = "HARD"
                max_attempts = 5
                points = 150
                break

            else:

                print("Please enter 1, 2, or 3.")

        except ValueError:

            print("Please enter a number.")

    # Choose random word

    target = random.choice(list(words))

    guesses = []
    feedback_history = []

    count = 0
    hint_used = False
    won = False

    print("\nDifficulty:", difficulty_name)
    print("You have", max_attempts, "attempts.")
    print("Type HINT to reveal a clue.\n")

    # -------------------------
    # GUESSING LOOP
    # -------------------------

    while count < max_attempts:

        guess = input(
            "Enter your 5-letter guess: "
        ).strip().upper()

        # Hint system

        if guess == "HINT":

            if hint_used == False:

                print("Hint:", words[target]["hint"])
                hint_used = True

            else:

                print("You already used your hint.")

            continue

        # Check guess length

        if len(guess) != 5:

            print("Your guess must be exactly 5 letters.")
            continue

        # Check repeated guesses

        if guess in guesses:

            print("You already guessed that word.")
            continue

        # Count valid guess

        count += 1
        guesses.append(guess)

        # Get feedback

        feedback = get_feedback(guess, target)
        feedback_history.append(feedback)

        print(feedback)
        print("Attempts remaining:", max_attempts - count)

        # Check if player won

        if guess == target:

            won = True
            print("\nCorrect! You guessed the word!")
            break

    # -------------------------
    # SHOW RESULTS
    # -------------------------

    show_history(guesses, feedback_history)

    if won:

        print("\nYou won!")

        print(
            "Definition:",
            words[target]["definition"]
        )

        bonus = (max_attempts - count) * 10
        score_earned = points + bonus

        print("Base points:", points)
        print("Bonus points:", bonus)
        print("Points earned:", score_earned)

        total_score += score_earned

        # Add score to leaderboard

        leaderboard_names.append(player_name)
        leaderboard_scores.append(score_earned)

    else:

        print("\nGame over!")
        print("The correct word was:", target)

        print(
            "Definition:",
            words[target]["definition"]
        )

        print("No points earned this game.")

    # -------------------------
    # UPDATE STATISTICS
    # -------------------------

    games_played += 1
    total_guesses += count

    if won:

        games_won += 1
        current_streak += 1

        if current_streak > best_streak:
            best_streak = current_streak

    else:

        current_streak = 0

    # Show updated information

    show_stats()
    show_leaderboard()


# -------------------------
# MAIN GAME LOOP
# -------------------------

while True:

    play_game()

    again = input(
        "\nWould you like to play again? (Yes/No): "
    ).strip().upper()

    while again != "YES" and again != "NO":

        print("Please enter Yes or No.")

        again = input(
            "\nWould you like to play again? (Yes/No): "
        ).strip().upper()

    if again == "NO":

        print("\nThanks for playing CodeWord!")
        break
