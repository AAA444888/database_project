import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def ip():
    def submitp():
        conn = sqlite3.connect("term-project-test.db")#連結資料庫
        cursor = conn.cursor()#啟用游標
        print("Opened database successfully")
        try:
            v0='patient'
            v1=id_text.get()
            v2=name_text.get()
            v3=onthchoosen.get()
            v4=bd_text.get()
            v5=phonen.get()
            v6=addresst.get()
            v7=allergy.get()
            v8=mih.get()
            if v1=='' or v2=='' or v3=='' or v4=='':
                messagebox.showinfo('訊息','error')
            else:
                cursor.execute(f"INSERT INTO {v0} VALUES ('{v1}','{v2}','{v3}','{v4}','{v5}','{v6}','{v7}','{v8}')")
                conn.commit()#執行sql語法
                messagebox.showinfo('訊息','新增成功')
                wnd.destroy()
                print("Records created successfully")
        except:
            messagebox.showinfo('訊息','error')
        cursor.close()#關閉游標
        conn.close()#關閉連結
        
    wnd = tk.Tk()
    wnd.geometry("400x400")
    wnd.title("新增資料")
    
    idt = tk.Label(wnd,text='請輸入ID:')
    idt.place(relx=0.3,rely=0.05,anchor='n')
    id_text = tk.Entry(wnd)
    id_text.place(relx=0.7,rely=0.05,anchor='n')

    namet = tk.Label(wnd,text='請輸入姓名:')
    namet.place(relx=0.3,rely=0.15,anchor='n')
    name_text = tk.Entry(wnd)
    name_text.place(relx=0.7,rely=0.15,anchor='n')

    sext = tk.Label(wnd,text='請選擇性別:')
    sext.place(relx=0.3,rely=0.25,anchor='n')
    n = tk.StringVar()
    onthchoosen = ttk.Combobox(wnd, width = 17, textvariable = n)
    onthchoosen['values'] = ('male', 'female')
    onthchoosen.place(relx=0.7,rely=0.25,anchor='n')

    bd = tk.Label(wnd,text='請輸入生日(ex:YYYY-MM-DD):')
    bd.place(relx=0.3,rely=0.35,anchor='n')
    bd_text = tk.Entry(wnd)
    bd_text.place(relx=0.7,rely=0.35,anchor='n')
    
    phone = tk.Label(wnd,text='請輸入手機號碼(ex:09xx-xxx-xxx):')
    phone.place(relx=0.3,rely=0.45,anchor='n')
    phonen = tk.Entry(wnd)
    phonen.place(relx=0.7,rely=0.45,anchor='n')
    
    address = tk.Label(wnd,text='請輸入地址:')
    address.place(relx=0.3,rely=0.55,anchor='n')
    addresst = tk.Entry(wnd)
    addresst.place(relx=0.7,rely=0.55,anchor='n')
    
    allerge = tk.Label(wnd,text='請輸入過敏藥物:')
    allerge.place(relx=0.3,rely=0.65,anchor='n')
    allergy = tk.Entry(wnd)
    allergy.place(relx=0.7,rely=0.65,anchor='n')
    
    mi = tk.Label(wnd,text='重大傷病紀錄:')
    mi.place(relx=0.3,rely=0.75,anchor='n')
    mih = tk.Entry(wnd)
    mih.place(relx=0.7,rely=0.75,anchor='n')

    button = tk.Button(wnd,text="submit",underline=-1,command=submitp)
    button.place(relx=0.4,rely=0.85,anchor='n')
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.6,rely=0.85,anchor='n')
    
def ih():
    def submith():
        conn = sqlite3.connect("term-project-test.db")#連結資料庫
        cursor = conn.cursor()#啟用游標
        print("Opened database successfully")
        try:
            v0='history'
            v1=date_text.get()
            v2=time_text.get()
            v3=pn_text.get()
            v4=pit.get()
            v5=dnt.get()
            v6=illt.get()
            v7=ct.get()
            #匯入資料至資料表
            if v1=='' or v2=='' or v3=='' or v4=='' or v5=='' or v7=='':
                messagebox.showinfo('訊息','error')
            else:
                cursor.execute(f"INSERT INTO {v0} VALUES ('{v1}','{v2}','{v3}','{v4}','{v5}','{v6}','{v7}')")
                conn.commit()#執行sql語法
                messagebox.showinfo('訊息','新增成功')
                wnd.destroy()
                print("Records created successfully")
        except:
            messagebox.showinfo('訊息','error')
        cursor.close()#關閉游標
        conn.close()#關閉連結
        
    wnd = tk.Tk()
    wnd.geometry("400x400")
    wnd.title("新增資料")
    
    datet = tk.Label(wnd,text='請輸入日期(ex:YYYY-MM-DD):')
    datet.place(relx=0.3,rely=0.1,anchor='n')
    date_text = tk.Entry(wnd)
    date_text.place(relx=0.7,rely=0.1,anchor='n')
    
    timet = tk.Label(wnd,text='請輸入時間(ex:hh:mm:ss):')
    timet.place(relx=0.3,rely=0.2,anchor='n')
    time_text = tk.Entry(wnd)
    time_text.place(relx=0.7,rely=0.2,anchor='n')
    
    pn = tk.Label(wnd,text='請輸入病人姓名:')
    pn.place(relx=0.3,rely=0.3,anchor='n')
    pn_text = tk.Entry(wnd)
    pn_text.place(relx=0.7,rely=0.3,anchor='n')
    
    pi = tk.Label(wnd,text='請輸入病人ID:')
    pi.place(relx=0.3,rely=0.4,anchor='n')
    pit = tk.Entry(wnd)
    pit.place(relx=0.7,rely=0.4,anchor='n')
    
    dn = tk.Label(wnd,text='請輸入醫護人員姓名:')
    dn.place(relx=0.3,rely=0.5,anchor='n')
    dnt = tk.Entry(wnd)
    dnt.place(relx=0.7,rely=0.5,anchor='n')
    
    ill = tk.Label(wnd,text='請輸入病症:')
    ill.place(relx=0.3,rely=0.6,anchor='n')
    illt = tk.Entry(wnd)
    illt.place(relx=0.7,rely=0.6,anchor='n')
    
    clinic = tk.Label(wnd,text='請輸入診所:')
    clinic.place(relx=0.3,rely=0.7,anchor='n')
    ct = tk.Entry(wnd)
    ct.place(relx=0.7,rely=0.7,anchor='n')

    button = tk.Button(wnd,text="submit",underline=-1,command=submith)
    button.place(relx=0.4,rely=0.85,anchor='n')
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.6,rely=0.85,anchor='n')
    
def ii():
    def submiti():
        conn = sqlite3.connect("term-project-test.db")#連結資料庫
        cursor = conn.cursor()#啟用游標
        print("Opened database successfully")
        try:
            v0='illness'
            v1=ill_text.get()
            v2=symt.get()
            v3=dt.get()
            if v1=='' or v2=='':
                messagebox.showinfo('訊息','error')
            else:
                cursor.execute(f"INSERT INTO {v0} VALUES ('{v1}','{v2}','{v3}')")
                conn.commit()#執行sql語法
                messagebox.showinfo('訊息','新增成功')
                wnd.destroy()
                print("Records created successfully")
        except:
            messagebox.showinfo('訊息','error')
        cursor.close()#關閉游標
        conn.close()#關閉連結
        
    wnd = tk.Tk()
    wnd.geometry("400x400")
    wnd.title("新增資料")
    
    illn = tk.Label(wnd,text='請輸入病名:')
    illn.place(relx=0.3,rely=0.1,anchor='n')
    ill_text = tk.Entry(wnd)
    ill_text.place(relx=0.7,rely=0.1,anchor='n')
    
    ills = tk.Label(wnd,text='請輸入症狀:')
    ills.place(relx=0.3,rely=0.2,anchor='n')
    symt = tk.Entry(wnd)
    symt.place(relx=0.7,rely=0.2,anchor='n')
    
    drug = tk.Label(wnd,text='請輸入藥單:')
    drug.place(relx=0.3,rely=0.3,anchor='n')
    dt = tk.Entry(wnd)
    dt.place(relx=0.7,rely=0.3,anchor='n')

    button = tk.Button(wnd,text="submit",underline=-1,command=submiti)
    button.place(relx=0.4,rely=0.85,anchor='n')
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.6,rely=0.85,anchor='n')
    
def idrug():
    def submitdrug():
        conn = sqlite3.connect("term-project-test.db")#連結資料庫
        cursor = conn.cursor()#啟用游標
        print("Opened database successfully")
        try:
            v0='drug'
            v1=nt.get()
            v2=idt.get()
            v3=effectt.get()
            v4=st.get()
            #匯入資料至資料表
            if v1=='':
                messagebox.showinfo('訊息','error')
            else:
                cursor.execute(f"INSERT INTO {v0} VALUES ('{v1}','{v2}','{v3}','{v4}')")
                conn.commit()#執行sql語法
                messagebox.showinfo('訊息','新增成功')
                wnd.destroy()
                print("Records created successfully")
        except:
            messagebox.showinfo('訊息','error')
        cursor.close()#關閉游標
        conn.close()#關閉連結
        
    wnd = tk.Tk()
    wnd.geometry("400x400")
    wnd.title("新增資料")
    
    name = tk.Label(wnd,text='請輸入藥物:')
    name.place(relx=0.3,rely=0.1,anchor='n')
    nt = tk.Entry(wnd)
    nt.place(relx=0.7,rely=0.1,anchor='n')
    
    inter = tk.Label(wnd,text='請輸入相互作用藥物:')
    inter.place(relx=0.3,rely=0.2,anchor='n')
    idt = tk.Entry(wnd)
    idt.place(relx=0.7,rely=0.2,anchor='n')
    
    effect = tk.Label(wnd,text='請輸入作用:')
    effect.place(relx=0.3,rely=0.3,anchor='n')
    effectt = tk.Entry(wnd)
    effectt.place(relx=0.7,rely=0.3,anchor='n')
    
    side = tk.Label(wnd,text='請輸入副作用:')
    side.place(relx=0.3,rely=0.4,anchor='n')
    st = tk.Entry(wnd)
    st.place(relx=0.7,rely=0.4,anchor='n')
    
    button = tk.Button(wnd,text="submit",underline=-1,command=submitdrug)
    button.place(relx=0.4,rely=0.85,anchor='n')
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.6,rely=0.85,anchor='n')
    
def ic():
    def submitc():
        conn = sqlite3.connect("term-project-test.db")#連結資料庫
        cursor = conn.cursor()#啟用游標
        print("Opened database successfully")
        try:
            v0='facilities'
            v1=c_text.get()
            v2=pt.get()
            v3=addresst.get()
            if v1=='' or v2=='' or v3=='':
                messagebox.showinfo('訊息','error')
            else:
                cursor.execute(f"INSERT INTO {v0} VALUES ('{v1}','{v2}','{v3}')")
                conn.commit()#執行sql語法
                messagebox.showinfo('訊息','新增成功')
                wnd.destroy()
                print("Records created successfully")
        except:
            messagebox.showinfo('訊息','error')
        cursor.close()#關閉游標
        conn.close()#關閉連結
        
    wnd = tk.Tk()
    wnd.geometry("400x400")
    wnd.title("新增資料")
    
    cn = tk.Label(wnd,text='請輸入醫療單位名稱:')
    cn.place(relx=0.3,rely=0.1,anchor='n')
    c_text = tk.Entry(wnd)
    c_text.place(relx=0.7,rely=0.1,anchor='n')
    
    phone = tk.Label(wnd,text='請輸入電話:')
    phone.place(relx=0.3,rely=0.2,anchor='n')
    pt = tk.Entry(wnd)
    pt.place(relx=0.7,rely=0.2,anchor='n')
    
    address = tk.Label(wnd,text='請輸入地址:')
    address.place(relx=0.3,rely=0.3,anchor='n')
    addresst = tk.Entry(wnd)
    addresst.place(relx=0.7,rely=0.3,anchor='n')

    button = tk.Button(wnd,text="submit",underline=-1,command=submitc)
    button.place(relx=0.4,rely=0.85,anchor='n')
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.6,rely=0.85,anchor='n')
    
def ims():
    def submitms():
        conn = sqlite3.connect("term-project-test.db")#連結資料庫
        cursor = conn.cursor()#啟用游標
        print("Opened database successfully")
        try:
            v0='medical_staff'
            v1=id_text.get()
            v2=name_text.get()
            v3=onthchoosen.get()
            v4=bd_text.get()
            v5=phonen.get()
            v6=addresst.get()
            v7=wp.get()
            v8=c2.get()
            if v1=='' or v2=='' or v3=='' or v4=='' or v7=='':
                messagebox.showinfo('訊息','error')
            else:
                cursor.execute(f"INSERT INTO {v0} VALUES ('{v1}','{v2}','{v3}','{v4}','{v5}','{v6}','{v7}','{v8}')")
                conn.commit()#執行sql語法
                messagebox.showinfo('訊息','新增成功')
                wnd.destroy()
                print("Records created successfully")
        except:
            messagebox.showinfo('訊息','error')
        cursor.close()#關閉游標
        conn.close()#關閉連結
        
    wnd = tk.Tk()
    wnd.geometry("400x400")
    wnd.title("新增資料")
    
    idt = tk.Label(wnd,text='請輸入ID:')
    idt.place(relx=0.3,rely=0.05,anchor='n')
    id_text = tk.Entry(wnd)
    id_text.place(relx=0.7,rely=0.05,anchor='n')

    namet = tk.Label(wnd,text='請輸入姓名:')
    namet.place(relx=0.3,rely=0.15,anchor='n')
    name_text = tk.Entry(wnd)
    name_text.place(relx=0.7,rely=0.15,anchor='n')

    sext = tk.Label(wnd,text='請選擇性別:')
    sext.place(relx=0.3,rely=0.25,anchor='n')
    n = tk.StringVar()
    onthchoosen = ttk.Combobox(wnd, width = 17, textvariable = n)
    onthchoosen['values'] = ('male', 'female')
    onthchoosen.place(relx=0.7,rely=0.25,anchor='n')

    bd = tk.Label(wnd,text='請輸入生日(ex:YYYY-MM-DD):')
    bd.place(relx=0.3,rely=0.35,anchor='n')
    bd_text = tk.Entry(wnd)
    bd_text.place(relx=0.7,rely=0.35,anchor='n')
    
    phone = tk.Label(wnd,text='請輸入手機號碼(ex:09xx-xxx-xxx):')
    phone.place(relx=0.3,rely=0.45,anchor='n')
    phonen = tk.Entry(wnd)
    phonen.place(relx=0.7,rely=0.45,anchor='n')
    
    address = tk.Label(wnd,text='請輸入地址:')
    address.place(relx=0.3,rely=0.55,anchor='n')
    addresst = tk.Entry(wnd)
    addresst.place(relx=0.7,rely=0.55,anchor='n')
    
    work = tk.Label(wnd,text='請輸入工作地點:')
    work.place(relx=0.3,rely=0.65,anchor='n')
    wp = tk.Entry(wnd)
    wp.place(relx=0.7,rely=0.65,anchor='n')
    
    si = tk.Label(wnd,text='工作狀態:')
    si.place(relx=0.3,rely=0.75,anchor='n')
    n2 = tk.StringVar()
    c2 = ttk.Combobox(wnd, width = 17, textvariable = n2)
    c2['values'] = ('active', 'in-active')
    c2.place(relx=0.7,rely=0.75,anchor='n')

    button = tk.Button(wnd,text="submit",underline=-1,command=submitms)
    button.place(relx=0.4,rely=0.85,anchor='n')
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.6,rely=0.85,anchor='n')