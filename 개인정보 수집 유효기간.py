def solution(today, terms, privacies):
    answer = []
    today=today.split(".")
    today=int(today[0])*12*28+int(today[1])*28+int(today[2])
    terms_dict={}
    for i in range(len(terms)):
        type,period=terms[i].split(" ")
        terms_dict[type]=int(period)

    for i in range(len(privacies)):
        y,m,d = int(privacies[i][0:4]),int(privacies[i][5:7]),int(privacies[i][8:10])
        days=y*12*28+m*28+d+terms_dict[privacies[i][-1]]*28
        if days<=today:
            answer.append(i+1)
    return answer

print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
