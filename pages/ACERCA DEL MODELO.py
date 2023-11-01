import streamlit as st
from PIL import Image

st.markdown("# Reporte técnico: Modelo de riesgo de crédito")
st.sidebar.markdown("# :orange[C]- :green[$CORE]")

st.header('Definición del problema')
multi = '''La base de datos Credit Risk Dataset (Tse, n.d.) muestra un caso donde se simula la
participación de personas dentro del buró de crédito.
Dicha base de datos contiene la siguiente información recolectada, separada en columnas:
- Edad (años): person_age
- Ingreso anual ($): person_income
- Tipo de vivienda (renta, hipoteca, propia u otra): person_home_ownership
- Duración de empleo (años): person_emp_length
- Intención de préstamo (educativa, médica, empresarial, personal o consolidada):
loan_intent
- Grado de préstamo (A, B, C, D o E): loan_grade
- Cantidad de préstamo ($): loan_amnt
- Interés (%): loan_int_rate
- Estado del préstamo (no incumplido o incumplido): loan_status
- Porcentaje de ingreso (%): loan_percent_income
- Histórico de incumplimiento (sí o no): cb_person_default_on_file
- Duración de historial crediticio (años): cb_person_cred_hist_length

Sin embargo, la base de datos muestra valores no adecuados o incoherentes entre sí, y bajo el
contexto en que están siendo analizados. Es por ello que se busca realizar un modelo de
riesgo crediticio basado en los datos presentados, y con él, poder tomar decisiones dentro del
buró de crédito que se está manejando.
Para ello, es necesario filtrar adecuadamente las variables, los datos y poder realizar un
análisis adecuado de estos. Se presentará entonces una página web que muestre el
comportamiento del modelo propuesto.'''
st.markdown(multi)

st.header('Metodología')

multi_2 = '''Para el desarrollo del análisis, se utilizan los datos suministrados por Tse (n.d.), de la
plataforma de ciencia de datos, Kaggle. La base de datos utiliza las variables descritas
anteriormente.
Para el análisis y manejo de los datos, se utiliza Python como lenguaje de programación que
permite desarrollar lo propuesto.
De igual manera, se trabaja en un scorecard, el cual será utilizado para mostrar el modelo
propuesto, mediante una página web.'''

st.markdown(multi_2)

st.header('Análisis descriptivo e hipótesis')

multi_3 = '''En primer lugar, se debe realizar una limpieza de datos atípicos, o lo que se le llamará un
pre-procesamiento de los datos, el cual seguirá los siguientes pasos:

1. Se eliminan los valores faltantes de la variable person_emp_length, correspondiente a
la duración de empleo de la persona, es decir, aquellos registros cuyo valor sea nulo.
Esto, a primera vista, no es viable, puesto que, al realizarlo, siguen existiendo 3048
datos nulos para esta columna. Por lo tanto, se debe revisar la significancia de la
variable en el modelo propuesto.
'''

st.markdown(multi_3)

image_1 = Image.open('imag1.PNG')
st.image(image_1, caption='Figura 1')

multi_4 = '''La existencia de estos datos nulos indica que no es viable eliminar los registros, ya
que representan casi el 10% de los datos. Por ende, se debe remuestrear o imputar
estos valores.

En principio, se observa la viabilidad de realizar esta imputación de los datos por
medio de un modelo KNN, pero esto no llegaría a ser muy viable en el modelo debido
a la precisión que podría tener en el contexto.

2. Se revisa ahora la variable loan_int_rate, correspondiente al interés asociado,
buscando eliminar también valores nulos.

'''
st.markdown(multi_4)
image_2 = Image.open('imag2.PNG')
st.image(image_2, caption='Figura 2')

st.markdown("De acuerdo con ello, se construye un histograma de los datos:")

image_3 = Image.open('imag3.PNG')
st.image(image_3, caption='Figura 3')

multi_5 = '''Y, antes de proseguir, se realiza una eliminación de datos atípicos según el contexto,
como es la edad de las personas cuando es mayor a 100 años, y los datos donde las
personas tengan una edad mayor al tiempo que han sido empleadas.'''

st.markdown(multi_5)

image_4 = Image.open('imag4.PNG')
st.image(image_4, caption='Figura 4')

multi_6 = '''Se presenta un gráfico de correlaciones, el cual se presenta con valores entre -1 y 1,
donde 0 indicará correlación nula, 1 indica una correlación directa positiva y -1 indica
una correlación directa negativa.'''

st.markdown(multi_6)
image_5 = Image.open('imag5.PNG')
st.image(image_5, caption='Figura 5')

multi_7 = '''Se observa que las variables con mayor correlación parecen ser la edad de la persona
y la duración de historial crediticio. Las otras variables parecieran no estar altamente
relacionadas, así exista un grado de correlación.'''

st.markdown(multi_7)

# Ruta al archivo PDF que se va a descargar
archivo_pdf = "FDA_T1_ReporteTécnico_CreditRisk.pdf"
def descargar_pdf():
    with open(archivo_pdf, "rb") as file:
        pdf_data = file.read()
        st.download_button("Descargar PDF", data=pdf_data, file_name="practicainforme.pdf", mime="application/pdf")

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

st.caption('Si deseas ver el informe completo puedes descargarlo en: :red[Descargar PDF]')
descargar_pdf()

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



