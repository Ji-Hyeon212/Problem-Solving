def solution(answers):
    scores = [0, 0, 0]
    best_scores = []
    m1 = [1,2,3,4,5]
    m2 = [2,1,2,3,2,4,2,5]
    m3 = [3,3,1,1,2,2,4,4,5,5]
    for i, ans in enumerate(answers):
        if ans == m1[i%len(m1)]:
            scores[0]+=1
        if ans == m2[i%len(m2)]:
            scores[1]+=1
        if ans == m3[i%len(m3)]:
            scores[2]+=1
    best = max(scores)
    for i, s in enumerate(scores):
        if s == best:
            best_scores.append(i+1)
    return best_scores