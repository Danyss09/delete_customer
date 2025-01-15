from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Conexión a la base de datos MySQL
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            database="CustomerDeleteDb",
            user="root",  # Cambia según tu configuración
            password="dani0919"  # Cambia según tu configuración
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

# Endpoint para eliminar un cliente
@app.route('/customer/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Customers WHERE CustomerID = %s", (customer_id,))
        conn.commit()
        rows_deleted = cursor.rowcount
        cursor.close()
        conn.close()
        if rows_deleted > 0:
            return jsonify({"message": "Customer deleted successfully!"}), 200
        else:
            return jsonify({"message": "Customer not found"}), 404
    return jsonify({"message": "Failed to connect to database"}), 500

# Iniciar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
