from flask import Flask, render_template, request, url_for
import pickle
import pandas as pd
import optbinning

app = Flask(__name__)

# Cargar el modelo de scorecard previamente entrenado
with open('modelo_scorecard2.pkl', 'rb') as modelo_pkl:
    scorecard_model = pickle.load(modelo_pkl)

@app.route('/', methods=['GET', 'POST'])
def calcular_puntaje():
    if request.method == 'POST':
        # Obtener los valores ingresados por el usuario desde el formulario web
        person_income = float(request.form['person_income'])
        person_home_ownership = request.form['person_home_ownership']
        person_emp_length = float(request.form['person_emp_length'])
        loan_intent = request.form['loan_intent']
        loan_grade = request.form['loan_grade']
        loan_amnt = float(request.form['loan_amnt'])
        loan_int_rate = float(request.form['loan_int_rate'])
        
        # Calcular el porcentaje de ingresos para el préstamo
        percent_income = loan_amnt / person_income
        
        # Crear un DataFrame con los valores ingresados
        input_data = pd.DataFrame({
            'person_income': [person_income],
            'person_home_ownership': [person_home_ownership],
            'person_emp_length': [person_emp_length],
            'loan_intent': [loan_intent],
            'loan_grade': [loan_grade],
            'loan_amnt': [loan_amnt],
            'loan_int_rate': [loan_int_rate],
            'loan_percent_income': [percent_income],
            'cb_person_default_on_file': ['N']  # Puedes cambiar esto según el valor real
        })
        
        # Calcular el puntaje utilizando el modelo de scorecard
        score = scorecard_model.score(input_data)
        
        return render_template('resultado.html', score=score)
    
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
