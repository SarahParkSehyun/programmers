def solution(s):
    answer = 0
    i=0
    while i<len(s):
        x=s[i]
        x_cnt=1
        y_cnt=0
        if i==(len(s)-1):
            answer+=1
            break
        for j in range(i+1,len(s)):
            if s[j]==x:
                x_cnt+=1
            elif s[j]!=x:
                y_cnt+=1
            if x_cnt==y_cnt:
                answer+=1
                i=j+1
                break
            if j==(len(s)-1) and x_cnt!=y_cnt:
                answer+=1
                return answer
    return answer

print(solution("abracadabra"))