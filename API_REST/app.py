from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sumar', methods=['POST'])
def sumar():
    numero1 = int(request.form['numero1'])
    numero2 = int(request.form['numero2'])
    resultado = numero1 + numero2
    return f"La suma de {numero1} y {numero2} es: {resultado}"

if __name__ == '__main__':
    app.run()
