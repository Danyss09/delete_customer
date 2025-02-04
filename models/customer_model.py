from flask import Blueprint, request, jsonify
from models.customer_model import delete_customer
from services.db_config import get_connection, read_customer

customer_controller = Blueprint('customer_controller', __name__)

# Ruta para eliminar un cliente
@customer_controller.route('/delete_customer', methods=['DELETE'])
def delete_customer_route():
    customer_id = request.args.get('customer_id')
    
    if not customer_id:
        return jsonify({'error': 'No customer_id provided'}), 400
    
    try:
        # Llamar al método read_customer antes de eliminar
        customer = read_customer(customer_id)
        if not customer:
            return jsonify({'error': 'Customer not found'}), 404
        
        result = delete_customer(customer_id)
        if result:
            return jsonify({'message': f'Customer {customer_id} deleted successfully.'}), 200
        else:
            return jsonify({'error': 'Customer not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500