import pymysql

conn = pymysql.connect(host='localhost', user='root',password='love71270^^', db='aof',charset='utf8')
cur = conn.cursor()
query = """select * from user"""
cur.execute(query)
data = cur.fetchall()
def Log(id, pw):
    g = 0
    query = """select * from user"""
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        if id == i[0]:
            if pw == str(i[1]):
                print("로그인이 완료되었습니다")
                g = 1
                break
            else:
                print("비밀번호를 다시 확인해주세요")
                g = 1
                break
    if g == 0: print("회원 정보가 존재하지 않습니다")
            
def signup(id, pw):
    #id key 설정해야 함(겹치는 아이디가 없도록)
    try: 
        with conn.cursor() as cursor:
            sql = 'INSERT INTO user (ID, PIN) VALUES ("%s", %d);'
            cursor.execute(sql%(id, int(pw)))
        conn.commit()
    except Exception as e:
        pass
    finally:
        print("회원가입을 완료되었습니다")

def delete(id, pw):
    try:
        with conn.cursor() as cursor:
            sql = 'DELETE FROM user WHERE ID = "%s";'
            cursor.execute(sql%id)
        conn.commit()
    except Exception as e:
        pass
    finally:
        print("회원탈퇴가 완료되었습니다")

def change(id, pw):
    ch = input("| HP | REGION | INTRO | SUBJECT | RATING | ROLE | SCHEDULE |\n변경하려는 요소 : ")
    si = input("변경할 값 : ")
    try:
        with conn.cursor() as cursor:
            sql = 'UPDATE user SET %s = "%s" WHERE id = "%s";'
            cursor.execute(sql%(ch, si, id))
        conn.commit()
    except Exception as e:
        pass
    finally:
        print("정보가 변경되었습니다.")

while (1):

    p = int(input('1: Login \n2: Signup\n3: delete\n4: change\n5: log out\n'))
    if p == 1:
        id = input("ID:")
        pw = input("PW:")
        Log(id, pw)
    elif p == 2:
        id = input("ID:")
        pw = input("PW:")
        signup(id, pw)
    elif p == 3:
        id = input("ID:")
        pw = input("PW:")
        delete(id, pw)
    elif p == 4:
        id = input("ID:")
        pw = input("PW:")
        change(id, pw)
    elif p == 5:
        break
    else:
        print('잘못된 값입니다, 다시 입력하세요')
