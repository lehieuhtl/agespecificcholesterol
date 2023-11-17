library(shiny)
#ui
ui = fluidPage(
  titlePanel("Imitation Login System"),
  sidebarLayout(
    sidebarPanel(
      textInput("username", "Username: "),
      passwordInput("password", "Password: "),
      actionButton("login", "Log In")
    ),
    mainPanel(
      textOutput("loginStatus")
    )
  )
)
#Define the server
server = function(input, output, session) {
  observeEvent(input$login, {
    #Simulation of a login system
    if (input$username == "demo" && input$password == "password") {
      output$loginStatus = renderText("Login Successful")
    } else {
      output$loginStatus = renderText("You put the wrong password, try again >:(")
    }
  })
}

shinyApp(ui, server)
