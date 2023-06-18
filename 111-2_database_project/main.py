import tkinter as tk
import Data.patient as patient
import Data.medical_history as medical_history
import Data.illness as illness
import Data.drug as drug
import Data.facilities as facilities
import Data.medical_staff as medical_staff

wnd = tk.Tk()
wnd.geometry("400x400")
wnd.title("medical management system")

button = tk.Button(wnd,text="病人資料",underline=-1,command=patient.p)
button.place(relx=0.5,rely=0.1,anchor='n')
button = tk.Button(wnd,text="病歷",underline=-1,command=medical_history.mh)
button.place(relx=0.5,rely=0.2,anchor='n')
button = tk.Button(wnd,text="病症",underline=-1,command=illness.i)
button.place(relx=0.5,rely=0.3,anchor='n')
button = tk.Button(wnd,text="藥物",underline=-1,command=drug.d)
button.place(relx=0.5,rely=0.4,anchor='n')
button = tk.Button(wnd,text="診所",underline=-1,command=facilities.c)
button.place(relx=0.5,rely=0.5,anchor='n')
button = tk.Button(wnd,text="醫療人員",underline=-1,command=medical_staff.ms)
button.place(relx=0.5,rely=0.6,anchor='n')

close = tk.Button(wnd,text="關閉",underline=-1,command=wnd.destroy)
close.place(relx=0.5,rely=0.9,anchor="n")

wnd.mainloop()