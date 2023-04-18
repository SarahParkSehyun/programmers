def solution(number, limit, power):
    answer = 1
    for i in range(2,number+1):
        cnt=2
        for j in range(2,int(i**0.5)+1):
            if j*j==i:
                cnt+=1
            elif i%j==0:
                cnt+=2
        #print(i,cnt)
        if cnt<=limit:
            answer+=cnt
        else:
            answer+=power
    return answer

print(solution(5,3,2))
