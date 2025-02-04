from flask import Flask
from routes.customer_controller import customer_controller

app = Flask(__name__)

# Registrar el blueprint
app.register_blueprint(customer_controller)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)