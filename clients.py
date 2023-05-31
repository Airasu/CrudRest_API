import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash,request


@app.route('/create', methods = ['POST'])
def create_emp():
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
            response = jsonify('Employee added successfully')
            response.status_code = 200
            return response
        else:   
            return jsonify('Error')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()



@app.route('/emp')
def fetch():
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


@app.route('/emp/<int:customer_id>')
def search(customer_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM clients_info WHERE customer_id =%s", customer_id)
        empRow = cursor.fetchone()
        response = jsonify(empRow)
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

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
            return jsonify('Error')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/delete/<int:customer_id>', methods=['DELETE'])
def delete(customer_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clients_info WHERE customer_id=%s", (customer_id,))
        conn.commit()
        response = jsonify('Client deleted successfully!')
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()





if __name__ == "__main__":
    app.run(debug=True)