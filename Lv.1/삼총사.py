def solution(number):
    answer = 0
    for i in range(len(number)-2):
        sum=0
        sum+=number[i]
        for j in range(i+1,len(number)-1):
            sum+=number[j]
            for k in range(j+1,len(number)):
                sum+=number[k]
                if sum==0:
                    answer+=1
                sum-=number[k]
            sum-=number[j]
        sum-=number[i]

    return answer


print(solution([-3, -2, -1, 0, 1, 2, 3]))