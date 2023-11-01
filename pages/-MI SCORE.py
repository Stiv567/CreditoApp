import streamlit as st
import pickle
import pandas as pd
import optbinning
from PIL import Image

# Mapeo de valores originales a etiquetas comprensibles
home_ownership_labels = {
    "MORTGAGE": "Hipoteca",
    "OWN": "Propia",
    "RENT": "Alquiler"
}



# Cargar el modelo de scorecard previamente entrenado
scorecard_model = pd.read_pickle("modelo_scorecard4.pkl")

def score():
    st.markdown("# CREDIT SCORE")
    st.sidebar.title("# :orange[C]- :green[$CORE]")
    with st.container():
        st.title("Calcula tu score crediticio")
        st.header("Ingresa tus datos:")

        person_age = st.number_input("Edad", min_value=18, max_value=120)
        person_income = st.number_input("Ingreso Personal anual (valores en USD)", min_value=1)
        # Lista desplegable con etiquetas comprensibles
        person_home_ownership = st.selectbox("Tipo de Propiedad", list(home_ownership_labels.values()))
        person_emp_length = st.number_input("Experiencia Laboral (en años)", min_value=0,max_value=person_age)
        # Lista desplegable con etiquetas comprensibles
        cb_person_cred_hist_length = st.number_input("Historial credicticio (en años)", min_value=0, max_value=person_age)

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
            if person_emp_length > person_age:
                st.error("La experiencia laboral no puede exceder la edad de la persona.")
            elif cb_person_cred_hist_length > person_age:
                st.error("El historial crediticio no puede exceder la edad de la persona.")
            else:
                imagen = Image.open("credit_table2.png")
                arrow_image = Image.open("vector_op.png")
                # Mapeo inverso para obtener valores originales
                person_home_ownership = next(key for key, value in home_ownership_labels.items() if value == person_home_ownership)

                # Crear un DataFrame con los valores ingresados
                input_data = pd.DataFrame({
                'person_age': [person_age],
                'person_income': [person_income],
                'person_home_ownership': [person_home_ownership],
                'person_emp_length': [person_emp_length],
                'cb_person_cred_hist_length': [cb_person_cred_hist_length]
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

