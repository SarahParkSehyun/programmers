def solution(numbers, target):
    answer=0

    def find_target(num, total):
        nonlocal answer
        if num == len(numbers):
            if total==target:
                answer+=1
            return

        find_target(num + 1, total + numbers[num])

        find_target(num + 1, total - numbers[num])

    find_target(0,0)
    return answer

print(solution([1, 1, 1, 1], 3)) 