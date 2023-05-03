def solution(players, callings):
    p_dict={player:index for index,player in enumerate(players)}
    i_dict={index:player for index,player in enumerate(players)}
    for calling in callings:
        curr_idx=p_dict[calling]
        pre_idx=curr_idx-1
        pre_player=i_dict[pre_idx]
        p_dict[pre_player]=curr_idx
        p_dict[calling]=pre_idx
        i_dict[curr_idx]=pre_player
        i_dict[pre_idx]=calling
    return list(i_dict.values())

print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"]))