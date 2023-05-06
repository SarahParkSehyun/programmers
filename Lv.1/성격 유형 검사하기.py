def solution(survey, choices):
    answer = ''
    num_dict={1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    alp_dict={"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    for i in range(len(survey)):
        if choices[i]<4:
            alp_dict[survey[i][0]]+=num_dict[choices[i]]
        else:
            alp_dict[survey[i][1]] += num_dict[choices[i]]
    alp_dict_keys=list(alp_dict.keys())
    alp_dict_values=list(alp_dict.values())
    i=0
    while i<7:
        if alp_dict_values[i]>alp_dict_values[i+1]:
            answer += alp_dict_keys[i]
        elif alp_dict_values[i] < alp_dict_values[i + 1]:
            answer += alp_dict_keys[i+1]
        else:
            answer+=min(alp_dict_keys[i],alp_dict_keys[i+1])
        i+=2
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))