import pandas as pd
import datetime as dt
import dash
from dash import dcc, html, callback, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   path='/Demo1',
                   name='Demo - Electricity Usage',
                   title='Demo1',
                   description='Electricity Usage Demo'
)

# page data
df = pd.read_csv("https://raw.githubusercontent.com/BGQM/fpl/main/FPL_Bills.csv")
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df['Month'] = df.index.month_name()
df['Year'] = df.index.year
year_list = sorted(df['Year'].unique())
max_year = df['Year'].max()

layout = html.Div([
    dcc.Markdown('### FPL Electricity Usage'),
    html.Hr(),
    dbc.RadioItems(id='selected_year', options=year_list, value=max_year, inline=True, 
        labelStyle={'display':'inline-block','margin-right': '15px'}),
    html.Hr(),
    dbc.Button('Select kWh/Cost', n_clicks=0, id='button',  
    style={'margin-left':'80px'}),
    dcc.Markdown(id='chart_title',
            style={'fontSize':24, 
                    'fontWeight' : 'bold',
                    'textAlign':'center'
                    }),
    dcc.Graph(id="graph"),
    html.Hr(),
])

@callback(
    Output("graph", "figure"),
    Output('chart_title', 'children'), 
    Input("selected_year", "value"),
    Input("button", "n_clicks")
    )
def display_graph(value, n_clicks):
    dff = df.loc[str(value)]
    total_kWh = round((dff['kWh'].sum()),0)
    total_cost = round((dff['Total'].sum()),2)
    avg_kWh = round((dff['Total'].sum()/dff['kWh'].sum()),3)
    
    if n_clicks % 2 == 0:
        x, y = dff['Month'], dff['kWh']
        chart_title = str(value) + '   ---   Total  ' + str(total_kWh) + ' kWh   ---   $' + str(avg_kWh) + '/kWh'
    else:
        x, y = dff['Month'], dff['Total']
        chart_title = str(value) + '   ---   Total  $' + str(total_cost) + '   ---   $' + str(avg_kWh) + '/kWh'
    fig = px.bar(dff, x=x, y=y, text_auto=True
    )  
    return fig, chart_title


# layout = html.Div([
#     dcc.Markdown('### Electricity Usage Sample Graph'),
#     html.Hr(),
#     dbc.RadioItems(id='selected_year', options=year_list, value=max_year, inline=True, className='me-2',
#         labelStyle={'display':'inline-block','marginRight': '10px'}),
#     html.Hr(),
#     dbc.Button('Select kWh/Cost', n_clicks=0, id='button',  
#     style={'marginLeft':'80px'}),
#     dcc.Graph(id="graph"),
#     html.Hr(),

#     html.Hr(),
# ])

# @callback(
#     Output("graph", "figure"), 
#     Input("selected_year", "value"),
#     Input("button", "n_clicks")
#     )

# def display_graph(value,n_clicks):
#     dff = df.loc[str(value)]
#     total_kWh = round((dff['kWh'].sum()),0)
#     total_cost = round((dff['Total'].sum()),2)
#     avg_kWh = round((dff['Total'].sum()/dff['kWh'].sum()),3)
    
#     if n_clicks % 2 == 0:
#         x, y = dff['Month'], dff['kWh']
#         chart_title = str(value) + '   Total  ' + str(total_kWh) + ' kWh    ($' + str(avg_kWh) + '/kWh)'
#     else:
#         x, y = dff['Month'], dff['Total']
#         chart_title = str(value) + '   Total  $' + str(total_cost) + '    ($' + str(avg_kWh) + ' /kWh)'
#     fig = px.bar(dff, x=x, y=y, text_auto=True, title= chart_title)  
#     return fig
