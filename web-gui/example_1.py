from flask import Flask
from flask import request
 
app = Flask(__name__)
 
@app.route('/get', methods = ['GET'])
def getHandler():
    return 'GET handler'
 
@app.route('/post', methods = ['POST'])
def postHandler():
    return 'POST handler'
 
@app.route('/getpost', methods = ['POST', 'GET'])
def postGetHandler():
    if request.method == 'POST':
        return 'request via POST'
    else:
        return 'request via GET'
 
app.run(host='0.0.0.0', port= 8090)