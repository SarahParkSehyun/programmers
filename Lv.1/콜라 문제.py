def solution(a, b, n):
    answer = 0
    while n>=a:
        x=n//a*b
        answer+=(n//a)*b
        n=n-(n//a)*a+x
    return answer

print(solution(2,1,20))