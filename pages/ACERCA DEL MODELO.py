import streamlit as st
from PIL import Image

st.markdown("# Reporte técnico: Modelo de riesgo de crédito")
st.sidebar.markdown("# :orange[C]- :green[$CORE]")

st.header('Definición del problema')
multi = '''La base de datos Credit Risk Dataset (Tse, n.d.) muestra un caso donde se simula la
participación de personas dentro del buró de crédito.
Dicha base de datos contiene la siguiente información recolectada, separada en columnas:
- :blue[Edad (años): person_age]
- :blue[Ingreso anual ($): person_income]
- :blue[Tipo de vivienda (renta, hipoteca, propia u otra): person_home_ownership]
- :blue[Duración de empleo (años): person_emp_length]
- Intención de préstamo (educativa, médica, empresarial, personal o consolidada):
loan_intent
- Grado de préstamo (A, B, C, D o E): loan_grade
- Cantidad de préstamo ($): loan_amnt
- Interés (%): loan_int_rate
- :orange[Estado del préstamo (no incumplido o incumplido): loan_status]
- Porcentaje de ingreso (%): loan_percent_income
- Histórico de incumplimiento (sí o no): cb_person_default_on_file
- :blue[Duración de historial crediticio (años): cb_person_cred_hist_length]

Sin embargo, la base de datos muestra valores no adecuados o incoherentes entre sí, y bajo el contexto en que están siendo analizados. 
Es por ello que se busca realizar un modelo de riesgo crediticio basado en los datos presentados, y con él, poder tomar decisiones dentro del buró de crédito que se está manejando. 
Para ello, es necesario filtrar adecuadamente las variables, los datos y poder realizar un análisis adecuado de estos.

El score crediticio que se quiere generar se hará a partir únicamente de variables de la persona. 
Es decir, la edad, los ingresos, la cantidad de años desde que inicio con su historial crediticio, entre otros.

Como se desea conocer cual es la probabilidad de que la persona que ingresa sus datos incumpla con algún crédito que se le otorgue 
se define como variable objetivo el estado del préstamo la cual aparece en naranja. En azul están todas aquellas variables que se consideran en este problema.'''

st.markdown(multi)

st.header('Hipótesis')

multi_2 = '''
- Edad (años): Se espera que el score se reduzca a medida que aumenta la edad.
- Ingreso anual (USD$): El score aumenta a medida que aumentan los ingresos anuales.
- Tipo de vivienda (renta, hipoteca, propia u otra): Si la vivienda es propia o esta en hipoteca indica una situación de estabilidad financiera, 
por lo que el score tendería a aumentar según estas dos entradas. Por otro lado, si la vivienda es rentada 
o cualquiera sea la situación (otra), el score no se vería tan afectado.
- Duración de empleo (años): Se espera que con mas años en el mundo laboral el score también aumente.
- Experiencia laboral (años):  El score presentara un aumento a medida que la experiencia laboral lo hace.
- Duración de historial crediticio (años): Al igual que la duración del empleo, el score aumentara a medida que esta variable aumenta aunque 
no en la misma magnitud que en el caso de la duración del empleo.
'''

st.markdown(multi_2)

st.header('Metodología')

multi_3 = '''Para el desarrollo del análisis, se utilizan los datos suministrados por Tse (n.d.), de la plataforma de ciencia de datos, Kaggle. 
La base de datos utiliza las variables descritas anteriormente. Para el análisis y manejo de los datos, se utiliza Python como lenguaje de programación que permite desarrollar lo propuesto.
De igual manera, se trabaja en un scorecard, el cual será utilizado para mostrar el modelo propuesto, mediante una página web usando la plataforma StreamLit. 
El puntaje crediticio se calcula con una escala que esta entre 300 y 850.'''

st.markdown(multi_3)
        

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

st.caption('Para ver el reporte técnico completo en Deepnote haz clic en :red[Reporte técnico]')
st.link_button("Reporte técnico","https://deepnote.com/publish/Score-Crediticio-Grupo-7-c3e73745-4797-4eab-9e9e-84b64802ff8e")

st.markdown('<div class="custom-space"></div>', unsafe_allow_html=True)


# Estilos CSS para el footer
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
    """,
    unsafe_allow_html=True
)



