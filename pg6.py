import dash
from dash import dcc, html
import plotly.express as px

dash.register_page(__name__,
                   path='/Volunteers',
                   name='Volunteers',
                   title='Volunteers',
                   description='Learn all about the heatmap3.'
)


layout = html.Div([
    dcc.Markdown('### Volunteers Analysis here...'),
    html.Hr()
])