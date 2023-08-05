answer=[]
def solution(n):
    hanoi(n,1,3,2)
    return answer

def hanoi(n,from_pos,to_pos,aux_pox):
    if n==1:
        answer.append([from_pos,to_pos])
        return
    hanoi(n-1,from_pos,aux_pox,to_pos)
    answer.append([from_pos,to_pos])
    hanoi(n-1,aux_pox,to_pos,from_pos)

print(solution(3))