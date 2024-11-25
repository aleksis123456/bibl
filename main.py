import sqlite3

conn=sqlite3.connect('biblioteka.db')

conn.execute("INSERT INTO GRAMATAS ( GRAMATAS_ID, NOSAUKUMS, GADS, AUTORA_ID )\
        VALUES(1, 'The Golden Age', 2023, 1 )"); 

conn.execute("INSERT INTO GRAMATAS ( GRAMATAS_ID, NOSAUKUMS, GADS, AUTORA_ID )\
        VALUES(2, 'Sometimes they come back', 2018, 2 )"); 

conn.execute("INSERT INTO GRAMATAS ( GRAMATAS_ID, NOSAUKUMS, GADS, AUTORA_ID )\
        VALUES(3, 'The Great Gatsby', 2024, 3 )"); 

conn.execute("INSERT INTO GRAMATAS ( GRAMATAS_ID, NOSAUKUMS, GADS, AUTORA_ID )\
        VALUES(4, 'The photography', 2023, 4 )"); 

conn.commit()
print("Ieraksti ir izveidoti")

conn.execute("INSERT INTO AUTORS ( AUTORA_ID, VARDS, UZVARDS )\
        VALUES(1, 'Kenneth', 'Grahame' )"); 

conn.execute("INSERT INTO AUTORS ( AUTORA_ID, VARDS, UZVARDS )\
        VALUES(2, 'Stephen', 'King' )"); 

conn.execute("INSERT INTO AUTORS ( AUTORA_ID, VARDS, UZVARDS )\
        VALUES(3, 'Francis', 'Scott Fitzgerald' )"); 

conn.execute("INSERT INTO AUTORS ( AUTORA_ID, VARDS, UZVARDS )\
        VALUES(4, 'Frank', 'Herbert' )"); 

conn.commit()
print("Ieraksti ir izveidoti")


#print('Datubāze ir izveidota!')
#conn.execute('''CREATE TABLE GRAMATAS
             #(GRAMATAS_ID INT PRIMARY KEY  NOT NULL,
             #NOSAUKUMS     TEXT       NOT NULL,
             #GADS       INT        NOT NULL,
             #AUTORA_ID    CHAR(50));''') 
#print('Tabula ir izveidota!')
#print('Datubāze ir izveidota!')
#conn.execute('''CREATE TABLE AUTORS
             #(AUTORA_ID INT PRIMARY KEY  NOT NULL,
             #VARDS     TEXT       NOT NULL,
             #UZVARDS       INT     CHAR(50));''')
               
'''print('Tabula ir izveidota!')'''
'''conn.close'''