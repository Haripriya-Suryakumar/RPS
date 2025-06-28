def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        return "R"
    last_five = opponent_history[-5:]
    most_common = max(set(last_five), key=last_five.count)

    if most_common == "R":
        return "P"
    elif most_common == "P":
        return "S"
    else:
        return "R"
