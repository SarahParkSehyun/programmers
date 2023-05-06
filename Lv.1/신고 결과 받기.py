def solution(id_list, report, k):
    report=set(report)
    answer = [0]*len(id_list)
    stop_user=[]
    user_dict={id:i for i,id in enumerate(id_list)}
    id_dict={id:0 for id in id_list}
    for id in report:
        id=id.split(" ")
        id_dict[id[-1]]+=1
    for id in id_list:
        if id_dict[id]>=k:
            stop_user.append(id)
    for id in report:
        id=id.split(" ")
        if id[-1] in stop_user:
            answer[user_dict[id[0]]]+=1
    return answer

print(solution(	["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))