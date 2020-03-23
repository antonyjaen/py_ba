import pymysql
import json

# prepare a cursor object using cursor() method
#cursor = db.cursor()

# ejecuta el SQL query usando el metodo execute().
#cursor.execute("SELECT VERSION()")

# procesa una unica linea usando el metodo fetchone().
#data = cursor.fetchone()
#print ("Database version : {0}".format(data))
# desconecta del servidor
#db.close()

  # Execute the SQL command
 #  cursor.execute(sql)
   # Commit your changes in the database
   #db.commit()
class database():

    def __init__(self):
        print("se inicio correctamente")
        self.db = pymysql.connect("localhost","root","","test")
        self.cursor = self.db.cursor()

    def verificar(self,id):
        self.cursor.execute("SELECT `id`, `nombre`, `telefono`, `correo` FROM `contactos` WHERE `id`={}".format(id))
        data = self.cursor.fetchall()
        if data[0][0]!="":
            js={ 
                "id": data[0][0],
                "nombre": data[0][1],
                "telefono": data[0][2],
                "correo":data[0][3]
            }
            res = json.dumps(js)
            return res
        else :
            return "errorse"



