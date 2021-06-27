#region
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from _thread import *
import time
from PIL import Image, ImageTk
#endregion

#region # thiết lập window
window = tk.Tk()
window.title("(N)ever (G)ive (U)p (ﾉ´･ω･)ﾉ ﾐ ┻━┻") #đổi tiêu đề
window.geometry("420x540") # đặt size 14x18 (x30)
window.iconbitmap("icon//NGU.ico") # đặt icon trên tiêu đề
window.configure(bg='#b3dfff') # đổi màu nền chính
window.resizable(0, 0)#khoá kích thước cửa sổ
#endregion

#region # frame bắt đầu 
frame_start = Frame(window, bg = '#000000', width = 420, height= 540)

ic_word_quiz_st = Image.open("icon//word_quiz.png")
ic_word_quiz_st = ic_word_quiz_st.resize((300,200))
icon_word_quiz_st = ImageTk.PhotoImage(ic_word_quiz_st)
label_word_quiz_st = tk.Label(frame_start, image = icon_word_quiz_st, bd = 0)
label_word_quiz_st.pack(side = TOP, anchor = CENTER)

pt_start = PhotoImage(file="icon//start.gif")
bt_start = tk.Button(frame_start, relief='flat',background='#000000',image=pt_start)
bt_start.pack(side = TOP)

#region # bảng xếp hạng
frame_start_ranking = Frame(window, bg = '#000000', width = 420, height= 540)
frame_start_ranking1= Frame(frame_start_ranking, bg = '#000000', width = 420, height= 40)
pt_ranking_back = PhotoImage(file="icon//back.gif")
bt_ranking_back = tk.Button(frame_start_ranking1, relief='flat',background='#000000',image=pt_ranking_back, command = lambda: bt_ranking_back_click())
def bt_ranking_back_click():
    frame_start_ranking.pack_forget()
    frame_start.pack()
bt_ranking_back.pack(side = LEFT)
frame_start_ranking1.propagate(0)
frame_start_ranking1.pack(side = TOP)

show_ranking_title = Message(frame_start_ranking, bg = '#000000', fg = '#ffffff', text = 'Bảng xếp hạng ╰(*°▽°*)╯', font = "Calibri 25 bold", width = 360, justify = CENTER)
show_ranking_title.pack(side = TOP)

frame_start_ranking2= Frame(frame_start_ranking, bg = '#000000', width = 420, height= 350)
def text_ranking(all_rank_text):
    text = '(rank | name | score)\n'
    data = all_rank_text
    data = data.replace('*',' ')
    data = data.split()
    i = 0
    for x in data:
        if i%3==0: text = text + '> #' + x + '    '
        elif i%3==1: text = text + x + '    '
        elif i%3==2: text = text + x + ' <\n'
        i += 1
    text = text[:len(text)-1] #xoá kí tự xuống dòng cuối cùng
    return text


show_ranking = tk.Text(frame_start_ranking2, relief='flat', bg = '#000000', font = "Calibri 17 bold", fg = '#ffffff', width = 360, cursor="arrow")
show_ranking.tag_configure('tag-center', justify='center')
show_ranking.pack(side = TOP)
frame_start_ranking2.propagate(0)
frame_start_ranking2.pack(side = TOP)

frame_start_ranking.propagate(0)
frame_start_ranking.pack()
frame_start_ranking.pack_forget()

pt_chart = PhotoImage(file="icon//topusers.gif")
bt_chart = tk.Button(frame_start, image=pt_chart, relief='flat',background='#000000')
bt_chart.pack(side = TOP)
#endregion

#region # thông tin chơi
frame_start_info = Frame(window, bg = '#000000', width = 420, height= 540)
frame_start_info1= Frame(frame_start_info, bg = '#000000', width = 420, height= 40)
pt_info_back = PhotoImage(file="icon//back.gif")
bt_info_back = tk.Button(frame_start_info1, relief='flat',background='#000000',image=pt_info_back, command = lambda: bt_info_back_click())
def bt_info_back_click():
    frame_start_info.pack_forget()
    frame_start.pack()
bt_info_back.pack(side = LEFT)
frame_start_info1.propagate(0)
frame_start_info1.pack(side = TOP)
show_info_title = Message(frame_start_info, bg = '#000000', fg = '#ffffff', text = 'Word Quiz', font = "Calibri 27 bold", width = 360, justify = CENTER)
show_info_title.pack(side = TOP)
text_info = """Bạn tìm gì ở đây?
Bạn muốn tìm hướng dẫn?
Không có đâu :)
Mở lên và chơi thôi!
Chứ có gì đâu mà hướng dẫn :)
Chơi vui nhé!!







Thank for your help! :)
Here's a little gift for you <3
___thaobarbie
laylaaa.d
__thuyb
_lingchii
_mayy.01
_trangthuy
charming.duong
delight_hyeon
deoonii.26
dg_linh
djmie95
elina_4_22
emitrann
fearythanyarat
fengtimo520
fox.hoang
grudina_anna_model
h.viviha
han_kyung__
hienanhh_99__
lizhen.149
mintny.zll
mintuyenn
monbiebs
nancy.momoland
qtrang.ng
superxuan001
thaohuyen__
thuytienn.2210
trang._.thu
vox.ngoc.traan
watsamon__
wyntracyy
yudayeon1004
----------------------------------------------
girlsfromasiatoeurope
------------------The end :)------------------
"""
show_info = tk.Text(frame_start_info,relief='flat', bg = '#000000', font = "Calibri 20 bold", fg = '#ffffff', width = 360, cursor="arrow")
show_info.insert('end', text_info)
show_info.pack(side = TOP)
frame_start_info.propagate(0)
frame_start_info.pack()
frame_start_info.pack_forget()
#endregion

pt_info = PhotoImage(file="icon//info.gif")
bt_info = tk.Button(frame_start, image=pt_info, relief='flat',background='#000000', command = lambda: bt_info_click())
bt_info.pack(side = TOP)
def bt_info_click():
    frame_start.pack_forget()
    frame_start_info.pack()

frame_start.pack(side = TOP)
frame_start.propagate(0)
frame_start.pack_forget()
#endregion

#region # frame này để đăng nhập
frame_login = Frame(window, bg = "#000000", width = 420, height= 540)

frame_login1= Frame(frame_login, bg = '#000000', width = 420, height= 40)
pt_login_back = PhotoImage(file="icon//back.gif")
bt_login_back = tk.Button(frame_login1, relief='flat',background='#000000',image=pt_login_back, command = lambda: bt_login_back_click())
def bt_login_back_click():
    frame_login.pack_forget()
    frame_start.pack()
bt_login_back.pack(side = LEFT)
frame_login1.propagate(0)
frame_login1.pack(side = TOP)

ic_word_quiz_lg = Image.open("icon//word_quiz.png")
ic_word_quiz_lg = ic_word_quiz_lg.resize((240,160))
icon_word_quiz_lg = ImageTk.PhotoImage(ic_word_quiz_lg)
label_word_quiz_lg = tk.Label(frame_login, image = icon_word_quiz_lg, bd = 0)
label_word_quiz_lg.pack(side = TOP, anchor = CENTER)

pt_box = PhotoImage(file = "icon//box.gif")
label_user_box = tk.Label(frame_login, image = pt_box, bd = 0)
label_user_box.place(x=100,y=196)
label_user_text = tk.Label(frame_login, text="USERNAME:", bg = '#000000', font = "Helvetica 17 bold", foreground="white")
label_user_text.place(x=20, y=210)
entry_user = tk.Entry(frame_login, bg="#000000", font = "Helvetica 17 bold", foreground="white", insertbackground="white", bd=0,  width = 16)
entry_user.place(x=170, y=210)

label_pass_box = tk.Label(frame_login, image = pt_box, bd = 0)
label_pass_box.place(x=100,y=256)
label_pass_text = tk.Label(frame_login, text="PASSWORD:", bg = '#000000', font = "Helvetica 17 bold", foreground="white")
label_pass_text.place(x=17, y=270)
entry_pass = tk.Entry(frame_login, show="*", bg="#000000", font = "Helvetica 17 bold", foreground="white", insertbackground="white", bd=0,  width = 16)
entry_pass.place(x=170, y=270)

label_new_pass_box = tk.Label(frame_login, image = pt_box, bd = 0)
label_new_pass_box.place(x=100,y=316)
label_new_pass_text = tk.Label(frame_login, text="NEW PASS:", bg = '#000000', font = "Helvetica 17 bold", foreground="white")
label_new_pass_text.place(x=31, y=330)
entry_new_pass = tk.Entry(frame_login, show="*", bg="#000000", font = "Helvetica 17 bold", foreground="white", insertbackground="white", bd=0,  width = 16)
entry_new_pass.place(x=170, y=330)

pt_sign_up = PhotoImage(file="icon//signup.gif")
bt_sign_up = tk.Button(frame_login, relief='flat',background='#000000',image=pt_sign_up)
bt_sign_up.place(x=45, y=385)

pt_login = PhotoImage(file="icon//login.gif")
bt_login = tk.Button(frame_login, relief='flat',background='#000000',image=pt_login)
bt_login.place(x=225, y=385)

pt_call_change_pass = PhotoImage(file="icon//changepass.gif")
bt_call_change_pass = tk.Button(frame_login, relief='flat',background='#000000',image=pt_call_change_pass)
bt_call_change_pass.place(x=135, y=460)

pt_change_pass = PhotoImage(file="icon//changepass.gif")
bt_change_pass = tk.Button(frame_login, relief='flat',background='#000000',image=pt_change_pass)
bt_change_pass.place(x=135, y=385)

def hide_change_pass(x):
    if x == 1:
        label_new_pass_box.place_forget()
        label_new_pass_text.place_forget()
        entry_new_pass.place_forget()
        bt_change_pass.place_forget()
        bt_sign_up.place(x=45, y=385)
        bt_login.place(x=225, y=385)
        bt_call_change_pass.place(x=135, y=460)
    elif x == 0:
        label_new_pass_box.place(x=100,y=316)
        label_new_pass_text.place(x=31, y=330)
        entry_new_pass.place(x=170, y=330)
        bt_change_pass.place(x=135, y=385)
        bt_sign_up.place_forget()
        bt_login.place_forget()
        bt_call_change_pass.place_forget()
hide_change_pass(1)

frame_login.pack(side = TOP)
frame_login.propagate(0)
frame_login.pack_forget() # lệnh ẩn frame
#endregion

#region # frame này để chơi game
frame_play = Frame(window, bg = '#000000', width = 420, height= 540)
# frameplay phần 1
frame_play1 = Frame(frame_play, bg = '#000000', width = 320, height= 60)

ic_hint = Image.open("icon//hint.png")
ic_hint = ic_hint.resize((35,35))
icon_hint = ImageTk.PhotoImage(ic_hint)
bt_hint = tk.Button(frame_play1, image = icon_hint,bg = '#000000', bd = 0, relief='flat',command = lambda: show_hint())
bt_hint.pack(side = RIGHT, anchor = CENTER)

ic_star = Image.open("icon//star.png")
ic_star = ic_star.resize((35,35))
icon_star = ImageTk.PhotoImage(ic_star)
label_star = tk.Label(frame_play1, image = icon_star,bg = '#000000', bd = 0)
label_star.pack(side = LEFT, anchor = CENTER)

score = 0

label_score = tk.Label(frame_play1, text=score, bg = '#000000', font = "Helvetica 17 bold", foreground="white")
label_score.pack(side = LEFT, anchor = CENTER)

count_score = 0

label_count_score = tk.Label(frame_play1, text="000000", bg = '#000000', font = "Helvetica 20 bold", foreground="white", height = 20, width = 100)
label_count_score.pack(side = BOTTOM, anchor = CENTER)

frame_play1.pack(side = TOP)
frame_play1.propagate(0)#dòng này để đặt frame này không bị thay đổi kích thước
# hết frameplay phần 1

# frameplay phần 2
frame_play2 = Frame(frame_play, bg = '#000000', width = 360, height= 240)
def image_load(question_num):
    global label_photo_a, photo___a, pt_a, photo_a, label_photo_b, photo___b, pt_b, photo_b, label_photo_c, photo___c, pt_c, photo_c, label_photo_d, photo___d, pt_d, photo_d
    qtn = str(question_num)
    photo___a = "photo//" + qtn + "a.jpg"
    photo___b = "photo//" + qtn + "b.jpg"
    photo___c = "photo//" + qtn + "c.jpg"
    photo___d = "photo//" + qtn + "d.jpg"
    

    pt_a = Image.open(photo___a)
    pt_a = pt_a.resize((174, 99))
    photo_a = ImageTk.PhotoImage(pt_a)
    label_photo_a = tk.Label(frame_play2, image = photo_a, bd = 0)
    label_photo_a.place(x=0,y=15)

    pt_b = Image.open(photo___b)
    pt_b = pt_b.resize((174, 99))
    photo_b = ImageTk.PhotoImage(pt_b)
    label_photo_b = tk.Label(frame_play2, image = photo_b, bd = 0)
    label_photo_b.place(x=186,y=15)

    pt_c = Image.open(photo___c)
    pt_c = pt_c.resize((174, 99))
    photo_c = ImageTk.PhotoImage(pt_c)
    label_photo_c = tk.Label(frame_play2, image = photo_c, bd = 0)
    label_photo_c.place(x=0,y=126)

    pt_d = Image.open(photo___d)
    pt_d = pt_d.resize((174, 99))
    photo_d = ImageTk.PhotoImage(pt_d)
    label_photo_d = tk.Label(frame_play2, image = photo_d, bd = 0)
    label_photo_d.place(x=186,y=126)

frame_play2.pack(side = TOP)
frame_play2.propagate(0)
# hết frameplay phần 2

# frameplay phần 3
frame_play3 = Frame(frame_play, bg = '#000000', width = 360, height= 60)
lbl_play30 = tk.Label(frame_play3, text="Answer: ", font = "Helvetica 16 bold", bg = '#000000', foreground="white").pack(side = LEFT)
lbl_play31 = tk.Label(frame_play3, text="", font = "Helvetica 16 bold", bg = '#000000', foreground="white")
lbl_play31.pack(side = LEFT)

frame_play3.pack(side = TOP)
frame_play3.propagate(0)
# hết frameplay phần 3

# frameplay phần 4
frame_play4 = Frame(frame_play, bg = '#000000', width = 363, height= 93)

choseword = "ABCDABCDABCDABCD"
answerword = ""

class button_word():
    def __init__(self, master):
        frame = tk.Frame(master, bg = '#000000', width = 363, height= 93)
        frame.pack()
        self.btw = [[None for _ in range(8)] for _ in range(2)]
        k = 0
        for i in range(2):
            for j in range(8):
                self.btw[i][j] = tk.Button(frame, text=choseword[k], bd = 2, font = "Helvetica 16 bold", foreground="white", bg = '#000000', command=lambda i=i, j=j, aschr = choseword[k]: self.udtas(self.btw[i][j],aschr))
                self.btw[i][j].place(x=45*j, y=45*i , width = 45, height= 45)
                k = k+1 
    def udrbtq(self): #updare button quest
        k = 0
        for i in range(2):
            for j in range(8):
                self.btw[i][j].config(text=choseword[k], command=lambda i=i, j=j, aschr = choseword[k]: self.udtas(self.btw[i][j],aschr)) #aschr = answer char
                self.btw[i][j].place()
                k = k+1
        self.rsbtas()
    def udtas(self, button, aschr): #update answer
        global answerword
        answerword = answerword + aschr
        lbl_play31.config(text = answerword)
        lbl_play31.pack()
        button.config(state=tk.DISABLED)
        btw_enter.config(state=tk.NORMAL)
    def rsbtas(self): #reset button answer
        for i in range(2):
            for j in range(8):
                self.btw[i][j].config(state=tk.NORMAL)
        btw_enter.config(state=tk.DISABLED)

btword = button_word(frame_play4)

frame_play4.pack(side = TOP)
frame_play4.propagate(0)
# hết frameplay phần 4

# frameplay phần 5
frame_play5 = Frame(frame_play, bg = '#000000', width = 350, height= 90)

def bt_reset_click():
    btword.rsbtas()
    global answerword
    answerword = ""
    lbl_play31.config(text = answerword)
    lbl_play31.pack()
    btw_enter.config(state=tk.DISABLED)

pt_reset = PhotoImage(file="icon//reset.gif")
btw_reset = tk.Button(frame_play5, image=pt_reset, bg = '#000000', relief='flat')
btw_reset.config(command=bt_reset_click)
btw_reset.pack(side = LEFT)

pt_enter = PhotoImage(file="icon//enter.gif")
btw_enter = tk.Button(frame_play5, image=pt_enter, bg = '#000000', relief='flat')
btw_enter.config(state=tk.DISABLED)
btw_enter.pack(side = RIGHT)

frame_play5.pack(side = TOP)
frame_play5.propagate(0)
# hết frameplay phần 5  

question_num = 1
question = ""
hint = ""
def update_quest_score(add_score_i, question_num_i, question_i, hint_i):
    global score, label_score, choseword, btword, answerword, question_num, question, hint
    question_num = question_num_i
    question = question_i
    if add_score_i == 1: score = score + get_score_now()
    label_score.config(text=score)
    label_score.pack()
    image_load(question_num)
    choseword = question
    btword.udrbtq()
    answerword = ""
    hint = hint_i
    call_score_couter()
    lbl_play31.config(text = answerword)
    lbl_play31.pack()

def update_last_quest(add_score_i):
    global score, label_score
    if int(add_score_i) == 1: 
        score = score + get_score_now()
        label_score.config(text=score)
        label_score.pack()
    time.sleep(1)

def show_hint():
    global hint, score
    score = score - 313
    if score < 0:
        score = score + 313
        messagebox.showinfo("(ﾉ´･ω･)ﾉ ﾐ ┻━┻", 'Làm gì còn đủ điểm đâu mà đòi coi gợi ý :)\nKiếm đủ 313 điểm đi rồi quay lại đây =))')
    else:
        messagebox.showinfo("(ﾉ´･ω･)ﾉ ﾐ ┻━┻", hint.replace('*',' '))

def get_answerword():
    return answerword

close_thread = 0

def change_close_thread(x):
    global close_thread
    close_thread = x

def get_close_thread():
    global close_thread
    return close_thread

def call_score_couter():
    global close_thread
    change_close_thread(1)
    time.sleep(1)
    change_close_thread(0)
    start_new_thread(score_couter, ())

def ud_score_couter(score_ct):
    label_count_score.config(text=score_ct)
    label_count_score.pack()
    window.update()

def score_couter():
    score_ct = 1000
    while score_ct >= 100:
        start_new_thread(ud_score_couter, (score_ct, ))
        start_new_thread(dongbo, (score_ct, ))
        time.sleep(0.1)
        score_ct -= 1
        if get_close_thread() == 1:
            break

score_now = 0

def dongbo(score_ct):
    global score_now
    score_now = score_ct

def get_score_now():
    global score_now
    return score_now


frame_play.pack(side = TOP)
frame_play.propagate(0)
frame_play.pack_forget() # lệnh ẩn frame
#endregion

#region # frame end game
frame_end_game = Frame(window, bg = '#000000', width = 420, height= 540)

end_game_title = Message(frame_end_game, bg = '#000000', fg = '#ffffff', text = 'END GAME :)', font = "Helvetica 25 bold", width = 360, justify = CENTER)
end_game_title.pack(side = TOP)

user_max_score = 0
user_rank = 0
def text_end_game():
    return (
    'Hết gòi! (ﾉ´･ω･)ﾉ ﾐ ┻━┻\n'
    +'Số điểm lượt này của bạn là: ' + str(score) +'\n'
    +'Số điểm cao nhất của bạn là: ' + str(user_max_score) + '\n'
    +'Với số điểm cao nhất thứ hạng của bạn là: ' + str(user_rank)
)

end_game_result = Message(frame_end_game, bg = '#000000', text = text_end_game(), font = "Helvetica 15 bold", fg = '#ffffff', width = 360, justify = LEFT)
end_game_result.pack(side = TOP)

end_game_ranking = Message(frame_end_game, bg = '#000000', text = 'Vị trí của bạn:', font = "Helvetica 20 bold", fg = '#ffffff', width = 360, justify = CENTER)
end_game_ranking.pack(side = TOP)

rank_a = rank_b = rank_c = 0
rank_name_a = rank_name_b = rank_name_c = 'xxx'
rank_score_a = rank_score_b = rank_score_c = 0

def text_rank():
    return (
    '> #' + str(rank_a) + ' ' + str(rank_name_a) + ' ' + str(rank_score_a) + ' <\n'
    +'> #' + str(rank_b) + ' ' + str(rank_name_b) + ' ' + str(rank_score_b) + ' <\n'
    +'> #' + str(rank_c) + ' ' + str(rank_name_c) + ' ' + str(rank_score_c) + ' <'
)
end_game_ranking_text = Message(frame_end_game, bg = '#000000', text = text_rank(), font = "Helvetica 18 bold", fg = '#ffffff', width = 360, justify = CENTER)
end_game_ranking_text.pack(side = TOP)

end_game_chill = Message(frame_end_game, bg = '#000000', text = """Bình tĩnh!! (ヘ･_･)ヘ┳━┳\nBạn có thể chơi lại mà! (●'◡'●)""", font = "Helvetica 15 bold", fg = '#ffffff', width = 360, justify = CENTER)
end_game_chill.pack(side = TOP)

pt_play_again = PhotoImage(file="icon//playagain.gif")
bt_play_again = tk.Button(frame_end_game, relief='flat',background='#000000',image=pt_play_again)
bt_play_again.pack(side = TOP)

pt_exit = PhotoImage(file="icon//exit.gif")
bt_exit = tk.Button(frame_end_game, relief='flat',background='#000000',image=pt_exit)
bt_exit.pack(side = TOP)

frame_end_game.pack(side = TOP)
frame_end_game.propagate(0)
frame_end_game.pack_forget()

user_name = ''
def start_end_game(data_rank):
    global rank_a, rank_b, rank_c, rank_name_a, rank_name_b, rank_name_c, rank_score_a, rank_score_b, rank_score_c, user_max_score, user_rank, user_name
    frame_play.pack_forget()
    data = data_rank.replace('*',' ')
    data = data.split()
    rank_a = data[0]
    rank_name_a = data[1]
    rank_score_a = data[2]
    rank_b = data[3]
    rank_name_b = data[4]
    rank_score_b = data[5]
    rank_c = data[6]
    rank_name_c = data[7]
    rank_score_c = data[8]
    end_game_ranking_text.config(text = text_rank())
    end_game_ranking_text.pack()
    if user_name == rank_name_a:
        user_max_score = rank_score_a
        user_rank = rank_a
    elif user_name == rank_name_b:
        user_max_score = rank_score_b
        user_rank = rank_b
    end_game_result.config(text = text_end_game())
    end_game_result.pack()
    frame_end_game.pack()

    


#endregion

#window.mainloop()