def solution(picks, minerals):
    answer = 0
    dia_dict={"diamond":1,"iron":1,"stone":1}
    iron_dict={"diamond":5,"iron":1,"stone":1}
    stone_dict={"diamond":25,"iron":5,"stone":1}

    counts={}
    for mineral in minerals:
        if mineral in minerals:
            counts[mineral]+=1
        else:
            counts[mineral]=1


    return answer