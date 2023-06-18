# def drop():
#     import sqlite3
#     #drop table 
#     conn = sqlite3.connect('D.db')#連結資料庫，如果沒有則會建立
#     print ("Opened database successfully")
#     cursor = conn.cursor()#啟用游標
#     cursor.execute("DROP TABLE  IF EXISTS  patient;")
#     cursor.execute("DROP TABLE  IF EXISTS  medical_staff;")
#     cursor.execute("DROP TABLE  IF EXISTS  clinic;")
#     cursor.execute("DROP TABLE  IF EXISTS  p_history;")
#     cursor.execute("DROP TABLE  IF EXISTS  medicine;")
    
#     conn.commit()#執行sql語法，每次執行都要提交sql語法
#     cursor.close()#每次執行都要關閉游標
#     conn.close()#每次執行都要關閉連結

# if __name__=='__main__':
#     drop()