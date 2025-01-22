import pymysql
from services.db_config import get_connection

def delete_customer(customer_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # SQL para eliminar un cliente de la base de datos
            sql = "DELETE FROM Customers WHERE CustomerID = %s"
            cursor.execute(sql, (customer_id,))
            connection.commit()
            
            if cursor.rowcount > 0:
                return True  # Cliente eliminado
            else:
                return False  # Cliente no encontrado
    except Exception as e:
        raise Exception(f"Error deleting customer: {str(e)}")
    finally:
        connection.close()
