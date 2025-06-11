import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True: #input number of players you want
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number between 2 and 4")
    else:
            print("Invalid, try again please.")

max_score = 50 #score cap
player_scores = [0 for _ in range(players)] #to generate an empty list for storing scores

while max(player_scores) < max_score: #simulate the turns

    for player_idx in range(players):
        print("\nPlayer #", player_idx +1, "turn has just started.")
        print("Your total score is:",player_scores[player_idx], "\n")
        current_score = 0 #keeps track

        while True: #simulate the turn
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your current score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:",player_scores[player_idx])
max_score = max(player_scores)
player_winning_idx = player_scores.index(max_score)
print("Player number", player_winning_idx+1, "is the winner with a score of:", max_score)