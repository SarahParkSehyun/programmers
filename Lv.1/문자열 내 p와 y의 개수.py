from collections import Counter

def solution(s):
    s=s.lower()
    count=Counter(s)
    if count['p']!=count['y']:
        return False
    return True

print(solution("pPoooyY"))