import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

# To create meta tag for each page, define the title, image, and description.
dash.register_page(__name__,
                   path='/',  # '/' is home page and it represents the url
                   name='Home',  # name of page (name of sidebar link)
                   title='Index',  # title that appears on browser's tab
                   description='Summary metrics page'
)

layout = html.Div([
    dcc.Markdown('### Summary metrics here...'),
    html.Hr()
    
])

