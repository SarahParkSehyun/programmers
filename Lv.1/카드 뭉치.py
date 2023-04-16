def solution(cards1, cards2, goal):
    answer="Yes"
    idx_1,idx_2=0,0
    for word in goal:
        if word in cards1 and cards1[idx_1]==word:
            idx_1+=1
        elif word in cards2 and cards2[idx_2]==word:
            idx_2+=1
        else:
            answer="No"
            return answer
    return answer

print(solution(["a","b","c"],["d", "e"],["b", "c", "d", "e"]))