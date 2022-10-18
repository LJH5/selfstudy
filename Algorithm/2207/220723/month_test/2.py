score_list = [100, 70, 90, 50]

def over(score_list):
    count = 0
    for score in score_list:
        if score >= 60:
            count += 1
    return count

print(over(score_list))