def solution(keymap, targets):
    answer = []
    for i in range(len(targets)):
        sum=0
        flag=False
        for j in range(len(targets[i])):
            idx=100
            for k in range(len(keymap)):
                if targets[i][j] in keymap[k]:
                    if keymap[k].index(targets[i][j])<idx:
                        idx=keymap[k].index(targets[i][j])
                        flag=True
            if flag==True:
                sum+=(idx+1)
            else:
                sum=-1
        answer.append(sum)
    return answer

print(solution(["AA"],["B"]))