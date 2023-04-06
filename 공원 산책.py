def in_range(nx,ny,n):
     return 0<=nx and nx<n and 0<=ny and ny<n
def solution(park, routes):
    print(park)
    answer = []
    op_dict={
        "N":0,
        "S":1,
        "W":2,
        "E":3
    }
    dx,dy=[-1,1,0,0],[0,0,-1,1]
    x,y=0,0
    for i in range(len(park)):
        if 'S' in park[i]:
            x,y=i,park[i].index('S')
    for i in range(len(routes)):
        Flag=True
        for j in range(int(routes[i][-1])):
            nx,ny=x+dx[op_dict[routes[i][0]]],y+dy[op_dict[routes[i][0]]]
            if not Flag or not in_range(nx,ny,len(park[0])) or park[nx][ny]=='X':
                Flag=False
                continue
            else:
                x,y=nx,ny
    answer.append(x)
    answer.append(y)
    return answer

print(solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"]))