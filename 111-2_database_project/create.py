def create_():
    import sqlite3
    #drop table 
    conn = sqlite3.connect('term-project-test.db')#連結資料庫，如果沒有則會建立
    print ("Opened database successfully")
    cursor = conn.cursor()#啟用游標
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS patient
        (ID TEXT PRIMARY KEY NOT NULL,
        name TEXT PRIMARY KEY NOT NULL,
        sex TEXT NOT NULL,
        born_date TEXT NOT NULL,
        phone TEXT,
        address TEXT,
        allergy_drug TEXT,
        major_illness_history TEXT,
        FOREIGN KEY (allergy_drug) REFERENCES drug (name));''')
    print ("Table patient created successfully")

    cursor.execute('''CREATE TABLE IF NOT EXISTS medical_staff
        (ID TEXT NOT NULL,
        name TEXT PRIMARY KEY NOT NULL,
        sex TEXT NOT NULL,
        born_date TEXT NOT NULL,
        phone TEXT,
        address TEXT,
        work_place TEXT NOT NULL,
        status TEXT,
        FOREIGN KEY (work_place) REFERENCES facilities (name));''')
    print ("Table medical_staff created successfully")
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS illness
        (name TEXT PRIMARY KEY NOT NULL,
        symptom TEXT NOT NULL,
        therapeutic_drug TEXT,
        FOREIGN KEY (therapeutic_drug) REFERENCES drug (name));''')
    print ("Table illness created successfully")
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS history
        (date TEXT  NOT NULL,
        time TEXT  NOT NULL,
        patient_name TEXT NOT NULL,
        patient_ID TEXT NOT NULL,
        doctor_name TEXT  NOT NULL,
        illness TEXT,
        facility_name TEXT NOT NULL,
        PRIMARY KEY (date, time, doctor_name),
        FOREIGN KEY (patient_name) REFERENCES patient (name),
        FOREIGN KEY (patient_ID) REFERENCES patient (ID),
        FOREIGN KEY (doctor_name) REFERENCES medical_staff (name),
        FOREIGN KEY (illness) REFERENCES illness (name),
        FOREIGN KEY (facility_name) REFERENCES facilities (name));''')
    print ("Table history created successfully")
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS facilities
        (name TEXT PRIMARY KEY NOT NULL,
        phone TEXT NOT NULL,
        address TEXT NOT NULL);''')
    print ("Table facilities created successfully")
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS drug
        (name TEXT PRIMARY KEY NOT NULL,
        interaction_drug TEXT,
        effect TEXT,
        side_effect TEXT);''')
    print ("Table drug created successfully")
    
    conn.commit()#執行sql語法，每次執行都要提交sql語法
    cursor.close()#每次執行都要關閉游標
    conn.close()#每次執行都要關閉連結

if __name__=='__main__':
    create_()