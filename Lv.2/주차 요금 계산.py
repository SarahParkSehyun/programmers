import math

def solution(fees, records):
    answer = []
    dict_car={}
    for r in records:
        car=r.split(" ")
        if car[-1]=="IN":
            dict_car[car[1]]=car[0]
        else:
            time2=car[0].split(":")
            time1=dict_car[car[1]].split(":")
            cnt=(time2[0]-time1[0])*60+(time2[1]-time1[1])
            if cnt>fees[0]:
                charge=fees[1]+math.ceil((cnt-fees[0])/10)*fees[-1]
            else:
                charge=fees[1]
            answer.append(charge)


    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))