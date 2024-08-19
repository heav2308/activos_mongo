from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Configuración de MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['gestion_activos']

# Rutas para las colecciones

@app.route('/')
def home():
    return render_template('index.html')

# Cliente
@app.route('/cliente', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_cliente():
    if request.method == 'POST':
        data = request.json
        result = db.Cliente.insert_one(data)
        return jsonify({"_id": str(result.inserted_id)}), 201
    elif request.method == 'GET':
        documents = list(db.Cliente.find())
        for doc in documents:
            doc['_id'] = str(doc['_id'])
        return jsonify(documents)
    elif request.method == 'PUT':
        id = request.args.get('id')
        data = request.json
        result = db.Cliente.update_one({"_id": ObjectId(id)}, {"$set": data})
        if result.matched_count:
            return jsonify({"message": "Documento actualizado"})
        else:
            return jsonify({"error": "Documento no encontrado"}), 404
    elif request.method == 'DELETE':
        id = request.args.get('id')
        result = db.Cliente.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return jsonify({"message": "Documento eliminado"})
        else:
            return jsonify({"error": "Documento no encontrado"}), 404

# Activo
@app.route('/activo', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_activo():
    if request.method == 'POST':
        data = request.json
        result = db.Activo.insert_one(data)
        return jsonify({"_id": str(result.inserted_id)}), 201
    elif request.method == 'GET':
        documents = list(db.Activo.find())
        for doc in documents:
            doc['_id'] = str(doc['_id'])
        return jsonify(documents)
    elif request.method == 'PUT':
        id = request.args.get('id')
        data = request.json
        result = db.Activo.update_one({"_id": ObjectId(id)}, {"$set": data})
        if result.matched_count:
            return jsonify({"message": "Documento actualizado"})
        else:
            return jsonify({"error": "Documento no encontrado"}), 404
    elif request.method == 'DELETE':
        id = request.args.get('id')
        result = db.Activo.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return jsonify({"message": "Documento eliminado"})
        else:
            return jsonify({"error": "Documento no encontrado"}), 404

# Accion
@app.route('/accion', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_accion():
    if request.method == 'POST':
        data = request.json
        result = db.Accion.insert_one(data)
        return jsonify({"_id": str(result.inserted_id)}), 201
    elif request.method == 'GET':
        documents = list(db.Accion.find())
        for doc in documents:
            doc['_id'] = str(doc['_id'])
        return jsonify(documents)
    elif request.method == 'PUT':
        id = request.args.get('id')
        data = request.json
        result = db.Accion.update_one({"_id": ObjectId(id)}, {"$set": data})
        if result.matched_count:
            return jsonify({"message": "Documento actualizado"})
        else:
            return jsonify({"error": "Documento no encontrado"}), 404
    elif request.method == 'DELETE':
        id = request.args.get('id')
        result = db.Accion.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return jsonify({"message": "Documento eliminado"})
        else:
            return jsonify({"error": "Documento no encontrado"}), 404

# Bono
@app.route('/bono', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_bono():
    if request.method == 'POST':
        data = request.json
        result = db.Bono.insert_one(data)
        return jsonify({"_id": str(result.inserted_id)}), 201
    elif request.method == 'GET':
        documents = list(db.Bono.find())
        for doc in documents:
            doc['_id'] = str(doc['_id'])
        return jsonify(documents)
    elif request.method == 'PUT':
        id = request.args.get('id')
        data = request.json
        result = db.Bono.update_one({"_id": ObjectId(id)}, {"$set": data})
        if result.matched_count:
            return jsonify({"message": "Documento actualizado"})
        else:
            return jsonify({"error": "Documento no encontrado"}), 404
    elif request.method == 'DELETE':
        id = request.args.get('id')
        result = db.Bono.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return jsonify({"message": "Documento eliminado"})
        else:
            return jsonify({"error": "Documento no encontrado"}), 404

# Categoria
@app.route('/categoria', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_categoria():
    if request.method == 'POST':
        data = request.json
        result = db.Categoria.insert_one(data)
        return jsonify({"_id": str(result.inserted_id)}), 201
    elif request.method == 'GET':
        documents = list(db.Categoria.find())
        for doc in documents:
            doc['_id'] = str(doc['_id'])
        return jsonify(documents)
    elif request.method == 'PUT':
        id = request.args.get('id')
        data = request.json
        result = db.Categoria.update_one({"_id": ObjectId(id)}, {"$set": data})
        if result.matched_count:
            return jsonify({"message": "Documento actualizado"})
        else:
            return jsonify({"error": "Documento no encontrado"}), 404
    elif request.method == 'DELETE':
        id = request.args.get('id')
        result = db.Categoria.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return jsonify({"message": "Documento eliminado"})
        else:
            return jsonify({"error": "Documento no encontrado"}), 404

# Deposito Bancario
@app.route('/deposito_bancario', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_deposito_bancario():
    if request.method == 'POST':
        data = request.json
        result = db.DepositoBancario.insert_one(data)
        return jsonify({"_id": str(result.inserted_id)}), 201
    elif request.method == 'GET':
        documents = list(db.DepositoBancario.find())
        for doc in documents:
            doc['_id'] = str(doc['_id'])
        return jsonify(documents)
    elif request.method == 'PUT':
        id = request.args.get('id')
        data = request.json
        result = db.DepositoBancario.update_one({"_id": ObjectId(id)}, {"$set": data})
        if result.matched_count:
            return jsonify({"message": "Documento actualizado"})
        else:
            return jsonify({"error": "Documento no encontrado"}), 404
    elif request.method == 'DELETE':
        id = request.args.get('id')
        result = db.DepositoBancario.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return jsonify({"message": "Documento eliminado"})
        else:
            return jsonify({"error": "Documento no encontrado"}), 404

# Transaccion
@app.route('/transaccion', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_transaccion():
    if request.method == 'POST':
        data = request.json
        result = db.Transaccion.insert_one(data)
        return jsonify({"_id": str(result.inserted_id)}), 201
    elif request.method == 'GET':
        documents = list(db.Transaccion.find())
        for doc in documents:
            doc['_id'] = str(doc['_id'])
        return jsonify(documents)
    elif request.method == 'PUT':
        id = request.args.get('id')
        data = request.json
        result = db.Transaccion.update_one({"_id": ObjectId(id)}, {"$set": data})
        if result.matched_count:
            return jsonify({"message": "Documento actualizado"})
        else:
            return jsonify({"error": "Documento no encontrado"}), 404
    elif request.method == 'DELETE':
        id = request.args.get('id')
        result = db.Transaccion.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return jsonify({"message": "Documento eliminado"})
        else:
            return jsonify({"error": "Documento no encontrado"}), 404

# Valoracion
@app.route('/valoracion', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_valoracion():
    if request.method == 'POST':
        data = request.json
        result = db.Valoracion.insert_one(data)
        return jsonify({"_id": str(result.inserted_id)}), 201
    elif request.method == 'GET':
        documents = list(db.Valoracion.find())
        for doc in documents:
            doc['_id'] = str(doc['_id'])
        return jsonify(documents)
    elif request.method == 'PUT':
        id = request.args.get('id')
        data = request.json
        result = db.Valoracion.update_one({"_id": ObjectId(id)}, {"$set": data})
        if result.matched_count:
            return jsonify({"message": "Documento actualizado"})
        else:
            return jsonify({"error": "Documento no encontrado"}), 404
    elif request.method == 'DELETE':
        id = request.args.get('id')
        result = db.Valoracion.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return jsonify({"message": "Documento eliminado"})
        else:
            return jsonify({"error": "Documento no encontrado"}), 404

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
