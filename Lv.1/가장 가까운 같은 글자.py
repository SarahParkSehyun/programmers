def solution(s):
    answer = [-1]
    for i in range(1,len(s)):
        c=s[i]
        flag = False
        for j in range(i-1,-1,-1):
            if flag==True:
                continue
            if s[j]==c:
                answer.append(i-j)
                flag=True
        if flag==False:
            answer.append(-1)

    return answer

print(solution("banana"))