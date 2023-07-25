from collections import deque  # 스택, 큐 복습하기


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    limit = len(queue1) + len(queue2)
    cnt = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    if (sum1 + sum2) % 2 != 0:
        return -1

    while sum1 != sum2:
        if cnt >= limit:
            return -1
        while queue1 and sum1 > sum2:
            num = queue1.popleft()
            queue2.append(num)
            sum1 -= num
            sum2 += num
            cnt += 1

        while queue2 and sum2 > sum1:
            num = queue2.popleft()
            queue1.append(num)
            sum1 += num
            sum2 -= num
            cnt += 1

    return cnt


print(solution([1, 4], [4, 8]))
