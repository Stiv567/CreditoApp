import streamlit as st
import pickle
import pandas as pd
import optbinning


# Mapeo de valores originales a etiquetas comprensibles
home_ownership_labels = {
    "MORTGAGE": "Hipoteca",
    "OWN": "Propia",
    "RENT": "Alquiler"
}

intent_labels = {
    "DEBTCONSOLIDATION": "Consolidación de Deuda",
    "EDUCATION": "Educación",
    "HOMEIMPROVEMENT": "Mejoras en el Hogar",
    "MEDICAL": "Gastos Médicos",
    "PERSONAL": "Personal",
    "VENTURE": "Emprendimiento"
}

cb_person_default_on_file_labels = {
    "N": "No",
    "Y": "Si"
}


# Cargar el modelo de scorecard previamente entrenado
with open('modelo_scorecard3.pkl', 'rb') as modelo_pkl:
    scorecard_model = pickle.load(modelo_pkl)

def main():
    st.title("Aplicación de Scorecard")

    st.sidebar.header("Parámetros de Entrada")

    person_age = st.sidebar.number_input("Edad", min_value=18, max_value=120)

    person_income = st.sidebar.number_input("Ingreso Personal anual (valores en USD)", min_value=0.0)
    
    # Lista desplegable con etiquetas comprensibles
    person_home_ownership = st.sidebar.selectbox("Tipo de Propiedad", list(home_ownership_labels.values()))
    
    person_emp_length = st.sidebar.number_input("Experiencia Laboral (en años)", min_value=0.0,max_value=100)
    
    # Lista desplegable con etiquetas comprensibles
    loan_intent = st.sidebar.selectbox("Propósito del Préstamo", list(intent_labels.values()))

    cb_person_default_on_file = st.sidebar.selectbox("¿Has incumplido alguna vez con un credito?", list(cb_person_default_on_file_labels.values()))
    
    cb_person_cred_hist_length = st.sidebar.number_input("Historial credicticio (en años)", min_value=0.0, max_value=100)
    

    if st.sidebar.button("Calcular Puntaje"):
        # Mapeo inverso para obtener valores originales
        person_home_ownership = next(key for key, value in home_ownership_labels.items() if value == person_home_ownership)
        loan_intent = next(key for key, value in intent_labels.items() if value == loan_intent)
        cb_person_default_on_file = next(key for key, value in cb_person_default_on_file_labels.items() if value == cb_person_default_on_file)

        # Crear un DataFrame con los valores ingresados
        input_data = pd.DataFrame({
            'person_age': [person_age],
            'person_income': [person_income],
            'person_home_ownership': [person_home_ownership],
            'person_emp_length': [person_emp_length],
            'loan_intent': [loan_intent],
            'cb_person_default_on_file': [cb_person_default_on_file],
            'cb_person_cred_hist_length': [cb_person_cred_hist_length]
        })

        # Calcular el puntaje utilizando el modelo de scorecard
        score = scorecard_model.score(input_data)

        # Mostrar el puntaje
        st.subheader("Puntaje de Crédito:")
        st.write(float(score))

if __name__ == '__main__':
    main()
