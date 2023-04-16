def solution(n, m, section):
    paint=section[0]-1
    answer = 0
    for v in section:
        if paint<v:
            answer+=1
            paint=v+m-1

    return answer
