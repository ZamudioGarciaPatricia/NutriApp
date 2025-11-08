from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/formulario')
def forms():
    return render_template('forms.html')


if __name__ == '__main__':
    app.run(debug=True) 