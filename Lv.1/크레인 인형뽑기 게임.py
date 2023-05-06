def solution(board, moves):
    answer = 0
    store=[]
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1]!=0:
                store.append(board[i][move-1])
                board[i][move-1]=0
                break
        if len(store)>=2 and store[-1]==store[-2]:
            store.pop()
            store.pop()
            answer+=2
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))