### this is the web-gui @@@ 

import json 
import jsonify 


from flask import Flask ,render_template , redirect, url_for ,jsonify
from flask import request


app = Flask(__name__)




# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login_2.html', error=error)




@app.route('/home') 

def home():
    ## present current bot stats 
    return render_template('home_page.html')








@app.route("/json")
def json_example():
      #  with open('BNBBTCorders.json', 'r') as jsonfile:
       #     file_data = json.loads(jsonfile.read())
        # We can then find the data for the requested date and send it back as json
        
       #return json.dumps(file_data['tickers'])
        with open('BNBBTCorders.json', 'r') as f:
            content = f.read()
            return render_template('stats.html' , content=content)
            






@app.route('/dashboard')
def dashboard():

    return json_example()





@app.route('/api', methods=['GET'])
def add_message():
    with open('BNBBTCorders.json' , 'r') as f_handle:
        content = json.load(f_handle)

    
    print (content)

    return jsonify(content['open_orders'])


if __name__ == "__main__":
    app.run()