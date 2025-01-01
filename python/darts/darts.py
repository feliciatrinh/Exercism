def score(x, y):
    distance_squared = x**2 + y**2
    if distance_squared <= 1:
        score = 10
    elif distance_squared <= 25:
        score = 5
    elif distance_squared <= 100:
        score = 1
    else:
        score = 0
    return score
