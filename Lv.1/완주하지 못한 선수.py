from collections import Counter

def solution(participant, completion):
    answer = ''
    p_count=Counter(participant)
    c_count=Counter(completion)
    for c in participant:
        if p_count[c]!=c_count[c]:
            answer=c
    return answer

print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))