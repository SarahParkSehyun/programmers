def solution(t, p):
    answer = 0
    n=len(p)
    for i in range(len(t)-n+1):
<<<<<<< HEAD
        sliced_lst=t[i:i+n]
        if int(sliced_lst)<=int(p):
=======
        sliced_lst=t[i:i+3]
        s=""
        for j in range(n):
            s+=str(sliced_lst[j])
            int(s)
        print(s)
        if s<=p:
>>>>>>> origin/main
            answer+=1
    return answer

print(solution("10203","15"))