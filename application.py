from flask import Flask, render_template, request,redirect,session, jsonify
from flask_cors import CORS,cross_origin
import requests
import pymongo

application = Flask(__name__) # initializing a flask app
app=application
app.config['SECRET_KEY'] = "b'\xf0\x95Ix}\xad4\xbc\xbc\xbamX\x06o\xf8W\xe2\xa0\xf8\x08\xca_\x87\x01'"
client = pymongo.MongoClient("mongodb+srv://usernamehimanshu999:pwskills@cluster0.efukwgk.mongodb.net/?retryWrites=true&w=majority")
db = client['practicum_data']
users = db['users']


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
            
            user = db.users.find_one(mydict)
            if user:
                session['input_mail'] = mail
                return redirect('/logedin_practicum.html')
            else:
                return 'Invalid username or password'
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'    
      
    return render_template('logedin_practicum.html')
        
    

@app.route('/logedin_practicum2.html',methods=['POST','GET'])
@cross_origin()
def register_fun():
    if request.method == 'POST':
        information = []
        Fname = request.form['input_name'].replace(" ","")
        Lname = request.form['input_Lname'].replace(" ","")
        mail = request.form['input_mail'].replace(" ","")
        password = request.form['input_password'].replace(" ","")
        conf_pass = request.form['input_Cpassword'].replace(" ","")
        name = Fname + Lname
        if db.users.find_one({'mail_id': mail}):
            return 'Username already exists'
        if conf_pass == password:
            print("pass")
        else:
            return "Password not matched"
        Reg_mydict = {"First_Name": Fname, "Last_Name": Lname, "UserNAME": name, "mail_id": mail,
            "password": password}
        
        db.users.insert_one(Reg_mydict)
    return render_template('logedin_practicum2.html')
        

@app.route('/INDIAN.html',methods = ['POST','GET'])
@cross_origin()
def indian():
        try:
            return render_template("INDIAN.html")
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
        
@app.route('/Order.html',methods = ['POST','GET'])
@cross_origin()
def Order():
        try:
            return render_template("Order.html")
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
        
@app.route('/payment.html',methods = ['POST','GET'])
@cross_origin()
def payment():
    return render_template('payment.html')
        
cart_items = []
total_price = 0

@app.route('/add_to_cart', methods=['POST'])
@cross_origin()
def add_to_cart():
    item = request.json
    cart_items.append(item)
    return jsonify({'message': 'Item added to cart successfully'})

@app.route('/remove_from_cart', methods=['POST'])
@cross_origin()
def remove_from_cart():
    item = request.json
    if item in cart_items:
        cart_items.remove(item)
        return jsonify({'message': 'Item removed from cart successfully'})
    else:
        return jsonify({'message': 'Item not found in cart'})
    
db2 = client['Payment']
orders_collection = db2['orders']


@app.route('/place-order', methods=['POST','GET'])
def place_order():
    if request.method == 'POST':
        order_details = request.json
        orders_collection.insert_one(order_details).inserted_id
        success = process_payment(order_details['totalPrice'])
        jsonify({'success': success})
        return render_template('payment.html')

def process_payment(amount):
    return True

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
	#app.run(debug=True)
