# import dash
# from dash import html, dcc, callback, Output, Input, State
# from dash.exceptions import PreventUpdate
# import pandas as pd 
# from dash import html

# #Load the cholesterol data
# agedata = pd.read_csv("agedata.csv")

# # Dash app with suppress_callback_exceptions=True
# app = dash.Dash(__name__, suppress_callback_exceptions=True)

# # # Load the content of the R Markdown file
# # with open('dashboard.Rmd', 'r') as file:
# #     rmarkdown_content = file.read()


# #Layout for login
# # login_layout = html.Div([
# #   html.H2("Login System"),
# #   html.Label("Username:"),
# #   dcc.Input(id='username-input', type='text', value=''),
# #   html.Label("Password:"),
# #   dcc.Input(id='password-input', type='password', value=''),
# #   html.Button('Log In', id='login-button'),
# #   html.Div(id='login-status', children='')
# # ])

# #New layout for login to allow enter/return 
# login_layout = html.Form([
#     html.H2("Login System"),
#     html.H2("Username:"),
#     dcc.Input(id='username-input', type='text', value=''),
#     html.Label("Password:"),
#     dcc.Input(id='password-input', type='password', value=''),
#     html.Button('Log In', id='login-button', type='submit'),
# ], action='javascript:void(0);')
    

# #Layout for the main page
# main_layout = html.Div([
#     html.H2("Main Page"),
#     html.Button('View Dashboard', id='dashboard-button'),
#     html.Button('View R Markdown', id='rmarkdown-button'),
# ])

# # Layout for cholesterol dashboard
# dashboard_layout = html.Div([
#     html.H2("Cholesterol Dashboard"),
#     dcc.Dropdown(id='age-group-dropdown',
#                  options=[{'label': age_group, 'value': age_group} for age_group in agedata['Age group'].unique()],
#                  value=agedata['Age group'].unique()[0]),
#     dcc.Graph(id='cholesterol-plot')
# ])

# # Layout for R Markdown content
# rmarkdown_layout = html.Div([
#     dcc.Markdown(id='rmarkdown-content', children=rmarkdown_content)
# ])


# # App layout
# app.layout = html.Div([
#     dcc.Location(id='url', refresh=False),
#     html.Div(id='page-content')
# ])

# # Callback to switch between pages based on URL pathname
# @app.callback(
#     Output('page-content', 'children'),
#     [Input('url', 'pathname')]
# )
# def display_page(pathname):
#     if pathname == '/dashboard':
#         return dashboard_layout
#     elif pathname == '/login':
#         return login_layout
#     elif pathname == '/rmarkdown':
#         return rmarkdown_layout
#     else:
#         # Redirect to default page (e.g., login)
#         return login_layout

# # Callback to handle login button click
# @app.callback(
#     [Output('login-status', 'children'),
#      Output('url', 'pathname')],
#     [Input('login-button', 'n_clicks')],
#     [State('username-input', 'value'),
#      State('password-input', 'value')]
# )
# def handle_login(n_clicks, username, password):
#     if n_clicks:
#         # Simulate authentication 
#         if username == 'demo' and password == 'password':
#             return 'Login successful! Redirecting to dashboard...', '/dashboard'
#         else:
#             return 'Invalid username or password. Please try again.', '/'
#     else:
#         # Initial state
#         raise PreventUpdate

# if __name__ == '__main__':
#     app.run_server(debug=True)

#REWRITE
import dash
from dash import html, dcc, callback, Output, Input, State
from dash.exceptions import PreventUpdate
import pandas as pd

#Cholesterol data
agedata = pd.read_csv("agedata.csv")

app = dash.Dash(__name__, suppress_callback_exceptions=True)

#Load content of R Markdown file
with open ('dashboard.Rmd', 'r') as file:
    rmarkdown_content = file.read()

#Layout login
login_layout = html.Form([
    html.H2("Login System"),
    html.H2("Username:"),
    dcc.Input(id='username-input', type='text', value=''),
    html.Label("Password:"),
    dcc.Input(id='password-input', type='password', value=''),
    html.Button('Log In', id='login-button', type='submit'),
], action='javascript:void(0);')

#Layout main page
main_layout = html.Div([
    html.H2("Main Page"),
    html.Button('View Cholesterol Dashboard', id='dashboard-button'),
    html.Button('View R Markdown', id='rmarkdown-button'),
])

#Layout cholesterol dashboard
dashboard_layout = html.Div([
    html.H2("Cholesterol Dashboard"),
    dcc.Dropdown(id='age-group-dropdown',
                    options=[{'label': age_group, 'value': age_group} for age_group in agedata['Age group'].unique()],
                    value=agedata['Age group'].unique()[0]),
    dcc.Graph(id='cholesterol-plot')
])

#Layout R Markdown content
rmarkdown_layout = html.Div([
    dcc.Markdown(id='rmarkdown-content', children=rmarkdown_content)
])

# App layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=login_layout),
    html.Div([
        main_layout,
        dashboard_layout,
        rmarkdown_layout
    ], style={'display': 'none'})
])

# Callback to switch between pages based on URL pathname
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/dashboard':
        return dashboard_layout
    elif pathname == '/login':
        return login_layout
    elif pathname == '/rmarkdown':
        return rmarkdown_layout
    elif pathname == '/main':
        return main_layout
    else:
        # Redirect to default page (e.g., login)
        return login_layout

# Callback to handle login, dashboard and rmarkdown button clicks
@app.callback(
    Output('url', 'pathname'),
    [Input('login-button', 'n_clicks'), Input('dashboard-button', 'n_clicks'), Input('rmarkdown-button', 'n_clicks')],
    [State('username-input', 'value'), State('password-input', 'value')],
    prevent_initial_call=True
)
def update_url_pathname(login_clicks, dashboard_clicks, rmarkdown_clicks, username, password):
    ctx = dash.callback_context

    if not ctx.triggered:
        raise PreventUpdate

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'login-button':
        if username == 'demo' and password == 'password':
            return '/main'
        else:
            return '/'
    elif button_id == 'dashboard-button':
        return '/dashboard'
    elif button_id == 'rmarkdown-button':
        return '/rmarkdown'


if __name__ == '__main__':
    app.run_server(debug=True)