def solution(new_id):
    new_id=new_id.lower()
    for i in range(len(new_id)):
        if not (new_id[i].isalpha() or new_id[i].isdigit() or new_id[i]=="-" or new_id[i]=="_" or new_id[i]=="."):
            new_id=new_id.replace(new_id[i]," ")
    new_id=new_id.replace(" ","")
    while '..' in new_id:
        new_id=new_id.replace("..",".")
    new_id=new_id.strip(".")
    if len(new_id)==0:
        new_id="a"
    if len(new_id)>=16:
        new_id=new_id[0:15]
    new_id=new_id.strip(".")
    if len(new_id)<=2:
        while len(new_id)<3:
            new_id+=new_id[-1]
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))