import pandas as pd
import datetime as dt
import dash
from dash import dcc, html, callback, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   path='/Demo2',
                   name='Demo - Life Expectancy',
                   title='Demo2',
                   description='Life Expectancy Demo'
) 
   
#Page data
df = px.data.gapminder()

layout = html.Div(
    [
        dcc.Markdown('### Average Life Expectancy Demo'),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Dropdown(options=df.continent.unique(),
                                     id='cont-choice')
                    ], xs=10, sm=10, md=8, lg=4, xl=4, xxl=4
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(id='line-fig',
                                  figure=px.histogram(df, x='continent',
                                                      y='lifeExp',
                                                      histfunc='avg'))
                    ], width=12
                )
            ]
        )
    ]
)

@callback(
    Output('line-fig', 'figure'),
    Input('cont-choice', 'value')
)
def update_graph(value):
    if value is None:
        fig = px.histogram(df, x='continent', y='lifeExp', histfunc='avg',text_auto=True)
    else:
        dff = df[df.continent==value]
        fig = px.histogram(dff, x='country', y='lifeExp', histfunc='avg',text_auto=True)
    return fig
