from flask import Flask, jsonify
from flask_cors import CORS
from pymodbus.client import ModbusTcpClient
import os

app = Flask(__name__)
CORS(app)

@app.route('/regval', methods=['GET'])
def get_modbus_val():
    modbus_host = os.getenv('MODBUS_HOST')
    modbus_port = int(os.getenv('MODBUS_PORT'))
    modbus_register = int(os.getenv('MODBUS_REGISTER'))
    client = ModbusTcpClient(modbus_host, port=modbus_port)
    connection = client.connect()

    if connection:
        result = client.read_holding_registers(modbus_register, 1, slave=1)  
        client.close()

        if not result.isError():
            return jsonify({'value': result.registers[0]})
        else:
            return jsonify({'error': 'Error reading register'}), 500
    else:
        return jsonify({'error': 'Unable to connect to the Modbus server'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
