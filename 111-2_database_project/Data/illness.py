import tkinter as tk
import insert
import select
import update

def i():
    wnd = tk.Tk()
    wnd.geometry("400x400")
    wnd.title("病症")

    button = tk.Button(wnd,text="新增",underline=-1,command=insert.ii)
    button.place(relx=0.5,rely=0.1,anchor='n')
    button = tk.Button(wnd,text="查詢",underline=-1,command=select.si)
    button.place(relx=0.5,rely=0.2,anchor='n')
    # button = tk.Button(wnd,text="修改",underline=-1)#,command=queryD.query)
    # button.place(relx=0.5,rely=0.3,anchor='n')

    close = tk.Button(wnd,text="關閉",underline=-1,command=wnd.destroy)
    close.place(relx=0.5,rely=0.9,anchor="n")

    wnd.mainloop()