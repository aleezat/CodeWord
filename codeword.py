# Aleeza Freshman Project
import random
games_played = 0 
games_won = 0
total_guesses = 0
current_streak = 0
best_streak = 0
words = ["ARRAY", "ERROR", "CLASS", "LOOPS", "BYTES","STACK", "QUEUE", "DEBUG", "INPUT", "PRINT","FLOAT", "LOGIC", "INDEX", "CACHE", "PARSE", "TOKEN", "WHILE","MERGE", "BREAK", "VALUE", "TRACE", "SCOPE", "NODES", "GRAPH","BLOCK", "EVENT", "FILES", "FINAL", "SHORT"]
def play_game():
    print("Welcome to CodeWord!")
    print("Guess the 5-letter programming word.")
    print("You have 7 attempts.")
    print("🟩 = correct letter and position")
    print("🟨 = correct letter, wrong position")
    print("⬜ = letter is not in the word")
    global games_played, games_won, total_guesses, current_streak, best_streak
    count = 0
    won = False
    guesses = []
    feedback_history = []
    secret_word = random.choice(words)
    while count < 7:
        guess = input("Guess the programming word: ").upper()
        if len(guess) != 5:
            print("Your guess must be 5 letters!")
            continue
        if guess in guesses:
            print("You already guessed that word!")
            continue
        guesses.append(guess)
        count += 1
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
        feedback_history.append(feedback)
        print("Guess history:")
        for i in range(len(guesses)):
            print(i + 1, ".", guesses[i], end=" ")
            for j in range(len(feedback_history[i])):
                print(feedback_history[i][j], end=" ")
            print()
        if guess == secret_word:
            print("You got it!")
            won = True
            break
        else:
            print("Not quite!")
        if count == 7:
            print("Game over!")
            print("The word was:", secret_word)
    games_played += 1
    total_guesses += count
    if won:
        games_won += 1
        current_streak += 1
        if current_streak > best_streak:
            best_streak = current_streak
    else:
        current_streak = 0
    average_guesses = round(total_guesses / games_played, 2)
    win_rate = round((games_won / games_played) * 100)
    print("Games played:", games_played)
    print("Games won:", games_won)
    print("Win rate:", win_rate, "%")
    print("Average guesses:", average_guesses)
    print("Current streak:", current_streak)
    print("Best streak:", best_streak)
while True:
    play_game()
    again = input("Play again? (yes/no): ").upper()
    if again != "YES":
        break