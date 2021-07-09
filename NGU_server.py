from tkinter import Toplevel
from tkinter.constants import END
import ui_server as ui_sv
import socket_server as sk_sv
import dtb
import dtb
from _thread import *
from time import sleep
import tkinter as tk
from tkinter import *
from tkinter import messagebox

host = '127.0.0.1'
port = 9090
ui_sv.update_host_port(host, port)
sk_sv.update_host_port(host, port)

ui_sv.btnStart.config(command=lambda : start_server())
def start_server():
    ui_sv.disable_button()
    start_new_thread(sk_sv.start_server, ())

ui_sv.btnMaxquest.config(command=lambda : btnMaxquest_click())
MaxQuest_input = MaxQuestWindow = None
def btnMaxquest_click():
    global MaxQuest_input, MaxQuestWindow
    MaxQuestWindow = Toplevel(ui_sv.window)
    MaxQuestWindow.title('Max Quest')
    MaxQuestWindow.geometry("470x62")
    MaxQuestWindow.configure(bg='#000000')
    MaxQuestWindow.resizable(0, 0)
    lb_MaxQuest_input = tk.Label(MaxQuestWindow, text='Max Quest: ', font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff')
    lb_MaxQuest_input.grid(row=0,column=0)
    MaxQuest_input = tk.Entry(MaxQuestWindow, font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff', insertbackground='#ffffff', width=20)
    MaxQuest_input.grid(row=0,column=1)
    bt_MaxQuest = tk.Button(MaxQuestWindow, text='Change', font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff', command=lambda: bt_MaxQuest_click())
    bt_MaxQuest.grid(row=0,column=2)
def bt_MaxQuest_click():
    global MaxQuest_input, MaxQuestWindow
    MQ_input = MaxQuest_input.get()
    max_quest_dtb = dtb.number_of_quest
    if MQ_input.isdigit():
        if int(MQ_input) <= max_quest_dtb():
            sk_sv.maxquest_play = int(MQ_input)
            messagebox.showinfo("(ヘ･_･)ヘ┳━┳", "Đã đổi số câu hỏi tối đa!!")
            MaxQuestWindow.destroy()
            return
        else:
            messagebox.showinfo("(ﾉ´･ω･)ﾉ ﾐ ┻━┻", "Phải nhập vào 1 số tự nhiên nhỏ hơn số câu hỏi trong database")
    else:
        messagebox.showinfo("(ﾉ´･ω･)ﾉ ﾐ ┻━┻", "Phải nhập vào 1 số tự nhiên nhỏ hơn số câu hỏi trong database")
    MaxQuest_input.delete(0,END)

ui_sv.btnShowDtb.config(command=lambda: btnShowDtb_click())
def btnShowDtb_click():
    ui_sv.text_user = ''
    data_acc = dtb.get_acc_server()
    for data in data_acc:
        ui_sv.text_user += ' ' + str(data[0]) +'\n'
    ui_sv.text_user = ui_sv.text_user[:len(ui_sv.text_user)-1]
    ui_sv.show_text_user.delete('1.0', 'end')
    ui_sv.show_text_user.insert('end', ui_sv.text_user)
    ui_sv.show_text_user.pack()
    ui_sv.text_chart = ''
    data_chart = dtb.get_chart_server()
    for data in data_chart:
        t = '#' + str(data[0])
        ui_sv.text_chart += t.center(6)
        t = str(data[1])
        ui_sv.text_chart += t.center(27)
        t = str(data[2])
        ui_sv.text_chart += t.center(7) + '\n'
    ui_sv.text_chart = ui_sv.text_chart[:len(ui_sv.text_chart)-1]
    ui_sv.show_text_chart.delete('1.0', 'end')
    ui_sv.show_text_chart.insert('end', ui_sv.text_chart)
    ui_sv.show_text_chart.pack()

ui_sv.btnOpenDtb.config(command=lambda: btnOpenDtb_click())
def btnOpenDtb_click():
    import os
    os.startfile("dtb.db")

ui_sv.window.mainloop()