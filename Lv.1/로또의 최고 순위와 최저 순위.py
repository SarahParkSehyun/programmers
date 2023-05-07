def solution(lottos, win_nums):
    cnt=0
    for lotto in lottos:
        if lotto in win_nums:
            cnt+=1
    dct={6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    answer=[dct[cnt+lottos.count(0)],dct[cnt]]

    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))