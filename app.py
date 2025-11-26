from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import requests

USUARIOS = {} 


app = Flask(__name__)
app.secret_key = 'kiwi-secreto'
CLAVE_API = "2mVbF6kxK7xneQO7arHpkEhocL3fieky45ymC89t" 
URL_BASE_BUSQUEDA = "https://api.nal.usda.gov/fdc/v1/foods/search"
URL_BASE_DETALLE = "https://api.nal.usda.gov/fdc/v1/food/"

#Rutas

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/Recetas')
def form():
    return render_template('recetas.html')

#Analizador de receta
def obtener_fdc_id_y_calorias_base(nombre_ingrediente):
    parametros_busqueda = {
        "api_key": CLAVE_API,
        "query": nombre_ingrediente,
        "pageSize": 1
    }
    
    try:
        respuesta_busqueda = requests.get(URL_BASE_BUSQUEDA, params=parametros_busqueda)
        
        if respuesta_busqueda.status_code != 200:
            print(f"Error de estado HTTP en búsqueda: {respuesta_busqueda.status_code}")
            return None

        resultados = respuesta_busqueda.json()
        
        if not resultados.get('foods'):
            return None 
        
        id_fdc = resultados['foods'][0]['fdcId']
        
        url_detalle = f"{URL_BASE_DETALLE}{id_fdc}"
        parametros_detalle = {"api_key": CLAVE_API} 

        respuesta_detalle = requests.get(url_detalle, params=parametros_detalle)
        
        if respuesta_detalle.status_code != 200:
            print(f"Error de estado HTTP en detalle: {respuesta_detalle.status_code}")
            return None

        datos_detalle = respuesta_detalle.json()
        
        for nutriente in datos_detalle.get('foodNutrients', []):
            if nutriente.get('nutrient', {}).get('name') == "Energy":
                return {
                    "descripcion": datos_detalle.get('description'),
                    "calorias_por_100g": nutriente.get('amount', 0)
                } 

        return None 

    except respuesta_detalle.status_code ==400:
        flash("Intenta con otro nombre")

@app.route('/', methods=['GET'])
def indice():
    return render_template('calculadora.html', total_calorias=None, detalle_ingredientes=None)

@app.route('/calculate', methods=['POST'])
def calcular():
    calorias_totales = 0
    detalle_ingredientes = []
    ingredientes_formulario = []
    

    for i in range(1, 11):
        nombre_key = f'nombre_{i}'
        gramos_key = f'gramos_{i}'
        
        nombre = request.form.get(nombre_key, '').strip()
        gramos_str = request.form.get(gramos_key, '0').strip()
        
        try:
            gramos = float(gramos_str)
        except ValueError:
            gramos = 0
        
        if nombre and gramos > 0:
            ingredientes_formulario.append({
                "nombre": nombre,
                "gramos": gramos,
                "nombre_campo": nombre_key, 
                "gramos_campo": gramos_key
            })
            
            datos_base = obtener_fdc_id_y_calorias_base(nombre)
            
            if datos_base and datos_base["calorias_por_100g"] > 0:
                factor = gramos / 100
                contribucion_calorias = datos_base["calorias_por_100g"] * factor
                calorias_totales += contribucion_calorias

                detalle_ingredientes.append({
                    "nombre": nombre,
                    "gramos": gramos,
                    "calorias": round(contribucion_calorias, 2),
                    "encontrado": True
                })
            else:
                detalle_ingredientes.append({
                    "nombre": f"{nombre} (No encontrado o 0 Kcal)",
                    "gramos": gramos,
                    "calorias": 0,
                    "encontrado": False
                })

    if not ingredientes_formulario:
        return render_template('calculadora.html', total_calorias=None, detalle_ingredientes=None, submitted_data={})
    return render_template('calculadora.html',
                            total_calorias=round(calorias_totales, 2),
                            detalle_ingredientes=detalle_ingredientes,
                            submitted_data={k: request.form.get(k) for k in request.form}
                            )


#Registro

base_usuarios = {} 
@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if request.method == 'POST':
        nombre          = request.form.get('nombre', '').strip()
        apellidos       = request.form.get('apellidos', '').strip()
        correo          = request.form.get('email', '').strip().lower()
        contrasena      = request.form.get('password', '').strip()
        edad            = request.form.get('edad', '').strip()
        sexo            = request.form.get('sexo', '').strip()
        peso            = request.form.get('peso', '').strip()
        altura          = request.form.get('altura', '').strip()
        nivel_actividad = request.form.get('nivel_actividad', '').strip()

        campos_obligatorios = {
            'nombre': nombre,
            'apellidos': apellidos,
            'correo': correo,
            'contraseña': contrasena,
            'edad': edad,
            'sexo': sexo,
            'peso': peso,
            'altura': altura,
            'nivel_actividad': nivel_actividad
        }
        for campo, valor in campos_obligatorios.items():
            if not valor:
                flash(f'{campo.capitalize()} es obligatorio', 'danger')
                return redirect(url_for('perfil'))

        base_usuarios[correo] = {
            'nombre': nombre,
            'apellidos': apellidos,
            'contraseña': contrasena,
            'edad': int(edad),
            'sexo': sexo,
            'peso': float(peso),
            'altura': float(altura),
            'nivel_actividad': nivel_actividad,
            'tipo_dieta': request.form.get('tipo_dieta') or None,
            'alergias': [a.strip() for a in request.form.get('alergias', '').split(',')] if request.form.get('alergias') else [],
            'intolerancias': [i.strip() for i in request.form.get('intolerancias', '').split(',')] if request.form.get('intolerancias') else [],
            'objetivos': request.form.getlist('objetivos'),
            'otro_objetivo': request.form.get('otro_objetivo') or None
        }
        flash('Perfil creado con éxito.')
        return redirect(url_for('iniciar_sesion'))

    return render_template('perfil.html')


#Calculadoras

def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal (altura en metros)."""
    return peso / (altura ** 2)

def calcular_tmb(sexo, peso, altura_cm, edad):
    """Calcula la Tasa Metabólica Basal (Fórmula Mifflin-St Jeor)."""
    if sexo == "masculino": 
        return 10 * peso + 6.25 * altura_cm - 5 * edad + 5
    else:
        return 10 * peso + 6.25 * altura_cm - 5 * edad - 161

def calcular_gct(tmb, actividad):

    factores = {
        "sedentario": 1.2,
        "ligero": 1.375,
        "moderado": 1.55,
        "activo": 1.725,  
        "muy_activo": 1.9 
    }
    return tmb * factores.get(actividad, 1.2)



def calcular_macros(calorias):
    prote = calorias * 0.30 / 4
    carbos = calorias * 0.40 / 4     
    grasas = calorias * 0.30 / 9     
    return prote, carbos, grasas


@app.route("/calculadora", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        
        try:
            peso = float(request.form["peso"])
            altura_m = float(request.form["altura"]) 
            altura_cm = altura_m * 100 
            edad = int(request.form["edad"])
            sexo = request.form["sexo"]
            actividad = request.form["actividad"]
        except ValueError:
            return render_template("calculadora.html", error="Por favor, introduce valores numéricos válidos.")


        imc = calcular_imc(peso, altura_m)
        tmb = calcular_tmb(sexo, peso, altura_cm, edad)
        gct = calcular_gct(tmb, actividad)
        prote, carbos, grasas = calcular_macros(gct)

        return render_template(
            "resultado.html",
            imc=round(imc, 2),
            tmb=round(tmb, 2),
            gct=round(gct, 2),
            prote=round(prote, 3),
            carbos=round(carbos, 2),
            grasas=round(grasas, 2)
        )

    return render_template("calculadora.html")

#Analizador de recetas


if __name__ == '__main__':
    app.run(debug=True)