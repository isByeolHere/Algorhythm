def solution(id_pw, db):
    check_id = id_pw[0]
    pw = id_pw[1]
    
    for db_id, db_pw in db:
        if check_id == db_id:
            if pw == db_pw:
                return "login"
            else:
                return "wrong pw"
    return "fail"
