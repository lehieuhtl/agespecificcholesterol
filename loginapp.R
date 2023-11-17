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

