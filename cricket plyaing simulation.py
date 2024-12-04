import random
import json

def get_player_name():
    return input("ENTER PLAYER NAME: ").strip()

def get_match_type():
    print("\nCHOOSE MATCH TYPE:")
    print("1. T20 (20 Overs)")
    print("2. ODI (50 Overs)")
    print("3. Test Match (Unlimited Overs)")
    while True:
        try:
            choice = int(input("ENTER YOUR CHOICE (1-3): "))
            if choice in [1, 2, 3]:
                return [120, 300, float('inf')][choice - 1]
            else:
                print("Please choose a valid match type.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

def get_pitch_condition():
    print("\nSELECT PITCH CONDITION:")
    print("1. Flat (High Scoring)")
    print("2. Green (Balanced)")
    print("3. Dry (Low Scoring)")
    while True:
        try:
            choice = int(input("ENTER YOUR CHOICE (1-3): "))
            if choice in [1, 2, 3]:
                return ["Flat", "Green", "Dry"][choice - 1]
            else:
                print("Please choose a valid pitch condition.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

def scoring_weights(pitch, match_overs):
    if match_overs == 120:
        if pitch == "Flat":
            return [20, 30, 35, 25, 30, 15, 10]
        elif pitch == "Green":
            return [25, 35, 30, 30, 25, 15 ,12]
        else:
            return [30, 40, 35, 25, 20, 10, 8]
    elif match_overs == 300:
        if pitch == "Flat":
            return [15, 25, 30, 20, 25, 10, 5]
        elif pitch == "Green":
            return [20, 30, 25, 25, 20, 10, 12]
        else:
            return [25, 35, 30, 20, 15, 5, 12]
    else:
        if pitch == "Flat":
            return [10, 20, 25, 15, 20, 5, 5]
        elif pitch == "Green":
            return [15, 25, 20, 20, 15, 5, 5]
        else:
            return [20, 30, 25, 15, 10, 0, 5]

def cricket_game():
    match_overs = get_match_type()
    pitch = get_pitch_condition()
    player_name = get_player_name()

    if match_overs == 120:
        target = random.randint(50, 200)
    elif match_overs == 300:
        target = random.randint(75, 425)
    else:
        target = random.randint(100, 750)

    print(f"\nTARGET SET: {target} RUNS")
    print(f"MATCH TYPE: {'Unlimited Overs' if match_overs == float('inf') else match_overs // 6} OVERS")
    print(f"PITCH CONDITION: {pitch}\n")
    
    total_score = 0
    balls_played = 0
    wickets = 0
    max_wickets = 10

    scoring_probs = scoring_weights(pitch, match_overs)

    commentary = {
        0: ["Dot ball! Excellent delivery.", "No runs scored.", "Defended well."],
        1: ["Quick single!", "Good running between the wickets.", "One run taken."],
        2: ["Nicely placed for two.", "Great running! Two runs added.", "Well played, two runs."],
        3: ["Brilliant running! Three runs.", "Fielders under pressure, it's three runs."],
        4: ["That's a boundary!", "Crisp shot, four runs!", "What a shot, it's a four!"],
        6: ["SIX! That's massive!", "Out of the park, six runs!", "Huge hit for a six!"],
        "OUT": ["That's a wicket!", "Caught! The batsman is out.", "Bowled! Cleaned up."]
    }

    player_runs = {player_name: 0}
    
    while wickets < max_wickets and balls_played < match_overs:
        outcome = random.choices([0, 1, 2, 3, 4, 6, "OUT"], weights=scoring_probs)[0]
        balls_played += 1

        if outcome == "OUT":
            wickets += 1
            print(random.choice(commentary["OUT"]))
            if wickets < max_wickets:  # Only ask for new player if there are wickets left
                new_player = get_player_name()
                player_runs[new_player] = 0
                player_name = new_player
        else:
            player_runs[player_name] += outcome
            total_score += outcome
            print(random.choice(commentary[outcome]))

        # Check for win condition
        if total_score >= target:
            print("\nYOU WON THE GAME!")
            break

    overs_played = balls_played // 6
    balls_in_current_over = balls_played % 6
    print("\nMATCH SUMMARY:")
    print(f"TARGET: {target} RUNS")
    print(f"FINAL SCORE: {total_score}/{wickets}")
    print(f"OVERS PLAYED: {overs_played}.{balls_in_current_over}")
    
    print("\nINDIVIDUAL PLAYER SCORES:")
    for player, runs in player_runs.items():
        print(f"{player}: {runs} runs")
    
    if total_score < target:
        print(f"YOU LOST THE GAME BY {target - total_score} RUNS.")
    elif total_score == target-1:
        print("THE MATCH ENDED IN A TIE!")
    elif total_score > target:
        print("YOU WON THE MATCH! CONGRATULATIONS!!")
    game_data = {
        "target": target,
        "score": total_score,
        "wickets": wickets,
        "overs_played": f"{overs_played}.{balls_in_current_over}",
        "result": "WON" if total_score >= target else "LOST" if total_score < target else "TIED",
        "player_scores": player_runs
    }

    with open("advanced_game_state.json", "w") as file:
        json.dump(game_data, file, indent=4)
    
    print("\nGAME DATA SAVED TO 'advanced_game_state.json'")

# Run the game
cricket_game()
