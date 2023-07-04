from tkinter import *

root = Tk()
root.title("덕행 GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended",height=0) 
# select single은 1나만 선택, height = 3 이면 3 list만 보임 안보이는 건 scroll bal 후에 설명
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # listbox.delete(END) # 맨 뒤에 항목을 삭제

    # 갯수 확인
    #print("리스트박스에는", listbox.size())
    #항목 확인 (시작 idx, 끝 idx)
    #print("1번째 부터 3번째 까지의 항목 :",listbox.get(0,2))
    #선택된 항목 확인 (위치로 반환 인덱스)
    print("선택 항목 :",listbox.curselection())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()

