'''def solution(X, Y):
    letter_lst=[]
    x_dict,y_dict={},{}
    for letter in X:
        x_dict[letter]=x_dict.get(letter,0)+1
    for letter in Y:
        y_dict[letter]=y_dict.get(letter,0)+1
    x_keys = x_dict.keys()
    #print(x_dict,y_dict)
    for letter in x_keys:
        if letter in Y:
            if x_dict[letter]<y_dict[letter]:
                for _ in range(x_dict[letter]):
                    letter_lst.append(letter)
            elif x_dict[letter]>=y_dict[letter]:
                for _ in range(y_dict[letter]):
                    letter_lst.append(letter)
    letter_lst.sort(reverse=True)
    if len(letter_lst)>0:
        return "".join(letter_lst)
    if list(set(letter_lst))[0]=="0":
        return "0"
    else:
        return -1'''
from collections import Counter

def solution(X, Y):
    answer=''
    x_counter=Counter(X)
    y_counter=Counter(Y)
    for i in range(9,-1,-1):
        answer+=(str(i)*min(x_counter[str(i)],y_counter[str(i)]))
    if answer=='':
        return '-1'
    elif len(answer)==answer.count('0'):
        return '0'
    else:
        return answer


print(solution("5525","1255"))