def solution(triangle):
    for i in range(1,len(triangle)):
        triangle[i][0]=triangle[i-1][0]+triangle[i][0]
        triangle[i][-1] = triangle[i - 1][-1]+triangle[i][-1]

    for i in range(2,len(triangle)):
        for j in range(1,len(triangle[i])):
            if j!=0 and j!=i:
                triangle[i][j]=max(triangle[i-1][j],triangle[i-1][j-1])+triangle[i][j]
    answer=max(triangle[-1])

    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))