from tkinter import *       #파이썬에 내장된 GUI 생성 함수
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("시계")

def time():
    string = strftime('%y.%m.%d %a\r%H:%M:%S %p')   # %p는 pm, am 을 뜻함
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("DS-Digital", 80), background = "black", foreground = "cyan")
#폰트명은 폰트 파일 자체의 이름을 사용

label.pack(anchor='center')
#label.pack 은 위젯들을 패킹하여 불필요한 공간을 없앰 / anchor = 'center' 위치지정 = 중앙 을 의미하며 시간이 중앙정렬됨

time()

mainloop()