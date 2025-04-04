import MySQLdb
from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_db_connection
import json
from flask import Response

app = Flask(__name__)
CORS(app)

@app.route('/buscar', methods=['GET'])
def buscar_operadoras():
    try:
        nome_fantasia = request.args.get('modalidade', '')
        
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Erro ao conectar ao banco de dados"}), 500

        cursor = conn.cursor()

        if nome_fantasia:
            query = """
                SELECT Registro_ANS, CNPJ, Razao_Social, Modalidade, Cidade, UF, Representante
                FROM operadoras
                WHERE Modalidade LIKE %s;
            """
            cursor.execute(query, (nome_fantasia + "%",))
        else:
            query = """
                SELECT Registro_ANS, CNPJ, Razao_Social, Modalidade, Cidade, UF, Representante
                FROM operadoras;
            """
            cursor.execute(query)

        resultados = cursor.fetchall()
        cursor.close()
        conn.close()

        print(f"Total de operadoras retornadas: {len(resultados)}")

        json_data = json.dumps(resultados, ensure_ascii=False, indent=2)
        return Response(json_data, mimetype='application/json')

    except MySQLdb.Error as db_err:
        print(f"Erro no banco de dados: {db_err}")
        return jsonify({"error": "Erro no banco de dados"}), 500

    except Exception as e:
        import traceback
        print("Stack trace do erro:")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

app.run(debug=True, port=5001)
