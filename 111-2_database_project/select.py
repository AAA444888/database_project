import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def sp():
    def submitp():
        flag=True
        try:
            conn = sqlite3.connect("term-project-test.db")#連結資料庫
            cursor = conn.cursor()#啟用游標
            f=True
            T='patient'
            s="SELECT * from "+T+" where "
            v0=id_text.get()
            v1=name_text.get()
            v2=onthchoosen.get()
            v3=bd_text.get()
            v4=phonen.get()
            v5=addresst.get()
            v6=allergy.get()
            v7=mih.get()
            if v0!="":
                s+="ID = '"+v0+"'"
                f=False
            if v1!="":
                if f==False:
                    s+=" AND "
                s+="name = '"+v1+"'"
                f=False
            if v2!="":
                if f==False:
                    s+=" AND "
                s+="sex = '"+v2+"'"
                f=False
            if v3!="":
                if f==False:
                    s+=" AND "
                s+="born_date = '"+v3+"'"
                f=False
            if v4!="":
                if f==False:
                    s+=" AND "
                s+="phone = '"+v4+"'"
                f=False
            if v5!="":
                if f==False:
                    s+=" AND "
                s+="address = '"+v5+"'"
                f=False
            if v6!="":
                if f==False:
                    s+=" AND "
                s+="allergy_drug = '"+v6+"'"
                f=False
            if v7!="":
                if f==False:
                    s+=" AND "
                s+="major_illness_history = '"+v7+"'"
                f=False
            print(s)
            cursor = cursor.execute(s)
            contacts = []
            for row in cursor:
                s0=row[0]
                s1=row[1]
                s2=row[2]
                s3=row[3]
                s4=row[4]
                s5=row[5]
                s6=row[6]
                s7=row[7]    
                columns = ("ID","name", "sex",'born_date','phone','address','allergy_drug','major_illness_history')
                headers =("ID","name", "sex",'born_date','phone','address','allergy_drug','major_illness_history')
                widthes = (80,120,60,80,100,100,80,130)
                tv = ttk.Treeview(wnd, show="headings",height=16 ,columns=columns)
                for (column, header, width) in zip(columns, headers, widthes):
                    tv.column(column, width=width, anchor="w")
                    tv.heading(column, text=header, anchor="w")
                def inser_data():
                    """插入数据"""
                    contacts.append(tuple([s0, s1, s2, s3, s4, s5, s6, s7]))
                    for i, v in enumerate(contacts):
                        print(i,v)
                        tv.insert('', i,values=v)
                tv.place(relx=0.5,rely=0.1,anchor= 'n')
                inser_data()
                conn.commit()#執行sql語法
                flag=False        
        except:
            messagebox.showinfo('訊息','error')
        cursor.close()#關閉游標
        conn.close()#關閉連結
        if flag==True:
            messagebox.showinfo('訊息','查無此人')
        
    wnd = tk.Tk()
    wnd.geometry("900x400")
    wnd.title("資料查詢")

    idt = tk.Label(wnd,text='欲查詢的ID:')
    idt.place(relx=0.3,rely=0.1,anchor='n')
    id_text = tk.Entry(wnd)
    id_text.place(relx=0.7,rely=0.1,anchor='n')
    
    namet = tk.Label(wnd,text='欲查詢的名字:')
    namet.place(relx=0.3,rely=0.2,anchor='n')
    name_text = tk.Entry(wnd)
    name_text.place(relx=0.7,rely=0.2,anchor='n')
    
    sext = tk.Label(wnd,text='欲查詢的性別:')
    sext.place(relx=0.3,rely=0.3,anchor='n')
    n = tk.StringVar()
    onthchoosen = ttk.Combobox(wnd, width = 17, textvariable = n)
    onthchoosen['values'] = ('male', 'female')
    onthchoosen.place(relx=0.7,rely=0.3,anchor='n')
    
    bd = tk.Label(wnd,text='欲查詢的生日(ex:YYYY-MM-DD):')
    bd.place(relx=0.3,rely=0.4,anchor='n')
    bd_text = tk.Entry(wnd)
    bd_text.place(relx=0.7,rely=0.4,anchor='n')
    
    phone = tk.Label(wnd,text='欲查詢的手機號碼(ex:09xx-xxx-xxx):')
    phone.place(relx=0.3,rely=0.5,anchor='n')
    phonen = tk.Entry(wnd)
    phonen.place(relx=0.7,rely=0.5,anchor='n')
    
    address = tk.Label(wnd,text='欲查詢的地址:')
    address.place(relx=0.3,rely=0.6,anchor='n')
    addresst = tk.Entry(wnd)
    addresst.place(relx=0.7,rely=0.6,anchor='n')
    
    allerge = tk.Label(wnd,text='欲查詢的過敏藥物:')
    allerge.place(relx=0.3,rely=0.7,anchor='n')
    allergy = tk.Entry(wnd)
    allergy.place(relx=0.7,rely=0.7,anchor='n')
    
    mi = tk.Label(wnd,text='欲查詢的重大傷病紀錄:')
    mi.place(relx=0.3,rely=0.8,anchor='n')
    mih = tk.Entry(wnd)
    mih.place(relx=0.7,rely=0.8,anchor='n')

    button = tk.Button(wnd,text="submit",underline=-1,command=submitp)
    button.place(relx=0.4,rely=0.9,anchor='n')            
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.6,rely=0.9,anchor='n')

    wnd.mainloop()
    
def sh():
    def submith():
        flag=True
        try:
            conn = sqlite3.connect("term-project-test.db")#連結資料庫
            cursor = conn.cursor()#啟用游標
            f=True
            T='history'
            s="SELECT * from "+T+" where "
            v0=date_text.get()
            v1=time_text.get()
            v2=pn_text.get()
            v3=pit.get()
            v4=dnt.get()
            v5=illt.get()
            v6=ct.get()
            if v0!="":
                s+="date = '"+v0+"'"
                f=False
            if v1!="":
                if f==False:
                    s+=" AND "
                s+="time = '"+v1+"'"
                f=False
            if v2!="":
                if f==False:
                    s+=" AND "
                s+="patient_name = '"+v2+"'"
                f=False
            if v3!="":
                if f==False:
                    s+=" AND "
                s+="patient_ID = '"+v3+"'"
                f=False
            if v4!="":
                if f==False:
                    s+=" AND "
                s+="doctor_name = '"+v4+"'"
                f=False
            if v5!="":
                if f==False:
                    s+=" AND "
                s+="illness = '"+v5+"'"
                f=False
            if v6!="":
                if f==False:
                    s+=" AND "
                s+="facility_name = '"+v6+"'"
                f=False
            print(s)
            cursor = cursor.execute(s)
            contacts = []
            for row in cursor:
                s0=row[0]
                s1=row[1]
                s2=row[2]
                s3=row[3]
                s4=row[4]
                s5=row[5]
                s6=row[6]   
                columns = ("date","time", "patient_name",'patient_ID','doctor_name','illness','facility_name')
                headers =("date","time", "patient_name",'patient_ID','doctor_name','illness','facility_name')
                widthes = (100,100,100,100,100,100,100)
                tv = ttk.Treeview(wnd, show="headings",height=16 ,columns=columns)
                for (column, header, width) in zip(columns, headers, widthes):
                    tv.column(column, width=width, anchor="w")
                    tv.heading(column, text=header, anchor="w")
                def inser_data():
                    """插入数据"""
                    contacts.append(tuple([s0, s1, s2, s3, s4, s5, s6]))
                    for i, v in enumerate(contacts):
                        print(i,v)
                        tv.insert('', i,values=v)
                tv.place(relx=0.5,rely=0.1,anchor= 'n')
                inser_data()
                conn.commit()#執行sql語法
                flag=False        
        except:
            messagebox.showinfo('訊息','error')
        cursor.close()#關閉游標
        conn.close()#關閉連結
        if flag==True:
            messagebox.showinfo('訊息','查無此資料')
        
    wnd = tk.Tk()
    wnd.geometry("900x400")
    wnd.title("資料查詢")

    datet = tk.Label(wnd,text='欲查詢的日期(ex:YYYY-MM-DD):')
    datet.place(relx=0.3,rely=0.1,anchor='n')
    date_text = tk.Entry(wnd)
    date_text.place(relx=0.7,rely=0.1,anchor='n')
    
    timet = tk.Label(wnd,text='欲查詢的時間(ex:hh:mm:ss):')
    timet.place(relx=0.3,rely=0.2,anchor='n')
    time_text = tk.Entry(wnd)
    time_text.place(relx=0.7,rely=0.2,anchor='n')
    
    pn = tk.Label(wnd,text='欲查詢的病人姓名:')
    pn.place(relx=0.3,rely=0.3,anchor='n')
    pn_text = tk.Entry(wnd)
    pn_text.place(relx=0.7,rely=0.3,anchor='n')
    
    pi = tk.Label(wnd,text='欲查詢的病人ID:')
    pi.place(relx=0.3,rely=0.4,anchor='n')
    pit = tk.Entry(wnd)
    pit.place(relx=0.7,rely=0.4,anchor='n')
    
    dn = tk.Label(wnd,text='欲查詢的醫護人員姓名:')
    dn.place(relx=0.3,rely=0.5,anchor='n')
    dnt = tk.Entry(wnd)
    dnt.place(relx=0.7,rely=0.5,anchor='n')
    
    ill = tk.Label(wnd,text='欲查詢的病症:')
    ill.place(relx=0.3,rely=0.6,anchor='n')
    illt = tk.Entry(wnd)
    illt.place(relx=0.7,rely=0.6,anchor='n')
    
    clinic = tk.Label(wnd,text='欲查詢的診所:')
    clinic.place(relx=0.3,rely=0.7,anchor='n')
    ct = tk.Entry(wnd)
    ct.place(relx=0.7,rely=0.7,anchor='n')

    button = tk.Button(wnd,text="submit",underline=-1,command=submith)
    button.place(relx=0.4,rely=0.9,anchor='n')            
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.6,rely=0.9,anchor='n')

    wnd.mainloop()

def si():
    def submiti():
        flag=True
        try:
            conn = sqlite3.connect("term-project-test.db")#連結資料庫
            cursor = conn.cursor()#啟用游標
            f=True
            T='illness'
            s="SELECT * from "+T+" where "
            v1=ill_text.get()
            v2=symt.get()
            v3=dt.get()
            if v1!="":
                s+="name = '"+v1+"'"
                f=False
            if v2!="":
                if f==False:
                    s+=" AND "
                s+="symptom = '"+v2+"'"
                f=False
            if v3!="":
                if f==False:
                    s+=" AND "
                s+="therapeutic_drug = '"+v3+"'"
                f=False
            print(s)
            cursor = cursor.execute(s)
            contacts = []
            for row in cursor:
                s0=row[0]
                s1=row[1]
                s2=row[2]  
                columns = ("name", "symptom",'therapeutic_drug')
                headers =("name", "symptom",'therapeutic_drug')
                widthes = (200,200,200)
                tv = ttk.Treeview(wnd, show="headings",height=16 ,columns=columns)
                for (column, header, width) in zip(columns, headers, widthes):
                    tv.column(column, width=width, anchor="w")
                    tv.heading(column, text=header, anchor="w")
                def inser_data():
                    """插入数据"""
                    contacts.append(tuple([s0, s1, s2]))
                    for i, v in enumerate(contacts):
                        print(i,v)
                        tv.insert('', i,values=v)
                tv.place(relx=0.5,rely=0.1,anchor= 'n')
                inser_data()
                conn.commit()#執行sql語法
                flag=False        
        except:
            messagebox.showinfo('訊息','error')
        cursor.close()#關閉游標
        conn.close()#關閉連結
        if flag==True:
            messagebox.showinfo('訊息','查無此資料')
        
    wnd = tk.Tk()
    wnd.geometry("900x400")
    wnd.title("資料查詢")

    illn = tk.Label(wnd,text='欲查詢的病名:')
    illn.place(relx=0.3,rely=0.1,anchor='n')
    ill_text = tk.Entry(wnd)
    ill_text.place(relx=0.7,rely=0.1,anchor='n')
    
    ills = tk.Label(wnd,text='欲查詢的症狀:')
    ills.place(relx=0.3,rely=0.2,anchor='n')
    symt = tk.Entry(wnd)
    symt.place(relx=0.7,rely=0.2,anchor='n')
    
    drug = tk.Label(wnd,text='欲查詢的藥單:')
    drug.place(relx=0.3,rely=0.3,anchor='n')
    dt = tk.Entry(wnd)
    dt.place(relx=0.7,rely=0.3,anchor='n')

    button = tk.Button(wnd,text="submit",underline=-1,command=submiti)
    button.place(relx=0.4,rely=0.9,anchor='n')            
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.6,rely=0.9,anchor='n')

    wnd.mainloop()
    
def sdrug():
    def submitdrug():
        flag=True
        try:
            conn = sqlite3.connect("term-project-test.db")#連結資料庫
            cursor = conn.cursor()#啟用游標
            f=True
            T='drug'
            s="SELECT * from "+T+" where "
            v1=nt.get()
            v2=idt.get()
            v3=effectt.get()
            v4=st.get()
            if v1!="":
                s+="name = '"+v1+"'"
                f=False
            if v2!="":
                if f==False:
                    s+=" AND "
                s+="interaction_drug = '"+v2+"'"
                f=False
            if v3!="":
                if f==False:
                    s+=" AND "
                s+="effect = '"+v3+"'"
                f=False
            if v4!="":
                if f==False:
                    s+=" AND "
                s+="side_effect = '"+v4+"'"
                f=False
            print(s)
            cursor = cursor.execute(s)
            contacts = []
            for row in cursor:
                s0=row[0]
                s1=row[1]
                s2=row[2]  
                s3=row[3] 
                columns = ("name", "interaction_drug ",'effect','side_effect')
                headers = ("name", "interaction_drug ",'effect','side_effect')
                widthes = (200,200,200,200)
                tv = ttk.Treeview(wnd, show="headings",height=16 ,columns=columns)
                for (column, header, width) in zip(columns, headers, widthes):
                    tv.column(column, width=width, anchor="w")
                    tv.heading(column, text=header, anchor="w")
                def inser_data():
                    """插入数据"""
                    contacts.append(tuple([s0, s1, s2, s3]))
                    for i, v in enumerate(contacts):
                        print(i,v)
                        tv.insert('', i,values=v)
                tv.place(relx=0.5,rely=0.1,anchor= 'n')
                inser_data()
                conn.commit()#執行sql語法
                flag=False        
        except:
            messagebox.showinfo('訊息','error')
        cursor.close()#關閉游標
        conn.close()#關閉連結
        if flag==True:
            messagebox.showinfo('訊息','查無此資料')
        
    wnd = tk.Tk()
    wnd.geometry("900x400")
    wnd.title("資料查詢")

    name = tk.Label(wnd,text='欲查詢的藥物:')
    name.place(relx=0.3,rely=0.1,anchor='n')
    nt = tk.Entry(wnd)
    nt.place(relx=0.7,rely=0.1,anchor='n')
    
    inter = tk.Label(wnd,text='欲查詢的相互作用藥物:')
    inter.place(relx=0.3,rely=0.2,anchor='n')
    idt = tk.Entry(wnd)
    idt.place(relx=0.7,rely=0.2,anchor='n')
    
    effect = tk.Label(wnd,text='欲查詢的作用:')
    effect.place(relx=0.3,rely=0.3,anchor='n')
    effectt = tk.Entry(wnd)
    effectt.place(relx=0.7,rely=0.3,anchor='n')
    
    side = tk.Label(wnd,text='欲查詢的副作用:')
    side.place(relx=0.3,rely=0.4,anchor='n')
    st = tk.Entry(wnd)
    st.place(relx=0.7,rely=0.4,anchor='n')
    
    button = tk.Button(wnd,text="submit",underline=-1,command=submitdrug)
    button.place(relx=0.4,rely=0.9,anchor='n')            
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.6,rely=0.9,anchor='n')

    wnd.mainloop()
    
def sc():
    def submiti():
        flag=True
        try:
            conn = sqlite3.connect("term-project-test.db")#連結資料庫
            cursor = conn.cursor()#啟用游標
            f=True
            T='facilities'
            s="SELECT * from "+T+" where "
            v1=c_text.get()
            v2=pt.get()
            v3=addresst.get()
            if v1!="":
                s+="name = '"+v1+"'"
                f=False
            if v2!="":
                if f==False:
                    s+=" AND "
                s+="phone = '"+v2+"'"
                f=False
            if v3!="":
                if f==False:
                    s+=" AND "
                s+="address = '"+v3+"'"
                f=False
            print(s)
            cursor = cursor.execute(s)
            contacts = []
            for row in cursor:
                s0=row[0]
                s1=row[1]
                s2=row[2]  
                columns = ("name", "phone",'address')
                headers =("name", "phone",'address')
                widthes = (200,200,200)
                tv = ttk.Treeview(wnd, show="headings",height=16 ,columns=columns)
                for (column, header, width) in zip(columns, headers, widthes):
                    tv.column(column, width=width, anchor="w")
                    tv.heading(column, text=header, anchor="w")
                def inser_data():
                    """插入数据"""
                    contacts.append(tuple([s0, s1, s2]))
                    for i, v in enumerate(contacts):
                        print(i,v)
                        tv.insert('', i,values=v)
                tv.place(relx=0.5,rely=0.1,anchor= 'n')
                inser_data()
                conn.commit()#執行sql語法
                flag=False        
        except:
            messagebox.showinfo('訊息','error')
        cursor.close()#關閉游標
        conn.close()#關閉連結
        if flag==True:
            messagebox.showinfo('訊息','查無此資料')
        
    wnd = tk.Tk()
    wnd.geometry("900x400")
    wnd.title("資料查詢")

    cn = tk.Label(wnd,text='欲查詢的醫療單位名稱:')
    cn.place(relx=0.3,rely=0.1,anchor='n')
    c_text = tk.Entry(wnd)
    c_text.place(relx=0.7,rely=0.1,anchor='n')
    
    phone = tk.Label(wnd,text='欲查詢的電話:')
    phone.place(relx=0.3,rely=0.2,anchor='n')
    pt = tk.Entry(wnd)
    pt.place(relx=0.7,rely=0.2,anchor='n')
    
    address = tk.Label(wnd,text='欲查詢的地址:')
    address.place(relx=0.3,rely=0.3,anchor='n')
    addresst = tk.Entry(wnd)
    addresst.place(relx=0.7,rely=0.3,anchor='n')

    button = tk.Button(wnd,text="submit",underline=-1,command=submiti)
    button.place(relx=0.4,rely=0.9,anchor='n')            
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.6,rely=0.9,anchor='n')

    wnd.mainloop()
    
def sms():
    def submitp():
        flag=True
        try:
            conn = sqlite3.connect("term-project-test.db")#連結資料庫
            cursor = conn.cursor()#啟用游標
            f=True
            T='medical_staff'
            s="SELECT * from "+T+" where "
            v0=id_text.get()
            v1=name_text.get()
            v2=onthchoosen.get()
            v3=bd_text.get()
            v4=phonen.get()
            v5=addresst.get()
            v6=wp.get()
            v7=c2.get()
            if v0!="":
                s+="ID = '"+v0+"'"
                f=False
            if v1!="":
                if f==False:
                    s+=" AND "
                s+="name = '"+v1+"'"
                f=False
            if v2!="":
                if f==False:
                    s+=" AND "
                s+="sex = '"+v2+"'"
                f=False
            if v3!="":
                if f==False:
                    s+=" AND "
                s+="born_date = '"+v3+"'"
                f=False
            if v4!="":
                if f==False:
                    s+=" AND "
                s+="phone = '"+v4+"'"
                f=False
            if v5!="":
                if f==False:
                    s+=" AND "
                s+="address = '"+v5+"'"
                f=False
            if v6!="":
                if f==False:
                    s+=" AND "
                s+="work_place = '"+v6+"'"
                f=False
            if v7!="":
                if f==False:
                    s+=" AND "
                s+="status = '"+v7+"'"
                f=False
            print(s)
            cursor = cursor.execute(s)
            contacts = []
            for row in cursor:
                s0=row[0]
                s1=row[1]
                s2=row[2]
                s3=row[3]
                s4=row[4]
                s5=row[5]
                s6=row[6]
                s7=row[7]    
                columns = ("ID","name", "sex",'born_date','phone','address','work_place','status')
                headers =("ID","name", "sex",'born_date','phone','address','work_place','status')
                widthes = (80,120,60,80,100,100,80,130)
                tv = ttk.Treeview(wnd, show="headings",height=17 ,columns=columns)
                for (column, header, width) in zip(columns, headers, widthes):
                    tv.column(column, width=width, anchor="w")
                    tv.heading(column, text=header, anchor="w")
                def inser_data():
                    """插入数据"""
                    contacts.append(tuple([s0, s1, s2, s3, s4, s5, s6, s7]))
                    for i, v in enumerate(contacts):
                        print(i,v)
                        tv.insert('', i,values=v)
                tv.place(relx=0.5,rely=0.05,anchor= 'n')
                inser_data()
                conn.commit()#執行sql語法
                flag=False        
        except:
            messagebox.showinfo('訊息','error')
        cursor.close()#關閉游標
        conn.close()#關閉連結
        if flag==True:
            messagebox.showinfo('訊息','查無此人')
        
    wnd = tk.Tk()
    wnd.geometry("900x400")
    wnd.title("資料查詢")

    idt = tk.Label(wnd,text='欲查詢的ID:')
    idt.place(relx=0.3,rely=0.05,anchor='n')
    id_text = tk.Entry(wnd)
    id_text.place(relx=0.7,rely=0.05,anchor='n')

    namet = tk.Label(wnd,text='欲查詢的姓名:')
    namet.place(relx=0.3,rely=0.15,anchor='n')
    name_text = tk.Entry(wnd)
    name_text.place(relx=0.7,rely=0.15,anchor='n')

    sext = tk.Label(wnd,text='欲查詢的性別:')
    sext.place(relx=0.3,rely=0.25,anchor='n')
    n = tk.StringVar()
    onthchoosen = ttk.Combobox(wnd, width = 17, textvariable = n)
    onthchoosen['values'] = ('male', 'female')
    onthchoosen.place(relx=0.7,rely=0.25,anchor='n')

    bd = tk.Label(wnd,text='欲查詢的生日(ex:YYYY-MM-DD):')
    bd.place(relx=0.3,rely=0.35,anchor='n')
    bd_text = tk.Entry(wnd)
    bd_text.place(relx=0.7,rely=0.35,anchor='n')
    
    phone = tk.Label(wnd,text='欲查詢的手機號碼(ex:09xx-xxx-xxx):')
    phone.place(relx=0.3,rely=0.45,anchor='n')
    phonen = tk.Entry(wnd)
    phonen.place(relx=0.7,rely=0.45,anchor='n')
    
    address = tk.Label(wnd,text='欲查詢的地址:')
    address.place(relx=0.3,rely=0.55,anchor='n')
    addresst = tk.Entry(wnd)
    addresst.place(relx=0.7,rely=0.55,anchor='n')
    
    work = tk.Label(wnd,text='欲查詢的工作地點:')
    work.place(relx=0.3,rely=0.65,anchor='n')
    wp = tk.Entry(wnd)
    wp.place(relx=0.7,rely=0.65,anchor='n')
    
    si = tk.Label(wnd,text='欲查詢的工作狀態:')
    si.place(relx=0.3,rely=0.75,anchor='n')
    n2 = tk.StringVar()
    c2 = ttk.Combobox(wnd, width = 17, textvariable = n2)
    c2['values'] = ('active', 'in-active')
    c2.place(relx=0.7,rely=0.75,anchor='n')

    button = tk.Button(wnd,text="submit",underline=-1,command=submitp)
    button.place(relx=0.4,rely=0.9,anchor='n')            
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.6,rely=0.9,anchor='n')

    wnd.mainloop()