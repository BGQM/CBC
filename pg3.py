import dash
from dash import dcc, html
import plotly.express as px

dash.register_page(__name__,
                   path='/Giving',
                   name='Giving',
                   title='Giving',
                   description='Learn all about giving'
)

layout = html.Div([
    dcc.Markdown('### Giving Analysis here...'),
    html.Hr()
])