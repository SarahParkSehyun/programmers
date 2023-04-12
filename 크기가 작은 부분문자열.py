def solution(t, p):
    answer = 0
    n=len(p)
    for i in range(len(t)-n+1):
        sliced_lst=t[i:i+3]
        s=""
        for j in range(n):
            s+=str(sliced_lst[j])
            int(s)
        print(s)
        if s<=p:
            answer+=1
    return answer

print(solution("10203","15"))