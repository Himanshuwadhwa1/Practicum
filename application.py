from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
import pymongo

application = Flask(__name__) # initializing a flask app
app=application

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin() ### to access to public
def homePage():
    return render_template("practicum1.html")

@app.route('/login.html',methods = ['POST','GET'])
@cross_origin()
def login():
        try:
            return render_template("login.html")
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
        
@app.route('/Register.html',methods = ['POST','GET'])
@cross_origin()
def Register():
        try:
            return render_template("Register.html")
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

@app.route('/logedin_practicum.html',methods = ['POST','GET'])
@cross_origin()
def login_fun():
    if request.method == 'POST':
        try:
            log_info = []
            mail = request.form['input_mail']
            password = request.form['input_pass']
            mydict = {"mail_id": mail,"password": password}
            log_info.append(mydict)
            client = pymongo.MongoClient("mongodb+srv://usernamehimanshu999:pwskills@cluster0.efukwgk.mongodb.net/?retryWrites=true&w=majority")
            db = client['log_data_practicum']
            log_website_col = db['login_user_data_practicum']
            log_website_col.insert_many(log_info)
            return render_template('logedin_practicum.html')
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    else:
        return render_template('login.html')

@app.route('/logedin_practicum2.html',methods=['POST','GET'])
@cross_origin()
def register_fun():
    if request.method == 'POST':
        try:
            information = []
            Fname = request.form['input_name'].replace(" ","")
            Lname = request.form['input_Lname'].replace(" ","")
            mail = request.form['input_mail'].replace(" ","")
            password = request.form['input_password'].replace(" ","")
            conf_pass = request.form['input_Cpassword'].replace(" ","")
            name = Fname + Lname
            if conf_pass == password:
                print("pass")
            else:
                print("Password not matched")
            Reg_mydict = {"First_Name": Fname, "Last_Name": Lname, "UserNAME": name, "mail_id": mail,
                "password": password}
            information.append(Reg_mydict)
            client = pymongo.MongoClient("mongodb+srv://usernamehimanshu999:pwskills@cluster0.efukwgk.mongodb.net/?retryWrites=true&w=majority")
            db = client['data_practicum']
            website_col = db['user_data_practicum']
            website_col.insert_many(information)
            return render_template('logedin_practicum2.html')
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

@app.route('/INDIAN.html',methods = ['POST','GET'])
@cross_origin()
def indian():
        try:
            return render_template("INDIAN.html")
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
	#app.run(debug=True)
