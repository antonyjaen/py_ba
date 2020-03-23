from flask import Flask, request
from flask_cors import CORS
from db import *
import json
import pymysql

#from flask_cors import CORS



app = Flask(__name__)
CORS(app)
@app.route('/',methods=['GET'])
def Index():
     # request.args.get('ID')
    db=database()
    id=request.args.get('ID')
    res = db.verificar(id)
    print(res)
    return res

if __name__ == '__main__':
    app.run(port =3000, debug= True)