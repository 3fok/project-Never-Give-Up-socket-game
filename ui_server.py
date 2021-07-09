import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
import random
import string 

window = tk.Tk()
window.title("N.G.U. Sever")
window.geometry("500x400")
window.configure(bg='#000000')
window.resizable(0, 0)

frame_info = tk.Frame(window, width = 400, height= 400, bg= '#000000')

lblHost = tk.Label(frame_info, font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff')
lblHost.pack(side=TOP, anchor=W)
lblPort = tk.Label(frame_info, font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff')
lblPort.pack(side=TOP, anchor=W)
def update_host_port(host, port):
    global lblHost,lblPort
    lblHost.config(text = "Address: " + str(host))
    lblHost.pack()
    lblPort.config(text = "Port: " + str(port))
    lblPort.pack()

frame_info_user = tk.Frame(frame_info, width = 400, height= 170, bg='#000000')
lb_user_title = tk.Label(frame_info_user, text='ACCOUNT', font = ('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff')
lb_user_title.pack(side=TOP, anchor=W)
text_user=''
show_text_user = tk.Text(frame_info_user, bd=-1, relief='flat', bg = '#000000', font = ('Roboto Mono', 12, 'bold'), fg = '#ffffff', width = 400, cursor="arrow")
show_text_user.insert('end', text_user)
show_text_user.bind("<Key>", lambda e: "break")
show_text_user.pack(side = TOP)
frame_info_user.propagate(0)
frame_info_user.pack(side=TOP)

frame_info_chart = tk.Frame(frame_info, width = 400, height= 170, bg='#000000')
text_chart_title = ' RANK |         ACCOUNT         | SCORE '
lb_chart_title = tk.Label(frame_info_chart, text=text_chart_title, font = ('Roboto Mono', 12, 'bold'), bg= '#000000', fg='#ffffff')
lb_chart_title.pack(side=TOP, anchor=W)
text_chart=''
show_text_chart = tk.Text(frame_info_chart, bd=-1, relief='flat', bg = '#000000', font = ('Roboto Mono', 12, 'bold'), fg = '#ffffff', width = 400, cursor="arrow")
show_text_chart.insert('end', text_chart)
show_text_chart.bind("<Key>", lambda e: "break")
show_text_chart.pack(side = TOP)
frame_info_chart.propagate(0)
frame_info_chart.pack(side=TOP)

frame_info.propagate(0)
frame_info.place(x=0,y=0)

frame_button = tk.Frame(window, width = 100, height= 400, bg= '#000000')

btnStart = tk.Button(frame_button, text="Start", font=('Roboto Mono', 12, 'bold'), bg= '#000000', fg='#ffffff', width = 8, height= 1)
btnStart.pack(side=TOP)

btnMaxquest = tk.Button(frame_button, text="Max Quest", font=('Roboto Mono', 10, 'bold'), bg= '#000000', fg='#ffffff', width = 10, height= 1)
btnMaxquest.pack(side=TOP)

btnShowDtb = tk.Button(frame_button, text="Show dtb", font=('Roboto Mono', 12, 'bold'), bg= '#000000', fg='#ffffff', width = 8, height= 1)
btnShowDtb.pack(side=TOP)

btnOpenDtb = tk.Button(frame_button, text="Open dtb", font=('Roboto Mono', 12, 'bold'), bg= '#000000', fg='#ffffff', width = 8, height= 1)
btnOpenDtb.pack(side=TOP)

btnMakeQuest = tk.Button(frame_button, text="Make Quest", font=('Roboto Mono', 10, 'bold'), bg= '#000000', fg='#ffffff', width = 10, height= 1)
btnMakeQuest.pack(side=TOP)
btnMakeQuest.config(command=lambda: btnMakeQuest_click())
makequest_input = makequest_output = None
def btnMakeQuest_click():
    global makequest_input, makequest_output
    MakeQuestWindow = Toplevel(window)
    MakeQuestWindow.title('Make Quest')
    MakeQuestWindow.geometry("470x62")
    MakeQuestWindow.configure(bg='#000000')
    MakeQuestWindow.resizable(0, 0)
    lb_quest_input = tk.Label(MakeQuestWindow, text='Input', font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff')
    lb_quest_input.grid(row=0,column=0)
    makequest_input = tk.Entry(MakeQuestWindow, font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff', insertbackground='#ffffff', width=20)
    makequest_input.grid(row=0,column=1)
    lb_quest_output = tk.Label(MakeQuestWindow, text='Output', font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff')
    lb_quest_output.grid(row=1,column=0)
    makequest_output = tk.Text(MakeQuestWindow, font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff', insertbackground='#ffffff', width=20, height=1)
    makequest_output.config(state='disabled')
    makequest_output.grid(row=1,column=1)
    bt_quest_convert = tk.Button(MakeQuestWindow, text='Convert', font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff', command=lambda: bt_convert_quest_click())
    bt_quest_convert.place(x=302, y=10)
    bt_quest_copy = tk.Button(MakeQuestWindow, text='Copy', font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff', command=lambda: bt_copy_quest_click())
    bt_quest_copy.place(x=402, y=10)
def bt_convert_quest_click():
    global makequest_input, makequest_output
    data = makequest_input.get()
    data = convert_quest(data)
    makequest_output.config(state='normal')
    makequest_output.delete('1.0', 'end')
    makequest_output.insert('end', data)
    makequest_output.config(state='disabled')
    makequest_output.grid(row=1,column=1)
def convert_quest(cv_input):
    x = 16 - len(cv_input)
    cv_output = random_char(x) + cv_input
    cv_output = ''.join(random.sample(cv_output,len(cv_output)))
    cv_output = cv_output.upper()
    return cv_output
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))
def bt_copy_quest_click():
    global makequest_output
    data = makequest_output.get("1.0", 'end-1c')
    window.clipboard_clear()
    window.clipboard_append(data)

btnMakeHint = tk.Button(frame_button, text="Make Hint", font=('Roboto Mono', 10, 'bold'), bg= '#000000', fg='#ffffff', width = 10, height= 1)
btnMakeHint.pack(side=TOP)
btnMakeHint.config(command=lambda: btnMakeHint_click())
makeHint_input = makeHint_output = None
def btnMakeHint_click():
    global makeHint_input, makeHint_output
    MakeHintWindow = Toplevel(window)
    MakeHintWindow.title('Make Hint')
    MakeHintWindow.geometry("520x120")
    MakeHintWindow.configure(bg='#000000')
    MakeHintWindow.resizable(0, 0)
    lb_hint_input = tk.Label(MakeHintWindow, text='Input', font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff')
    lb_hint_input.grid(row=0,column=0)
    makeHint_input = tk.Entry(MakeHintWindow, font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff', insertbackground='#ffffff', width=40)
    makeHint_input.grid(row=0,column=1)
    lb_hint_output = tk.Label(MakeHintWindow, text='Output', font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff')
    lb_hint_output.grid(row=1,column=0)
    makeHint_output = tk.Text(MakeHintWindow, font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff', insertbackground='#ffffff', width=40, height=1)
    makeHint_output.config(state='disabled')
    makeHint_output.grid(row=1,column=1)
    bt_hint_convert = tk.Button(MakeHintWindow, text='Convert', font=('Roboto Mono', 14, 'bold'), width=10, bg= '#000000', fg='#ffffff', command=lambda: bt_convert_hint_click())
    bt_hint_convert.place(x=150, y=70)
    bt_hint_copy = tk.Button(MakeHintWindow, text='Copy', font=('Roboto Mono', 14, 'bold'), width=10, bg= '#000000', fg='#ffffff', command=lambda: bt_copy_hint_click())
    bt_hint_copy.place(x=300, y=70)
def bt_convert_hint_click():
    global makeHint_input, makeHint_output
    data = makeHint_input.get()
    data = data.replace(' ','*')
    makeHint_output.config(state='normal')
    makeHint_output.delete('1.0', 'end')
    makeHint_output.insert('end', data)
    makeHint_output.config(state='disabled')
    makeHint_output.grid(row=1,column=1)
def bt_copy_hint_click():
    global makeHint_output
    data = makeHint_output.get("1.0", 'end-1c')
    window.clipboard_clear()
    window.clipboard_append(data)

frame_button.propagate(0)
frame_button.place(x=400,y=0)
def disable_button():
    global btnStart
    btnStart.config(state=tk.DISABLED)
    btnMaxquest.config(state=tk.DISABLED)

#window.mainloop()
