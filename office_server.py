from flask import Flask, render_template,request
import mysql.connector
import registration
app = Flask(__name__)
number = "7"

conn = mysql.connector.connect(host='localhost',user='root', password='root',database = 'project')
cursor = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/person',methods=["POST"])
def insert():
    data=request.get_json()
    fName = data['prenume']
    lName = data['nume']
    company = data['companie']
    idManager = (data['idManager'].upper())
    registration.Employee(fName,lName,company,idManager)
    return 'The user has been processed'

@app.route('/gate', methods = ['POST'])
def json_gate():
    data = request.get_json()
    data_value = data['data']
    sens = data['sens']
    idPerson = data['idPersoana']
    idGate = data['idPoarta']
    data_format = data_value.replace("T", " ").replace("Z", "")
    cursor.execute(f"insert into access values({idPerson},'{sens}', '{data_format}', {int(idGate)})")
    conn.commit()
    return 'The data has been processed'



if __name__ == '__main__':
    app.run(debug=True)
