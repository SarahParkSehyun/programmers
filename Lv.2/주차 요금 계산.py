import math

def solution(fees, records):
    car_info = {}
    answer = {}

    for record in records:
        time, car_num, status = record.split()

        if car_num not in car_info:
            car_info[car_num] = []

        car_info[car_num].append((time, status))

    for car, infos in car_info.items():
        total_time = 0
        in_time = None

        for info in infos:
            time, status = info
            h, m = map(int, time.split(":"))
            minutes = h * 60 + m

            if status == "IN":
                in_time = minutes
            else:
                total_time += minutes - in_time
                in_time = None

        if in_time is not None:  # 23:59 출차 적용
            total_time += (23 * 60 + 59) - in_time

        if total_time <= fees[0]:
            charge = fees[1]
        else:
            charge = fees[1] + math.ceil((total_time - fees[0]) / fees[2]) * fees[3]

        answer[car] = charge

    sorted_answer = dict(sorted(answer.items()))

    return list(sorted_answer.values())


print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))