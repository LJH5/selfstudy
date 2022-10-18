score_list = [100, 70, 90, 50]

def max_score(score_list):
    max_sc = 0
    for score in score_list:
        if score > max_sc:
            max_sc = score
    return max_sc