def solution(targets):
    answer = 1
    targets.sort(key=lambda x:(x[1],x[0]))
    location=targets[0][1]-1
    for i in range(1,len(targets)):
        if targets[i][0]>location:
            answer+=1
            location=targets[i][1]-1
    return answer


print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))