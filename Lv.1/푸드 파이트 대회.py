def solution(food):
    answer = []
    for i in range(1,len(food)):
        num=food[i]//2
        for _ in range(num):
            answer.append(i)
    reversed_answer=answer[::-1]
    answer.append(0)
    answer+=reversed_answer
    answer=[str(x) for x in answer]
    return ''.join(answer)
print(solution([1, 3, 4, 6]))