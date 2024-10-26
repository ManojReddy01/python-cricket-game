import random

#generate a random target within a specified range
target = random.randint(1, 200)
print("TARGET:", target)
#write the valid input
while True:
    try:
        balls = int(input("GUESS THE NUMBER OF BALLS TO REACH THE TARGET (1 to 120): "))
        if balls < 1 or balls > 120:
            print("Please enter a number within the range of 1 to 120.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

#variables for the game
total_score = 0
dots = ones = twos = threes = fours = sixes = 0
balls_played = 0  # Track the number of balls actually played

#count each ball
for i in range(balls):
    number = random.choice([0, 1, 2, 3, 4, 6])
    total_score += number
    balls_played += 1

    # Count occurrences of each score type
    if number == 0:
        dots += 1
    elif number == 1:
        ones += 1
    elif number == 2:
        twos += 1
    elif number == 3:
        threes += 1
    elif number == 4:
        fours += 1
    elif number == 6:
        sixes += 1

    #stopping
    if total_score >= target:
        break

# Display the final score and overs played
print("YOUR SCORE IS:", total_score)
overs_played = balls_played // 6
balls_played_in_current_over = balls_played % 6
print(f"YOU PLAYED {overs_played}.{balls_played_in_current_over} OVERS")

#outcomes of the match
if total_score > target:
    print("YOU WON THE GAME")
elif total_score < target:
    print("YOU LOST THE GAME")
    print("YOU LOST THE MATCH BY", target - total_score, "runs")
else:
    print("THE MATCH GOT TIED")

#statistics
print("NO OF DOTS:", dots)
print("NO OF SINGLES:", ones)
print("NO OF TWOS:", twos)
print("NO OF THREES:", threes)
print("NO OF BOUNDARIES:", fours)
print("NO OF SIXES:", sixes)

#actual balls
print("TOTAL BALLS NEEDED TO REACH TARGET:", balls_played)
