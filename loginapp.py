import dash
from dash import html, dcc, callback, Output, Input, State
import pandas as pd 

#Load the cholesterol data
agedata = pd.read_csv("agedata.csv")

# Dash app with suppress_callback_exceptions=True
app = dash.Dash(__name__, suppress_callback_exceptions=True)

#Dash app
app = dash.Dash(__name__)
#Layout for login
login_layout = html.Div([
  html.H2("Login System"),
  html.Label("Username:"),
  dcc.Input(id='username-input', type='text', value=''),
  html.Label("Password:"),
  dcc.Input(id='password-input', type='password', value=''),
  html.Button('Log In', id='login-button'),
  html.Div(id='login-status', children='')
])

# Layout for cholesterol dashboard
dashboard_layout = html.Div([
    html.H2("Cholesterol Dashboard"),
    dcc.Dropdown(id='age-group-dropdown',
                 options=[{'label': age_group, 'value': age_group} for age_group in agedata['Age group'].unique()],
                 value=agedata['Age group'].unique()[0]),
    dcc.Graph(id='cholesterol-plot')
])

# App layout
app.layout = html.Div([
    # Initial page content is the login layout
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Callback to switch between login page and dashboard based on login status
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/dashboard':
        return dashboard_layout
    else:
        return login_layout

# Callback to handle login button click
@app.callback(
    Output('login-status', 'children'),
    [Input('login-button', 'n_clicks')],
    [State('username-input', 'value'),
     State('password-input', 'value')]
)
def handle_login(n_clicks, username, password):
    if n_clicks:
        # Simulate authentication 
        if username == 'demo' and password == 'password':
            return 'Login successful! Redirecting to dashboard...'
        else:
            return 'Invalid username or password. Please try again.'

# Callback to update dashboard based on age group selection
@app.callback(
    Output('cholesterol-plot', 'figure'),
    [Input('age-group-dropdown', 'value')]
)
def update_dashboard(age_group):
    filtered_data = agedata[agedata['Age group'] == age_group]
   
    figure = {
        'data': [{'x': filtered_data['Country'], 'y': filtered_data['Mean total cholesterol (mmol/L)'], 'type': 'bar', 'name': 'Cholesterol'}],
        'layout': {'title': f'Cholesterol Levels for {age_group} Age Group', 'xaxis': {'title': 'Country'}, 'yaxis': {'title': 'Cholesterol Levels'}}
    }
    return figure

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
    
