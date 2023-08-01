import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import datetime as dt

dash.register_page(__name__,
                   path='/Ministries',
                   name='Ministries',
                   title='Ministries',
                   description='Learn all about CBC ministries'
)

# page 4 data
df = pd.read_csv("https://raw.githubusercontent.com/BGQM/CBC/main/CBC_Ministries.csv")
df['Date'] = pd.to_datetime(df['Date']) #Note: this is required to make into a datetime object
df = df.set_index('Date')
df['Month'] = df.index.month_name()
df['Year'] = df.index.year
year_list = sorted(df['Year'].unique())#Note: sorting is probably not necessary
max_year = df['Year'].max()

layout = html.Div([
    dcc.Markdown('### CBC Ministries - People Served'),
    html.Hr(),
    dbc.RadioItems(id='year_radio', options=year_list, value=max_year, inline=True,
        labelStyle={'display':'inline-block', 'marginLeft': '10px'}),
    html.Hr(),
    dcc.Dropdown(id='ministries_dpdn', options=[], multi=True),
    dcc.Graph(id='graph2', figure={}),
    html.Hr(),
    ])

# Determine the options of ministries based on the year selected
@callback(
    Output('ministries_dpdn', 'options'),
    Input('year_radio', 'value')
)
def set_ministries_options(chosen_year):
    dff = df[df.Year==chosen_year]
    return [{'label': c, 'value': c} for c in sorted(dff.Ministry.unique())]

# Populate the initial values of ministries dropdown based on the year selected
@callback(
    Output('ministries_dpdn', 'value'),
    Input('ministries_dpdn', 'options')
)
def set_ministries_value(available_options):
    return [x['value'] for x in available_options]

# Update graph based on year selected and ministry(s) selected
@callback(
    Output('graph2', 'figure'),
    Input('year_radio', 'value'),
    Input('ministries_dpdn','value')   
)
def update_graph(selected_year, selected_ministries):
    if selected_year is None:
        return dash.no_update
    else:
        dff = df[(df.Year==selected_year) & (df.Ministry.isin(selected_ministries))]
        total_quantity = round((dff['Quantity'].sum()),0)
        chart_title = str(selected_year) + '   Total Served:  ' + str(total_quantity)
        fig = px.histogram(dff, x='Month', y='Quantity', color='Ministry', barmode='group', 
        text_auto=True, title=chart_title
        )
    return fig


