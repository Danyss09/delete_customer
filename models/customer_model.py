from services.db_config import get_connection

def delete_customer(customer_id):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM customers WHERE id = %s", (customer_id,))
        connection.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Error deleting customer: {e}")
        return False
    finally:
        cursor.close()
        connection.close()