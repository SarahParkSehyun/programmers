def solution(wallpaper):
    answer = []
    idx=[]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j]=='#':
                idx.append([i,j])
    x_lst,y_lst=[],[]
    for i in range(len(idx)):
        x_lst.append(idx[i][0])
        y_lst.append(idx[i][1])
    x_lst.sort()
    y_lst.sort()
    answer=[x_lst[0],y_lst[0],x_lst[-1]+1,y_lst[-1]+1]
    return answer

''''
def solution(wall):
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]
'''

print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))