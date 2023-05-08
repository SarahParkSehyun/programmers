def solution(dartResult):
    answer = 0
    for _ in range(3):
        digit=""
        idx=0
        save=0
        for i in range(2):
            if dartResult[i].isdigit():
                digit+=dartResult[i]
                idx+=1
        if dartResult[idx]=='S':
            save=int(digit)
            answer+=int(digit)
        elif dartResult[idx]=='D':
            save = int(digit)
            answer+=int(digit)**2
        else:
            save = int(digit)
            answer+=int(digit)**3
        idx+=1
        print(idx)
        if idx!=len(dartResult)-1 and dartResult[idx]=='*':
            idx+=1
            answer=answer*2
        if idx!=len(dartResult)-1 and dartResult[idx]=='#':
            idx+=1
            answer-=save*2
        dartResult=dartResult[idx:]

    return answer

print(solution('1S2D*3T'))