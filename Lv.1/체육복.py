def solution(n, lost, reserve):
    student={x:1 for x in range(1,n+1)}
    for l in lost:
        student[l]-=1
    for r in reserve:
        student[r]+=1
    lst=[x for x in range(1,n+1) if student[x]==0]
    for l in lst:
        if l==1:
            if student[l+1]==2:
                student[l]+=1
                student[l+1]-=1
        elif l==n:
            if student[l-1]==2:
                student[l]+=1
                student[l-1]-=1
        else:
            if student[l - 1] == 2:
                student[l] += 1
                student[l - 1] -= 1
            if student[l]!=1:
                if student[l + 1] == 2:
                    student[l] += 1
                    student[l + 1] -= 1
    answer = len([x for x in range(1, n + 1) if student[x] >= 1])
    return answer

print(solution(5,[2,4],[1,3,5]))