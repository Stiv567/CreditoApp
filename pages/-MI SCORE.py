import streamlit as st
import pickle
import pandas as pd
import optbinning
from PIL import Image

scorecard_model = pd.read_pickle("modelo_scorecard2.pkl")

# Cargar el modelo de scorecard previamente entrenado
#with open('modelo_scorecard2.pkl', 'rb') as modelo_pkl:
#    scorecard_model = pickle.load(modelo_pkl)

def score():
    st.markdown("# CREDIT SCORE")
    st.sidebar.markdown("# Inicio")
    with st.container():
        st.title("Calcula tu credit Score")
        st.header("Ingresa los datos:")

        person_income = st.number_input("Ingreso Personal", min_value=1)
        person_home_ownership = st.selectbox("Tipo de Propiedad", ["MORTGAGE", "OWN", "RENT"])
        person_emp_length = st.number_input("Experiencia Laboral (en años)", min_value=0.0)
        loan_intent = st.selectbox("Propósito del Préstamo", ["DEBTCONSOLIDATION", "EDUCATION", "HOMEIMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE"])
        loan_grade = st.selectbox("Grado del Préstamo", ["A", "B", "C", "D", "E", "F", "G"])
        loan_amnt = st.number_input("Monto del Préstamo", min_value=1.0)
        loan_int_rate = st.number_input("Tasa de Interés del Préstamo", min_value=0.0)

        percent_income = loan_amnt / person_income

        max_score = 850
        def determinar_categoria(puntaje):
            if 300 <= puntaje < 630:
                return "Malo"
            elif 630 <= puntaje < 690:
                return "Aceptable"
            elif 690 <= puntaje < 720:
                return "Bueno"
            elif 720 <= puntaje <= 850:
                return "Excelente"
            else:
                return "Puntaje no válido"
        def mostrar_mensaje_consejo(puntaje):
            categoria = determinar_categoria(puntaje)
            puntaje_entero = int(puntaje)
            
            if categoria == "Malo":
                mensaje = "Lastimosamente, tu puntaje es {} y te encuentras en la categoría Malo.".format(puntaje_entero)
                consejo = "Para mejorar tu puntaje crediticio, es importante pagar tus deudas a tiempo y reducir tus saldos pendientes."

            elif categoria == "Aceptable":
                mensaje = "Tu puntaje es {} y te encuentras en la categoría Aceptable.".format(puntaje_entero)
                consejo = "Mantén tus pagos al día y evita solicitar crédito en exceso para mejorar tu puntaje."

            elif categoria == "Bueno":
                mensaje = "Felicidades, tu puntaje es {} y te encuentras en la categoría Bueno.".format(puntaje_entero)
                consejo = "Sigue manteniendo tus cuentas en orden y evita endeudarte en exceso."

            elif categoria == "Excelente":
                mensaje = "¡Enhorabuena! Tu puntaje es {} y te encuentras en la categoría Excelente.".format(puntaje_entero)
                consejo = "Sigue manteniendo tus finanzas en excelente estado y aprovecha las ofertas crediticias con tasas preferenciales."

            else:
                mensaje = "El puntaje no es válido. Ingresa un puntaje entre 300 y 850."
                consejo = ""
            
            st.write(mensaje)
            st.write("Consejos:")
            st.write(consejo)
        
        if st.button("Calcular Puntaje"):
            imagen = Image.open("credit_table2.png")
            arrow_image = Image.open("vector_op.png")
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

            new_size = (1000, 1200)  # Tamaño deseado
            resized_arrow = arrow_image.resize(new_size)
            
            min_score = 300
            max_angle = 180
            angle = max_angle * (score - min_score) / (max_score - min_score)
            rotated_arrow = resized_arrow.rotate(-angle)

            imagen.paste(rotated_arrow, (2370,1300), rotated_arrow)
            st.image(imagen, caption='ScoreImage', width=600)

            st.markdown(f"<h1 style='text-align: center; color: white;'>Tu Puntaje Crediticio Es: {int(score)}</h1>", unsafe_allow_html=True)

            with st.expander("¿Que quiere decir mi puntaje?"):
                 mostrar_mensaje_consejo(score)
        
        st.markdown(
            """
            <style>
            .footer {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #333;
            color: white;
            padding: 10px;
            text-align: center;
            }
            .footer a {
                color: white;
                text-decoration: none;
                margin: 0 10px;
            }
            </style>
            """,unsafe_allow_html=True)
        
        st.markdown(
            """
            <style>
            .custom-space {
            margin-top: 3cm;
            }
            </style>
            """,
            unsafe_allow_html=True
            )
        st.markdown('<div class="custom-space"></div>', unsafe_allow_html=True)
        
        footer_content = """
        <div class="footer">
        Aviso de Privacidad: Sus datos personales están protegidos. Nos tomamos en serio su privacidad y cumplimos con todas las normativas de protección de datos.
        Puede obtener más información en nuestra política de privacidad.<br>| 
        <a href="https://github.com/Stiv567/CreditoApp" target="_blank">
        Repositorio GitHub
        </a> | 
        <a href="https://www.kaggle.com/datasets/laotse/credit-risk-dataset" target="_blank">
        Dataset
        </a> |
        </div>
        """

        # Mostrar el contenido del footer
        st.markdown(footer_content, unsafe_allow_html=True)

            

if __name__ == '__main__':
    score()