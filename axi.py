from flask import Flask, request
from flask_cors import CORS
import json
#from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/',methods=['POST'])
def Index():
     # request.args.get('ID')
    x = {
  "name": "tony",
  "age": 15,
  "city": "New York"
    }  
    y = json.dumps(x)
    return y  

if __name__ == '__main__':
    app.run(port =3000, debug= True)