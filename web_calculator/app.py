from flask import Flask, render_template, request, jsonify
import calculator_logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data.get('operation')
    try:
        if operation in ['add', 'subtract', 'multiply', 'divide', 'power']:
            num1 = float(data.get('num1'))
            num2 = float(data.get('num2'))
            func = getattr(calculator_logic, operation)
            result = func(num1, num2)
        elif operation in ['sin', 'cos', 'tan', 'log', 'ln', 'sqrt', 'factorial', 'exp']:
            num = float(data.get('num'))
            func = getattr(calculator_logic, operation)
            result = func(num)
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
