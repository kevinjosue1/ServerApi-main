from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/api', methods=['POST'])
def api_endpoint():
    try:
        data = request.get_json()
        name = data.get('name', 'World')
        return jsonify({'message': f'Hello, {name}!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
