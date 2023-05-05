def solution(numbers, hand):
    answer = ''
    left_idx=(3,0)
    right_idx=(3,2)
    for number in numbers:
        if number==1 or number==4 or number==7:
            answer+='L'
            if number==1:
                left_idx=(0,0)
            elif number==4:
                left_idx=(1,0)
            else:
                left_idx=(2,0)
        elif number==3 or number==6 or number==9:
            answer+='R'
            if number==3:
                right_idx=(0,2)
            elif number==6:
                right_idx=(1,2)
            else:
                right_idx=(2,2)
        else:
            if number==2:
                right_dict=abs(0-right_idx[0])+abs(1-right_idx[1])
                left_dict=abs(0-left_idx[0])+abs(1-left_idx[1])
                if right_dict<left_dict:
                    answer += 'R'
                    right_idx=(0,1)
                elif right_dict>left_dict:
                    answer += 'L'
                    left_idx=(0,1)
                else:
                    if hand=='right':
                        answer+='R'
                        right_idx = (0, 1)
                    else:
                        answer+='L'
                        left_idx = (0, 1)
            elif number==5:
                right_dict = abs(1 - right_idx[0]) + abs(1 - right_idx[1])
                left_dict = abs(1 - left_idx[0]) + abs(1 - left_idx[1])
                if right_dict < left_dict:
                    answer += 'R'
                    right_idx=(1,1)
                elif right_dict > left_dict:
                    answer += 'L'
                    left_idx = (1, 1)
                else:
                    if hand=='right':
                        answer+='R'
                        right_idx=(1,1)
                    else:
                        answer+='L'
                        left_idx = (1, 1)
            elif number==8:
                right_dict = abs(2 - right_idx[0]) + abs(1 - right_idx[1])
                left_dict = abs(2 - left_idx[0]) + abs(1 - left_idx[1])
                if right_dict < left_dict:
                    answer += 'R'
                    right_idx=(2,1)
                elif right_dict > left_dict:
                    answer += 'L'
                    left_idx = (2, 1)
                else:
                    if hand=='right':
                        answer+='R'
                        right_idx=(2,1)
                    else:
                        answer+='L'
                        left_idx = (2, 1)
            else:
                right_dict = abs(3 - right_idx[0]) + abs(1 - right_idx[1])
                left_dict = abs(3 - left_idx[0]) + abs(1 - left_idx[1])
                if right_dict < left_dict:
                    answer += 'R'
                    right_idx=(3,1)
                elif right_dict > left_dict:
                    answer += 'L'
                    left_idx = (3, 1)
                else:
                    if hand=='right':
                        answer+='R'
                        right_idx=(3,1)
                    else:
                        answer+='L'
                        left_idx = (3, 1)
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))