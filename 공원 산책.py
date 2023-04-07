def in_range(nx,ny,n):
     return 0<=nx and nx<n and 0<=ny and ny<n
def solution(park, routes):
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
        f_x,f_y=x,y
        Flag=True
        for j in range(int(routes[i][-1])):
            nx,ny=x+dx[op_dict[routes[i][0]]],y+dy[op_dict[routes[i][0]]]
            if not Flag or not in_range(nx,ny,len(park[0])) or park[nx][ny]=='X':
                Flag=False
                continue
            else:
                x,y=nx,ny
        if not Flag or not in_range(x,y,len(park[0])) or park[x][y]=='X':
            x,y=f_x,f_y
    answer.append(x)
    answer.append(y)
    return answer

print(solution(["OSO", "OOO", "OXO", "OOO"],["E 2","S 3","W 1"]))