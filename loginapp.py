import dash
from dash import html, dcc, callback, Output, Input, State
import pandas as pd 

#Load the cholesterol data
agedata = pd.read_csv("agedata.csv")

#Dash app
app = dash.Dash(__Chol__)
#Layout for login
