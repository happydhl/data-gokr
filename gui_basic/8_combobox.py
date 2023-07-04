import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("덕행 GUI")
root.geometry("640x480")

def create_new_file():
    print("새파일을 만듭니다")

menu = Menu(root)
# File 메뉴
menu_file = Menu(menu, tearoff=0) 
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")  # 비 활성 화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)  
menu.add_cascade(label="File",menu=menu_file)

# Edit 메뉴(빈 값)
menu.add_cascade(label="Edit")

root.config(menu=menu)
root.mainloop()

