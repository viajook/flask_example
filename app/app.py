from flask import Flask, redirect, jsonify
import mysql.connector

app = Flask(__name__)

index = '''
        <body><h1 style='color:blue'>GTG Online Cafe</h1>  
                <h2 style='color:green'>Dockerizing Flask App is a possibility.</h2> 
                <p>With Docker, we can containerize back-end and front-end applications.</p> 
                <h2>Next Step - Automation</h2>
                <ul style='list-style-type:square'>
                <li>Continuous Integration</li> 
                <li>Continuous Delivery</li> 
        </ul></body>
        '''

def product_data():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'mysql-db',
        'port': '3306',
        'database': 'gtg_db'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT Product_Name, Description FROM product_data')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


@app.route("/")
def home():
    return index #f"<html><body><h1 style='color:blue'>GTG Online Cafe</h1></body></html>"
 
@app.route('/products')
def products():
    return jsonify({'Products': product_data()})

   
@app.route("/via")
def via():
    return redirect("https://mit.via.dk/", code=301)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
    
# may map to a specific port
#app.run(host='0.0.0.0', port=8080)