import streamlit as st
import pickle
import pandas as pd

# Cargar el modelo de scorecard previamente entrenado
with open('modelo_scorecard2.pkl', 'rb') as modelo_pkl:
    scorecard_model = pickle.load(modelo_pkl)

def main():
    st.title("Aplicación de Scorecard")

    st.sidebar.header("Parámetros de Entrada")

    person_income = st.sidebar.number_input("Ingreso Personal", min_value=1)
    person_home_ownership = st.sidebar.selectbox("Tipo de Propiedad", ["MORTGAGE", "OWN", "RENT"])
    person_emp_length = st.sidebar.number_input("Experiencia Laboral (en años)", min_value=0.0)
    loan_intent = st.sidebar.selectbox("Propósito del Préstamo", ["DEBTCONSOLIDATION", "EDUCATION", "HOMEIMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE"])
    loan_grade = st.sidebar.selectbox("Grado del Préstamo", ["A", "B", "C", "D", "E", "F", "G"])
    loan_amnt = st.sidebar.number_input("Monto del Préstamo", min_value=1.0)
    loan_int_rate = st.sidebar.number_input("Tasa de Interés del Préstamo", min_value=0.0)

    percent_income = loan_amnt / person_income

    if st.sidebar.button("Calcular Puntaje"):
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

        # Mostrar el puntaje
        st.subheader("Puntaje de Crédito:")
        st.write(score)

if __name__ == '__main__':
    main()
