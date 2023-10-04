
install.packages("shiny")
py_install("joblib")

# Cargar la biblioteca Shiny
py_install("pandas")
library(shiny)

# Carga el modelo de puntuación
library(joblib)

# Carga el modelo de puntuación previamente guardado
scorecard_model <- joblib::load("modelo_scorecard.pkl")

# Verifica que el modelo se haya cargado correctamente en R
str(modelo_scorecard)

# Definir la interfaz de usuario (UI)
ui <- fluidPage(
  titlePanel("Calculadora de Puntaje Crediticio"),
  
  sidebarLayout(
    sidebarPanel(
      # Entrada de usuario: Campos de entrada para las variables
      numericInput("person_income", "Ingreso Personal:", value = 69900),
      numericInput("loan_amnt", "Monto del Préstamo:", value = 5050),
      sliderInput("person_emp_length", "Antigüedad en el Empleo:", min = 0, max = 30, value = 9),
      selectInput("loan_intent", "Motivo del Préstamo:",
                  choices = c("DEBTCONSOLIDATION", "EDUCATION", "MEDICAL", "PERSONAL")),
      selectInput("loan_grade", "Grado del Préstamo:",
                  choices = c("A", "B", "C", "D")),
      radioButtons("cb_person_default_on_file", "Antecedentes de Incumplimiento en el Historial:",
                   choices = c("N" = "No", "Y" = "Sí")),
      
      # Botón para calcular el puntaje
      actionButton("calcular_puntaje", "Calcular Puntaje")
    ),
    
    mainPanel(
      # Resultado del puntaje
      verbatimTextOutput("resultado")
    )
  )
)

# Definir el servidor
server <- function(input, output) {
  # Función para calcular el puntaje crediticio
  calcular_puntaje <- function(person_income, loan_amnt, person_emp_length, loan_intent, loan_grade, cb_person_default_on_file) {
    # Crear un DataFrame con los valores de entrada
    data <- data.frame(
      person_income = person_income,
      loan_amnt = loan_amnt,
      person_emp_length = person_emp_length,
      loan_intent = loan_intent,
      loan_grade = loan_grade,
      cb_person_default_on_file = cb_person_default_on_file
    )
    
    # Llamar al modelo Python para calcular el puntaje
    puntaje <- py_run_string("modelo_scorecard.score(data)")
    
    return(puntaje)
  }
  
  # Observador para calcular el puntaje cuando se presiona el botón
  observeEvent(input$calcular_puntaje, {
    puntaje <- calcular_puntaje(
      input$person_income, 
      input$loan_amnt, 
      input$person_emp_length, 
      input$loan_intent, 
      input$loan_grade, 
      input$cb_person_default_on_file
    )
    
    output$resultado <- renderPrint({
      paste("Puntaje Crediticio:", puntaje)
    })
  })
}

# Ejecutar la aplicación Shiny
shinyApp(ui, server)