def solution(k, score):
    answer = []
    min_score=2000
    honor=[]
    if len(score)<k:
        for i in range(len(score)):
            min_score = min(min_score, score[i])
            answer.append(min_score)
        return answer
    for i in range(k):
        min_score=min(min_score,score[i])
        answer.append(min_score)
        honor.append(score[i])
    for i in range(k,len(score)):
        honor.append(score[i])
        honor.sort()
        honor.pop(0)
        answer.append(honor[0])
    return answer

print(solution(3,	[10, 100, 20, 150, 1, 100, 200]))