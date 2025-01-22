from flask import Flask, request, jsonify, send_file
import pandas as pd
import os

app = Flask(__name__)

# Base de datos temporal (simulación)
activos = []

@app.route('/')
def home():
    return "🚀 API de Gestión de Activos está en línea."

# Endpoint para agregar un activo
@app.route('/agregar_activo', methods=['POST'])
def agregar_activo():
    data = request.json
    activos.append(data)
    return jsonify({"mensaje": "Activo agregado con éxito!", "activos": activos})

# Endpoint para obtener los activos
@app.route('/listar_activos', methods=['GET'])
def listar_activos():
    return jsonify(activos)

# Endpoint para exportar a Excel
@app.route('/exportar_excel', methods=['GET'])
def exportar_excel():
    df = pd.DataFrame(activos)
    filename = "activos.xlsx"
    df.to_excel(filename, index=False)

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
