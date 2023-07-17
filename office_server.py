from flask import Flask, render_template,request
import mysql.connector
import registration
from meeting import meet_email

app = Flask(__name__)
number = "7"

conn = mysql.connector.connect(host='localhost',user='root', password='root',database = 'project')
cursor = conn.cursor()

@app.route('/')
def home():
    query = "select * from project.employees"
    cursor.execute(query)
    employees = cursor.fetchall()

    return render_template('home_page.html', employees = employees)


@app.route('/signup')
def sign_up():
    return render_template('signup.html')

@app.route('/meet')
def index_meet():
    return render_template('meeting.html')


@app.route('/signup',methods=["POST"])
def insert():
    """
    Inserts a new employee into the system based on the provided data.

    Returns:
        str: A message indicating the status of the operation.

    Raises:
        str: '500 Internal Server Error' if KeyError occurs while retrieving data from the JSON request.

    """
    try:
        data=request.get_json()
        fName = data['prenume']
        lName = data['nume']
        company = data['companie']
        idManager = (data['idManager'].upper())
        email = data['email']
        registration.Employee(fName,lName,company,idManager,email)
        return 'The user has been processed'
    
    except KeyError:
        return '500 Internal Server Error'

    

@app.route('/gate', methods = ['POST'])
def json_gate():
    """
    Processes JSON data related to gate access and inserts it into the database.

    Returns:
        str: A message indicating the status of the operation.

    Raises:
        str: '500 Internal Server Error' if KeyError occurs while retrieving data from the JSON request.

    """
    try:
        data = request.get_json()
        data_value = data['data']
        sens = data['sens']
        idPerson = data['idPersoana']
        idGate = data['idPoarta']
        data_format = data_value.replace("T", " ").replace("Z", "")
        cursor.execute(f"insert into access values({idPerson},'{sens}', '{data_format}', {int(idGate)})")
        conn.commit()
        return 'The data has been processed'
    
    except KeyError:
        return '500 Internal Server Error'
        
@app.route('/meet', methods = ['POST'])
def meeting():
    """
    Renders a meeting template, retrieves data from a JSON request, and sends meeting emails.

    Returns:
        str: Success message if emails are sent successfully.
    
    Raises:
        str: '500 Internal Server Error' if KeyError occurs while retrieving data from the JSON request.
    """
    try:
        data = request.get_json()
        data_value = data['data']
        hour = data['hour']
        meeting_room = data['meeting_room']
        id_persons = data['id_persons']
        email_content = f'On {data_value} we will have a meeting in room number {meeting_room} at {hour}'
        meet_email(id_persons,'Meeting',email_content)
        return 'The emails has been send'
    
    except KeyError:
        return '500 Internal Server Error'

if __name__ == '__main__':
    app.run(debug=True)
