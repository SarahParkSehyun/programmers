def solution(t, p):
    answer = 0
    n=len(p)
    for i in range(len(t)-n+1):
        sliced_lst=t[i:i+n]
        if int(sliced_lst)<=int(p):
            answer+=1
    return answer

print(solution("10203","15"))