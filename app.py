from flask import Flask, render_template, request,session

app = Flask(__name__)
app.secret_key ='a'
def showall():
    sql= "SELECT * from CLOUD"
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
    sql= "INSERT into LOGIN VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(FIRSTNAME,LASTNAME,MOBILENUMBER,GENDER,EMAIL,PASSWORD,DOB,STUDY,YEAROFSTUDY,ADDRESS,ZIP,STATE,COUNTRY)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))
    
    
import ibm_db
#conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=pnz39897;PWD=sjlh0lq7gOhZDrMP",'','')
#conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=pnz39897;PWD=sjlh0lq7gOhZDrMP",'','')
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=ks73281;PWD=Oken02dcpRohIxI0",'','')

print(conn)
print("connection successful...")

@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == "POST":
        NAME = request.form['NAME']
        EMAIL = request.form['EMAIL'] 
        CONTACT = request.form['CONTACT']
        CONTACT  = request.form['ADDRESS']
        ROLE = request.form['ROLE']
        BRANCH = request.form['BRANCH']
        PASSWORD = request.form['PASSWORD']
    
        
        #inp=[FIRSTNAME,last name,mobile number,gender,email,password,date of birth,study,year of study,address,Zip,state,country]
        insertdb(conn,NAME,EMAIL,CONTACT,ROLE,BRANCH,PASSWORD)
        return render_template('login.html')
        

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        sql= "select * from LOGIN where email='{}' and password='{}'".format(email,password)
        stmt = ibm_db.exec_immediate(conn, sql)
        userdetails = ibm_db.fetch_both(stmt)
        print(userdetails)
        if userdetails:
            session['register'] =userdetails["EMAIL"]
            return render_template('userprofile.html',name=userdetails["NAME"],email= userdetails["EMAIL"],contact= userdetails["CONTACT"],address=userdetails["ADDRESS"],role=userdetails["ROLE"],branch=userdetails["BRANCH"])
        else:
            msg = "Incorrect Email id or Password"
            return render_template("login.html", msg=msg)
    return render_template('login.html')


if _name_ =='_main_':
    app.run( debug = True)