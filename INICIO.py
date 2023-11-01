import streamlit as st

def main():
    st.markdown(
        """
        <style>
        .big-text {
            font-size: 36px;
            color: orange;
            background-color: green;
            padding: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Apply the CSS class to text and specify the text content
    st.sidebar.markdown("<p class='big-text'>C - $CORE</p>", unsafe_allow_html=True)

    
    #st.sidebar.title(":orange[C]- :green[$CORE]")
    with st.container():
        st.title("¿Que es el puntaje crediticio?")
        multi = '''Un puntaje crediticio es como una "nota" que refleja tu responsabilidad financiera. Imagina que es tu "boleta de confianza" en el mundo financiero.Las instituciones financieras la utilizan para saber si puedes pagar tus préstamos a tiempo.''',
        '''Este puntaje se representa en una especie de "tarjeta de puntaje" que te dice cuán confiable eres.Cuanto más alto sea tu puntaje, más confianza tendrán en ti.''',
        '''En resumen, tu puntaje crediticio es como tu reputación financiera, ¡y mantenerla en buen estado es clave para obtener préstamos y tarjetas de crédito en el futuro!
        '''
        st.markdown(multi)
        video_file = open('FDA T1_ C-Score - Grupo 7.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

        st.header('_VISITA LA SECCION :green[MI SCORE] PARA CALCULAR_', divider='rainbow')
        
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
        # Contenido del footer
        footer_content = """
        <div class="footer">
        Amilder Stewin Ospina Tobón<br>
        Nicolás Pérez Vásquez<br>
        John Stiven Mejía Lopera<br>
        Juan Paulo Cepeda Zúñiga<br>|
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
    main()
