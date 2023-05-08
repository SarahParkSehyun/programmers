def solution(dartResult):
    answer = []
    for _ in range(3):
        digit=""
        idx=0
        for i in range(2):
            if dartResult[i].isdigit():
                digit+=dartResult[i]
                idx+=1
        if dartResult[idx]=='S':
            answer.append(int(digit))
        elif dartResult[idx]=='D':
            answer.append(int(digit)**2)
        else:
            answer.append(int(digit)**3)
        idx+=1
        if idx!=len(dartResult) and dartResult[idx]=='*':
            idx+=1
            if len(answer)>1:
                answer[-2]=answer[-2]*2
                answer[-1]=answer[-1]*2
            else:
                answer[-1]=answer[-1]*2
        if idx!=len(dartResult) and dartResult[idx]=='#':
            idx+=1
            answer[-1]=answer[-1]*(-1)
        dartResult=dartResult[idx:]
    return sum(answer)

print(solution("1S2D*3T"))