import tkinter.ttk as ttk
import time
from tkinter import *

root = Tk()
root.title("덕행 GUI")
root.geometry("640x480")
#progressbar = ttk.Progressbar(root, maximum=100, mode = "indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode = "determinate")
# progressbar.start(10)
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()


p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum =100,length=150, variable = p_var2 )
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.1초 대기

        p_var2.set(i) # progress bar 의 값을 설정
        progressbar2.update() # UI 없데이트
        print(p_var2.get())


btn = Button(root, text="시작", command=btncmd2)
btn.pack()


root.mainloop()

