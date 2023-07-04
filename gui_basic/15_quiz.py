import tkinter.ttk as ttk
import os
from tkinter import *

root = Tk()
root.title("덕행 메모장 만들기")
root.geometry("640x480")

filename = "mynote.txt"

menu = Menu(root)

def fileopen():
    if os.path.isfile(filename): # 파일 있으면 True
        with open(filename,"r", encoding="utf8") as file:
            txt.delete("1.0", END) # txt 위젯 본문 삭제  - 안하면 기존 내용뒤에 append 됨
            txt.insert(END,file.read())

    
def filesave():
    with open(filename,"w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))  #모든 내용 가져와서 저장

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=fileopen)
menu_file.add_command(label="저장", command=filesave)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")

# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right",fill="y")

# 본문 영역
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command= txt.yview)
root.config(menu=menu)

root.mainloop()
