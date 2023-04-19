def solution(k, m, score):
    answer = 0
    if len(score)<m:
        return 0
    score.sort(reverse=True)
    #print(score)
    i=0
    while len(score)-i>=m:
        answer+=score[i+m-1]
        i+=m
    return answer*m

print(solution(3,4,[1, 2, 3, 1, 2, 3, 1]))