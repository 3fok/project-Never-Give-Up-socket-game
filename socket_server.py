from os import terminal_size
import socket
from _thread import *
from tkinter.constants import NONE
import dtb
import time
import random

dtb.connect_dtb()
ServerSocket = None
host = None
port = None
ThreadCount = 0

def update_host_port(host1, port1): #cập nhật các địa chỉ
    global host, port
    host = host1
    port = port1

def data_for_play(question_num, data_received, last_answer):
    if data_received == last_answer: add_score = 1
    else: add_score = 0
    last_answer = dtb.view_ans(question_num)
    question = dtb.view_quest(question_num)
    hint = dtb.view_hint(question_num)
    data4sent = 'play ' + str(add_score) + " " + str(question_num) + " " + str(question) + " " + str(hint)
    return data4sent, last_answer

maxquest_play = 4
def threaded_client(connection):
    global maxquest_play
    user_name = ''
    question_num_play = 1
    #maxquest_play = 4
    last_answer = ''
    maxquest = dtb.number_of_quest()
    while True:
        dataFromClient = connection.recv(1024)
        if not dataFromClient:
            continue
        else:
            data = dataFromClient.decode()
            data = data.split()
            if data[0] == 'getchart':
                data_sent = dtb.get_chart()
                connection.send(data_sent.encode())
            elif data[0] == 'login':
                if data[1] == 'signup':
                    if dtb.view_acc(data[2]) == None:
                        dtb.add_acc(data[2], data[3])
                        x='login 1'
                        connection.send(x.encode())
                    else:
                        x='login 0'
                        connection.send(x.encode())
                elif data[1] == 'login':
                    if dtb.view_acc(data[2]) == data[3]:
                        user_name = data[2]
                        x='login 1'
                        connection.send(x.encode())
                        time.sleep(0.5)
                        question_num_play = 1
                        question_num = random.sample(range(1, maxquest+1), maxquest_play)
                        (data_sent, last_answer) = data_for_play(question_num[question_num_play-1], '*', last_answer)
                        connection.send(data_sent.encode())
                    else:
                        x='login 0'
                        connection.send(x.encode())
                elif data[1] == 'changepass':
                    if dtb.view_acc(data[2]) == data[3]:
                        user_name = data[2]
                        x='login 1'
                        connection.send(x.encode())
                        dtb.changepass(data[2], data[4])
                    else:
                        x='login 0'
                        connection.send(x.encode())
            elif data[0] == 'answer':
                if question_num_play == maxquest_play:
                    if data[1] == last_answer: check_answer = 1
                    else: check_answer = 0
                    data_sent = 'lastques ' + str(check_answer)
                    connection.send(data_sent.encode()) 
                else:
                    question_num_play +=1
                    (data_sent, last_answer) = data_for_play(question_num[question_num_play-1], data[1], last_answer)
                    connection.send(data_sent.encode())
            elif data[0] == 'endgame':
                dtb.add_rank(user_name, data[1])
                data = dtb.view_user_rank(user_name)
                data = 'endgame ' + data
                connection.send(data.encode())
            elif data[0] == 'playagain':
                question_num_play = 1
                question_num = random.sample(range(1, maxquest+1), maxquest_play)
                last_answer = ''
                (data_sent, last_answer) = data_for_play(question_num[question_num_play-1], '*', last_answer)
                connection.send(data_sent.encode())
            elif data[0] == 'exit':
                question_num_play = 1
                question_num = random.sample(range(1, maxquest+1), maxquest_play)
    connection.close()            

def start_server():
    global ServerSocket, host, port, ThreadCount
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))

    ServerSocket.listen()
    while True:
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(threaded_client, (Client, ))
        ThreadCount += 1

#ServerSocket.close()