#region
from typing import NoReturn
import sqlite3
from sqlite3.dbapi2 import Cursor
#Ket noi den dtb
conn = cursor = None
def connect_dtb():
    global conn, cursor
    conn  = sqlite3.connect('dtb.db', check_same_thread=False)
    cursor = conn.cursor()
#endregion

def view_acc(acc): #tìm tài khoản
    global cursor
    cursor.execute('select * from account')
    for row in cursor:
        if row[0] == acc:
            return row[1]
    return None

def add_acc(acc,pw): #thêm tài khoản
    conn  = sqlite3.connect('dtb.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("insert into account values (?,?)",(acc,pw))
    conn.commit()

def changepass(acc, newpw): #đổi userpass
    global cursor
    cursor.execute('update account SET PASS=? WHERE ACCOUNT=?', (newpw, acc))
    conn.commit()

def number_of_quest(): #tinh tong so cau hoi
    global cursor
    cursor.execute('select count(ID_q) from ques_list')
    count = cursor.fetchone()[0]
    return count

def view_quest(quest_num): #noi dung cau hoi
    global cursor
    cursor.execute('select * from ques_list')
    for row in cursor:
        if int(row[0]) == quest_num:
            return row[1]     

def view_ans(quest_num): #noi dung cau tra loi
    global cursor
    cursor.execute('select * from ques_list')
    for row in cursor:
        if int(row[0]) == quest_num:
            return row[2]

def view_hint(quest_num): #noi dung hint
    global cursor
    cursor.execute('select * from ques_list')
    for row in cursor:
        if int(row[0]) == quest_num:
            return row[3]

def view_user_rank(acc):#xem 3 rank quanh user
    global cursor
    data = ''
    cursor.execute('select * from ranking')
    for row in cursor:
        if row[1] == acc:
            rank = int(row[0])
            data = row[0]+'*'+row[1]+'*'+row[2]
            break
    cursor.execute('select * from ranking')
    if rank == 1:
        flag = 0
        for row in cursor:
            if int(row[0]) == 2:
                b = row[0]+'*'+row[1]+'*'+row[2]
                if flag == 0: flag = 1
                else: break
            if int(row[0]) == 3:
                c = row[0]+'*'+row[1]+'*'+row[2]
                if flag == 0: flag = 1
                else: break
        return str(data) + '*' + str(b) + '*' + str(c)
    else:
        flag = 0
        for row in cursor:
            if int(row[0]) == rank-1:
                a = row[0]+'*'+row[1]+'*'+row[2]
                if flag == 0: flag = 1
                else: break
            if int(row[0]) == rank+1:
                c = row[0]+'*'+row[1]+'*'+row[2]
                if flag == 0: flag = 1
                else: break
        return str(a) + '*' + str(data) + '*' + str(c)   

#region #cập nhật điểm vào rank
def add_rank(acc, score):
    global cursor
    flag = 0
    cursor.execute('select * from ranking')
    for row in cursor:
        if row[1] == acc:
            flag = 1
            break
    if flag == 0:
        cursor.execute('select count(rank) from ranking')
        count = cursor.fetchone()[0]
        cursor.execute("insert into ranking values (?,?,?)",(count+1,acc,score))
        conn.commit()
        update_rank()
    if flag == 1:
        if int(row[2]) < int(score):
            cursor.execute('update ranking SET SCORE=? WHERE ACCOUNT=?', (score, acc))
            conn.commit()
            update_rank()

def update_rank():
    global cursor
    cursor.execute('select * from ranking')
    data = cursor.fetchall()
    for i in range(0, len(data)):
        data[i]=list(data[i])
    for i in range(0, len(data)):
        for j in range(i+1, len(data)):
            if int(data[i][2]) <= int(data[j][2]):
                t=data[i]
                data[i] = data[j]
                data[j] = t
    for i in range(0, len(data)):
        data[i][0] = str(i+1)
        data[i]=tuple(data[i])
    cursor.execute('delete from ranking')
    cursor.executemany('insert into ranking values (?,?,?)', data)
    conn.commit()
#endregion              

def get_chart(): # lấy toàn bộ bảng xếp hạng
    global cursor
    data = 'getchart '
    cursor.execute('select * from ranking')
    for row in cursor:
        data = data + row[0]+'*'+row[1]+'*'+row[2]+'*'
    return data

def get_acc_server(): # lấy toàn bộ account cho server hiển thị
    global cursor
    cursor.execute('select * from account')
    return cursor.fetchall()

def get_chart_server(): # lấy toàn bộ bảng xếp hạng cho server hiển thị
    global cursor
    cursor.execute('select * from ranking')
    return cursor.fetchall()

def close_dtb(): #đóng database
    conn.close()
