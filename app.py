from flask import Flask, jsonify, request

app = Flask(__name__)

empleados = [
    {"id": 1, "nombre": "Ana Garcia",    "puesto": "Analista de Credito",    "departamento": "Creditos",   "salario": 28000, "activo": True},
    {"id": 2, "nombre": "Carlos Lopez",  "puesto": "Ejecutivo de Cuenta",    "departamento": "Comercial",  "salario": 25000, "activo": True},
    {"id": 3, "nombre": "Maria Torres",  "puesto": "Gerente de Sucursal",    "departamento": "Operaciones","salario": 45000, "activo": True},
    {"id": 4, "nombre": "Luis Mendoza",  "puesto": "Analista de Riesgos",    "departamento": "Riesgos",    "salario": 32000, "activo": True},
    {"id": 5, "nombre": "Sofia Ramirez", "puesto": "Desarrollador DevOps",   "departamento": "Tecnologia", "salario": 38000, "activo": True},
]

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "servicio": "banco-empleados-api"})

@app.route('/empleados', methods=['GET'])
def get_empleados():
    return jsonify({"total": len(empleados), "empleados": empleados})

@app.route('/empleados/<int:emp_id>', methods=['GET'])
def get_empleado(emp_id):
    emp = next((e for e in empleados if e['id'] == emp_id), None)
    if emp is None:
        return jsonify({"error": f"Empleado {emp_id} no encontrado"}), 404
    return jsonify(emp)

@app.route('/empleados', methods=['POST'])
def create_empleado():
    data = request.get_json()
    nuevo = {
        "id": max(e['id'] for e in empleados) + 1,
        "nombre": data['nombre'],
        "puesto": data['puesto'],
        "departamento": data['departamento'],
        "salario": data['salario'],
        "activo": True
    }
    empleados.append(nuevo)
    return jsonify(nuevo), 201

@app.route('/empleados/<int:emp_id>', methods=['PUT'])
def update_empleado(emp_id):
    emp = next((e for e in empleados if e['id'] == emp_id), None)
    if emp is None:
        return jsonify({"error": f"Empleado {emp_id} no encontrado"}), 404
    data = request.get_json()
    emp.update(data)
    return jsonify(emp)

@app.route('/empleados/<int:emp_id>', methods=['DELETE'])
def delete_empleado(emp_id):
    global empleados
    emp = next((e for e in empleados if e['id'] == emp_id), None)
    if emp is None:
        return jsonify({"error": f"Empleado {emp_id} no encontrado"}), 404
    empleados = [e for e in empleados if e['id'] != emp_id]
    return jsonify({"mensaje": f"Empleado {emp_id} eliminado correctamente"})

@app.route('/empleados/departamento/<departamento>', methods=['GET'])
def get_por_departamento(departamento):
    resultado = [e for e in empleados if e['departamento'].lower() == departamento.lower()]
    if not resultado:
        return jsonify({"error": f"No hay empleados en {departamento}"}), 404
    return jsonify({"departamento": departamento, "total": len(resultado), "empleados": resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
