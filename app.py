from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Handle GET requests (display the form)
    return render_template('calculator2.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Handle POST requests (process the calculation)
    try:
        data = request.get_json()
        expression = data['expression']
    except (KeyError, TypeError) as e:
        return jsonify({'error': f'Invalid request body: {str(e)}'}), 400

    try:
        if "+" in expression:
            result = eval(expression)


        
        # Use a safer evaluation method, like a custom parser or a library like SymPy
        # This example uses eval() for simplicity (replace with a safer approach)
        
    except Exception as e:
        return jsonify({'error': f'Error evaluating expression: {str(e)}'}), 500

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)