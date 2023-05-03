def solution(babbling):
    answer = 0
    for word in babbling:
        if len(word)<=1:
            continue
        i=0
        check=""
        flag=True
        while i<len(word):
            if i<=len(word)-2 and (word[i:i+2]== "ye" or word[i:i+2]=="ma") and word[i:i+2]!=check:
                check = word[i:i + 2]
                i+=2
            elif i<=len(word)-3 and (word[i:i+3]=="aya" or word[i:i+3]=="woo") and word[i:i+3]!=check:
                check=word[i:i+3]
                i+=3
            else:
                flag=False
                break
        if flag:
            answer+=1
    return answer

print(solution(["yemawoo"]))