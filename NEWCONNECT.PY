# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:58:50 2023

@author: Shivani_SB
"""
def showall():
    sql= "SELECT * from LOGIN"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The NAME is : ",  dictionary["NAME"])
        print("The EMAIL is : ", dictionary["EMAIL"])
        print("The CONTACT is : ",  dictionary["CONTACT"])
        print("The ADDRESS is : ",  dictionary["ADDRESS"])
        print("The ROLE is : ",  dictionary["ROLE"])
        print("The BRANCH is : ",  dictionary["BRANCH"])
        print("The PASSWORD is : ",  dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmt)
        
def getdetails(email,password):
    sql= "select * from LOGIN where email='{}' and password='{}'".format(email,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The NAME is : ",  dictionary["NAME"])
        print("The EMAIL is : ", dictionary["EMAIL"])
        print("The CONTACT is : ",  dictionary["CONTACT"])
        print("The ADDRESS is : ",  dictionary["ADDRESS"])
        print("The ROLE is : ",  dictionary["ROLE"])
        print("The BRANCH is : ",  dictionary["BRANCH"])
        print("The PASSWORD is : ",  dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmt)
        
def insertdb(conn,NAME,EMAIL,CONTACT,ADDRESS,ROLE,BRANCH,PASSWORD):
    sql= "INSERT into LOGIN VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(NAME,EMAIL,CONTACT,ADDRESS,ROLE,BRANCH,PASSWORD)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))


print("start")
try:
    import ibm_db
    print("hiiiii")
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=ks73281;PWD=Oken02dcpRohIxI0",'','')
    print(conn)
    print("connection successful...")
    #insertdb(conn,"Hari","Hari@gmail.com",'1234567890','Adarsh nagar','Faculty','Civil','1234567')
    # getdetails("Hari@gmail.com",'1234567')
    #showall()

except:
    
    print("Error connecting to the database")