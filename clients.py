import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash,request
import secrets

auth = secrets.token_hex(4)
print(auth)




@app.route('/create', methods = ['POST'])
def create():
    try:
        _json = request.json
        _id = _json['customer_id']
        _name = _json['customer_name']
        _number = _json['customer_number']
        _email = _json['customer_email_address']
        if _id and _name and _number and _email and  request.method == 'POST':
            conn = mysql.connect()
            cursor  = conn.cursor()
            slqQuery = "INSERT INTO clients_info (customer_id, customer_name, customer_number, customer_email_address) VALUES(%s, %s, %s, %s)"
            bindData= (_id, _name,_number, _email)
            cursor.execute(slqQuery, bindData)
            conn.commit()
            response = jsonify('Client added successfully')
            response.status_code = 200
            return response
        else:   
            return jsonify("ERROR")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()



@app.route('/get')
def get():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM clients_info")
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get/<int:customer_id>')
def search(customer_id):
    token = request.headers.get('Authorization')
    if token == auth: 
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM clients_info WHERE customer_id =%s", customer_id)
            empRow = cursor.fetchall()
            if empRow:
                return jsonify(empRow), 200
            else:
                return jsonify({'ERROR': 'No clients found.'}), 404
        except Exception as e:
            print(e)
            return jsonify({'ERROR': 'An error occurred while retrieving clients.'}), 500
    else:
        return jsonify({'ERROR': 'Invalid Token'}), 401


@app.route('/update', methods = ['PUT'])
def update():
    try:
        _json = request.json
        _id = _json['customer_id']
        _name = _json['customer_name']
        _number = _json['customer_number']
        _email = _json['customer_email_address']  
        if _id and _name and _number and _email and request.method == 'PUT':
            sqlQuery = "UPDATE clients_info SET customer_id=%s, customer_name=%s, customer_number=%s, customer_email_address=%s WHERE customer_id=%s"
            bindData = (_id, _name, _number, _email, _id)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Client updated successfully!')
            response.status_code = 200
            return response
        else:
            return jsonify("ERROR")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/delete/<int:customer_id>', methods=['DELETE'])
def delete(customer_id):
        try:
            conn = mysql.connect()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            checker = f"SELECT * FROM clients_info WHERE EXISTS (SELECT * FROM clients_info WHERE customer_id = {customer_id})"
            cur.execute(checker)
            exist = cur.fetchall() 
            if exist:
                cur.execute("DELETE FROM clients_info WHERE customer_id =%s", (customer_id,))
                conn.commit()
                response = jsonify('Client deleted successfully!')
                response.status_code = 200
                return response
            else:
                return jsonify('Error: Nonexistent') 
        except Exception as e:
            print(e)
        finally:
            cur.close() 
            conn.close()

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == "__main__":
    app.run(debug=True)