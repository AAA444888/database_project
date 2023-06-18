import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def up():
    def submitp():
        def updatep():
            conn = sqlite3.connect('term-project-test.db')
            cursor = conn.cursor()
            print("Opened database successfully")
            try:
                f=True
                T='patient'
                s="UPDATE "+T+" set "
                v0=name_text.get()
                v1=onthchoosen.get()
                v2=bd_text.get()
                v3=phonen.get()
                v4=addresst.get()
                v5=allergy.get()
                v6=mih.get()
                if v0!="":
                    s+="name = '"+v0+"'"
                    f=False
                if v1!="":
                    if f==False:
                        s+=", "
                    s+="sex = '"+v1+"'"
                    f=False
                if v2!="":
                    if f==False:
                        s+=", "
                    s+="born_date = '"+v2+"'"
                    f=False
                if v3!="":
                    if f==False:
                        s+=", "
                    s+="phone = '"+v3+"'"
                if v4!="":
                    if f==False:
                        s+=", "
                    s+="address = '"+v4+"'"
                if v5!="":
                    if f==False:
                        s+=", "
                    s+="allergy_drug = '"+v5+"'"
                if v6!="":
                    if f==False:
                        s+=", "
                    s+="major_illness_history = '"+v6+"'"
                print(s)
                cursor.execute(s+" where id = '"+id+"'")
                conn.commit()
                #顯示更新幾筆
                print("Total number of rows updated :", conn.total_changes)

                cursor = conn.execute(f"SELECT * from {T}")
                print( "Operation done successfully")
                messagebox.showinfo('訊息','更新成功')
                wnd.destroy()
            except:
                messagebox.showinfo('訊息','error')
            cursor.close()
            conn.close()
            
        id=id_text.get()
        conn = sqlite3.connect('term-project-test.db')
        cursor = conn.cursor()
        print("Opened database successfully")
        cursor = cursor.execute(f"SELECT * from patient where ID= '{id}'")
        a=()
        for row in cursor:
            a=row
        if len(a)>=1:
            wnd = tk.Tk()
            wnd.geometry("400x400")
            wnd.title(id+"資料修改")
            
            namet = tk.Label(wnd,text='更新後的名字:')
            namet.place(relx=0.3,rely=0.1,anchor='n')
            name_text = tk.Entry(wnd)
            name_text.place(relx=0.7,rely=0.1,anchor='n')
            
            sext = tk.Label(wnd,text='更新後的性別:')
            sext.place(relx=0.3,rely=0.2,anchor='n')
            n = tk.StringVar()
            onthchoosen = ttk.Combobox(wnd, width = 17, textvariable = n)
            onthchoosen['values'] = ('male', 'female')
            onthchoosen.place(relx=0.7,rely=0.2,anchor='n')
            
            bd = tk.Label(wnd,text='更新後的生日(ex:YYYY-MM-DD):')
            bd.place(relx=0.3,rely=0.3,anchor='n')
            bd_text = tk.Entry(wnd)
            bd_text.place(relx=0.7,rely=0.3,anchor='n')
            
            phone = tk.Label(wnd,text='更新後的手機號碼(ex:09xx-xxx-xxx):')
            phone.place(relx=0.3,rely=0.4,anchor='n')
            phonen = tk.Entry(wnd)
            phonen.place(relx=0.7,rely=0.4,anchor='n')
            
            address = tk.Label(wnd,text='更新後的地址:')
            address.place(relx=0.3,rely=0.5,anchor='n')
            addresst = tk.Entry(wnd)
            addresst.place(relx=0.7,rely=0.5,anchor='n')
            
            allerge = tk.Label(wnd,text='更新後的過敏藥物:')
            allerge.place(relx=0.3,rely=0.6,anchor='n')
            allergy = tk.Entry(wnd)
            allergy.place(relx=0.7,rely=0.6,anchor='n')
            
            mi = tk.Label(wnd,text='更新後的重大傷病紀錄:')
            mi.place(relx=0.3,rely=0.7,anchor='n')
            mih = tk.Entry(wnd)
            mih.place(relx=0.7,rely=0.7,anchor='n')


            button = tk.Button(wnd,text="update",underline=-1,command=updatep)
            button.place(relx=0.3,rely=0.9,anchor='n')            
            button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
            button.place(relx=0.7,rely=0.9,anchor='n')
        else:
            messagebox.showinfo('訊息','查無此人')
        conn.commit()#執行sql語法
        cursor.close()
        conn.close()
                
    wnd = tk.Tk()
    wnd.geometry("400x400")
    wnd.title("資料修改")
    
    idt = tk.Label(wnd,text='請輸入欲更新的ID:')
    idt.place(relx=0.3,rely=0.1,anchor='n')
    id_text = tk.Entry(wnd)
    id_text.place(relx=0.7,rely=0.1,anchor='n')

    button = tk.Button(wnd,text="submit",underline=-1,command=submitp)
    button.place(relx=0.3,rely=0.7,anchor='n')            
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.7,rely=0.7,anchor='n')
    
    wnd.mainloop()
    
def ums():
    def submitms():
        def updatems():
            conn = sqlite3.connect('term-project-test.db')
            cursor = conn.cursor()
            print("Opened database successfully")
            try:
                f=True
                T='medical_staff'
                s="UPDATE "+T+" set "
                v0=name_text.get()
                v1=onthchoosen.get()
                v2=bd_text.get()
                v3=phonen.get()
                v4=addresst.get()
                v5=allergy.get()
                v6=c1.get()
                if v0!="":
                    s+="name = '"+v0+"'"
                    f=False
                if v1!="":
                    if f==False:
                        s+=", "
                    s+="sex = '"+v1+"'"
                    f=False
                if v2!="":
                    if f==False:
                        s+=", "
                    s+="born_date = '"+v2+"'"
                    f=False
                if v3!="":
                    if f==False:
                        s+=", "
                    s+="phone = '"+v3+"'"
                if v4!="":
                    if f==False:
                        s+=", "
                    s+="address = '"+v4+"'"
                if v5!="":
                    if f==False:
                        s+=", "
                    s+="work_place = '"+v5+"'"
                if v6!="":
                    if f==False:
                        s+=", "
                    s+="status = '"+v6+"'"
                print(s)
                cursor.execute(s+" where id = '"+id+"'")
                conn.commit()
                #顯示更新幾筆
                print("Total number of rows updated :", conn.total_changes)

                cursor = conn.execute(f"SELECT * from {T}")
                print( "Operation done successfully")
                messagebox.showinfo('訊息','更新成功')
                wnd.destroy()
            except:
                messagebox.showinfo('訊息','error')
            cursor.close()
            conn.close()
            
        id=id_text.get()
        conn = sqlite3.connect('term-project-test.db')
        cursor = conn.cursor()
        print("Opened database successfully")
        cursor = cursor.execute(f"SELECT * from medical_staff where ID= '{id}'")
        a=()
        for row in cursor:
            a=row
        if len(a)>=1:
            wnd = tk.Tk()
            wnd.geometry("400x400")
            wnd.title(id+"資料修改")
            
            namet = tk.Label(wnd,text='更新後的名字:')
            namet.place(relx=0.3,rely=0.1,anchor='n')
            name_text = tk.Entry(wnd)
            name_text.place(relx=0.7,rely=0.1,anchor='n')
            
            sext = tk.Label(wnd,text='更新後的性別:')
            sext.place(relx=0.3,rely=0.2,anchor='n')
            n = tk.StringVar()
            onthchoosen = ttk.Combobox(wnd, width = 17, textvariable = n)
            onthchoosen['values'] = ('male', 'female')
            onthchoosen.place(relx=0.7,rely=0.2,anchor='n')
            
            bd = tk.Label(wnd,text='更新後的生日(ex:YYYY-MM-DD):')
            bd.place(relx=0.3,rely=0.3,anchor='n')
            bd_text = tk.Entry(wnd)
            bd_text.place(relx=0.7,rely=0.3,anchor='n')
            
            phone = tk.Label(wnd,text='更新後的手機號碼(ex:09xx-xxx-xxx):')
            phone.place(relx=0.3,rely=0.4,anchor='n')
            phonen = tk.Entry(wnd)
            phonen.place(relx=0.7,rely=0.4,anchor='n')
            
            address = tk.Label(wnd,text='更新後的地址:')
            address.place(relx=0.3,rely=0.5,anchor='n')
            addresst = tk.Entry(wnd)
            addresst.place(relx=0.7,rely=0.5,anchor='n')
            
            allerge = tk.Label(wnd,text='更新後的工作地點:')
            allerge.place(relx=0.3,rely=0.6,anchor='n')
            allergy = tk.Entry(wnd)
            allergy.place(relx=0.7,rely=0.6,anchor='n')
            
            mi = tk.Label(wnd,text='更新後的工作狀態:')
            mi.place(relx=0.3,rely=0.7,anchor='n')
            n1 = tk.StringVar()
            c1= ttk.Combobox(wnd, width = 17, textvariable = n1)
            c1['values'] = ('active', 'in-active')
            c1.place(relx=0.7,rely=0.7,anchor='n')

            button = tk.Button(wnd,text="update",underline=-1,command=updatems)
            button.place(relx=0.3,rely=0.9,anchor='n')            
            button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
            button.place(relx=0.7,rely=0.9,anchor='n')
        else:
            messagebox.showinfo('訊息','查無此人')
        conn.commit()#執行sql語法
        cursor.close()
        conn.close()
                
    wnd = tk.Tk()
    wnd.geometry("400x400")
    wnd.title("資料修改")
    
    idt = tk.Label(wnd,text='請輸入欲更新的ID:')
    idt.place(relx=0.3,rely=0.1,anchor='n')
    id_text = tk.Entry(wnd)
    id_text.place(relx=0.7,rely=0.1,anchor='n')

    button = tk.Button(wnd,text="submit",underline=-1,command=submitms)
    button.place(relx=0.3,rely=0.7,anchor='n')            
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.7,rely=0.7,anchor='n')
    
    wnd.mainloop()