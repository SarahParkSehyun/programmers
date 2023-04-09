def solution(keymap, targets):
    answer = []
    for i in range(len(targets)):
        Flag = True
        sum=0
        for j in range(len(targets[i])):
            if Flag==False:
                continue
            flag = False
            idx=100
            for k in range(len(keymap)):
                if targets[i][j] in keymap[k]:
                    if keymap[k].index(targets[i][j])<idx:
                        idx=keymap[k].index(targets[i][j])
                        flag=True

            if flag==True:
                sum+=(idx+1)
            else:
                Flag=False
                sum=-1
                continue
        answer.append(sum)
    return answer

print(solution(["ABCE"] , ["ABDE"]))