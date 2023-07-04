import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("덕행 GUI")
root.geometry("640x480")
# 기타 예매 시스템 
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료 되었습니다.")

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진 되었습니다.")
def error():
    msgbox.showerror("에러", "결제 오류")
def okcancel():
    msgbox.askokcancel("확인/취소", "해당 죄석은 유아 동반석입니다. 예매 하시갰습니까?")
def retrycancel():
    msgbox.askretrycancel("재시도/취소", "일시적 요류입니다. 재시도 하시겠습니까?")
def yesno():
    msgbox.askyesno("예 아니오", "해당 좌석은 역방향 입니다. 예매 하시겠습니까?")
def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n 저장 후 프로그램을 종료 하겠습니까?")
    # 네 : 저장 후 종료
    #아니오 : 저장 하지 않고 종료
    #취소 : 프로그램 종료 취소(현재 화면에서 계속 있음)
    print("응답 :",response) # True, False, Noen  예 : 1 , 아니오 0, 그외
    if response == 1:
        print("ok")
    elif response == 0:
        print("아니오")
    else:
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()

