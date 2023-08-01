# This works fine.
# import dash
# from dash import dcc, html, callback, Output, Input
# import plotly.express as px
# import dash_bootstrap_components as dbc
# import pandas as pd
# import datetime as dt

import pandas as pd
import datetime as dt
import dash
from dash import dcc, html, callback, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   path='/Groups',
                   name='Groups',
                   title='Groups',
                   description='Learn all about CBC groups'
)

# page data

# #Initialize app
# app = Dash(__name__)
# server = app.server

df = pd.read_csv("https://raw.githubusercontent.com/BGQM/fpl/main/FPL_Bills.csv")
df['Date'] = pd.to_datetime(df['Date']) #Note: this is required to make into a datetime object
df = df.set_index('Date')
df['Month'] = df.index.month_name()
df['Year'] = df.index.year
year_list = sorted(df['Year'].unique())#Note: sorting is probably not necessary
max_year = df['Year'].max()

layout = html.Div([
    dcc.Markdown('### Groups Analysis here...'),
    html.Hr(),
    # dcc.Markdown('#### Electricity Usage Sample Graph'),
    # html.Hr(),
    
#     dcc.RadioItems(id='selected_year', options=year_list, value=max_year, inline=True,
#         labelStyle={'display':'inline-block','padding':'50','margin-left': '10px'}),
#     html.Hr(),
#     html.Button('Select kWh/Cost', n_clicks=0, id='button'),
#     dcc.Graph(id="graph"),
#     html.Hr(),
])

# @callback(
#     Output("graph", "figure"), 
#     Input("selected_year", "value"),
#     Input("button", "n_clicks")
#     )

# def display_graph(value,n_clicks):
#     dff = df.loc[str(value)]
#     avg_kWh = round(dff['Total'].sum()/dff['kWh'].sum(),3)
#     if n_clicks % 2 == 0:
#         x, y = dff['Month'], dff['kWh']
#         chart_title = str(dff['kWh'].sum()) + " kWh"
#     else:
#         x, y = dff['Month'], dff['Total']
#         chart_title = str(dff['Total'].sum()) + " ($)"
#     fig = px.bar(dff, x=x, y=y, text_auto=True, title='Total Usage/Cost = ' + chart_title + "  --  Average Price: $/" + str(avg_kWh))
#     #print(value)#this is just for monitoring
#     #print(n_clicks)#this is just for monitoring
#     #print(df2)   
#     return fig

#     #Run app
# if __name__ == '__main__':
#     app.run(debug=True)