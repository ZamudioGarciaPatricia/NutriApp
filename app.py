from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/form')
def animales():
    return render_template('form.html')

@app.route('/Aprendemas')
def Aprende_mas():
    return render_template('miinfo.html')



#calculadora 

def calcular_imc(peso, altura):
    # altura en metros
    return peso / (altura ** 2)

def calcular_tmb(sexo, peso, altura_cm, edad):
    # Fórmula Mifflin-St Jeor
    if sexo == "hombre":
        return 10 * peso + 6.25 * altura_cm - 5 * edad + 5
    else:
        return 10 * peso + 6.25 * altura_cm - 5 * edad - 161

def calcular_gct(tmb, actividad):
    factores = {
        "sedentario": 1.2,
        "ligero": 1.375,
        "moderado": 1.55,
        "alto": 1.725,
        "muy_alto": 1.9
    }
    return tmb * factores.get(actividad, 1.2)

def calcular_peso_ideal(altura_cm, sexo):
    # Fórmula de Devine
    if sexo == "hombre":
        return 50 + 0.9 * ((altura_cm - 152) / 2.54)
    else:
        return 45.5 + 0.9 * ((altura_cm - 152) / 2.54)

def calcular_macros(calorias):
    prote = calorias * 0.30 / 4      
    carbos = calorias * 0.40 / 4     
    grasas = calorias * 0.30 / 9     
    return prote, carbos, grasas


@app.route("/calculadora", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        peso = float(request.form["peso"])
        altura = float(request.form["altura"]) 
        altura_cm = altura * 100
        edad = int(request.form["edad"])
        sexo = request.form["sexo"]
        actividad = request.form["actividad"]

        imc = calcular_imc(peso, altura)
        tmb = calcular_tmb(sexo, peso, altura_cm, edad)
        gct = calcular_gct(tmb, actividad)
        peso_ideal = calcular_peso_ideal(altura_cm, sexo)
        prote, carbos, grasas = calcular_macros(gct)

        return render_template(
            "resultado.html",
            imc=round(imc, 2),
            tmb=round(tmb, 2),
            gct=round(gct, 2),
            peso_ideal=round(peso_ideal, 2),
            prote=round(prote, 3),
            carbos=round(carbos, 2),
            grasas=round(grasas, 2)
        )

    return render_template("calculadora.html")

if __name__ == '__main__':
    app.run(debug=True) 