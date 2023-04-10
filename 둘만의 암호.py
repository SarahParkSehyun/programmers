def solution(s, skip, index):
    answer = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in list(skip):
        alpha=alpha.replace(i,"")
    for a in s:
        answer+=alpha[(alpha.find((a))+index)%len(alpha)]
    return answer

s="aukks"
skip="wbqd"
index=5
print(solution(s, skip, index))