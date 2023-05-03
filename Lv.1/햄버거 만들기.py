def solution(ingredient):
    # 1:빵 2:야채 3:고기 연속한 1231 찾기
    answer = 0
    s=[]
    for i in ingredient:
        s.append(i)
        if s[-4:]==[1,2,3,1]: # s[-4:] -> 뒤에서부터 4개 원소
            answer+=1
            for _ in range(4):
                s.pop() #뒤에 4개 pop
    return answer

print(solution([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1]))