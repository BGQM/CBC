import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   path='/Attendance',  # represents the url text
                   name='Attendance',  # name of page, commonly used as name of link
                   title='Attendance',  # title that appears on browser's tab
                   description='Attendance analysis'
)

layout = html.Div([
    dcc.Markdown('### Attendance Analysis here...'),
    html.Hr()
])


# page 2 data
# df = px.data.tips()

# layout = html.Div(
#     [
#     dcc.Markdown('### Attendance Analysis here...'),
#     html.Hr(),
#         dbc.Row([
#             dbc.Col(
#                 width=2
#             ),
#             dbc.Col(
#                 [
#                     dcc.RadioItems(df.day.unique(), id='day-choice', value='Sat')
#                 ], width=6
#             )
#         ]),
#         dbc.Row([
#             dbc.Col(
#                 [
#                     dcc.Graph(id='bar-fig',
#                               figure=px.bar(df, x='smoker', y='total_bill'))
#                 ], width=12
#             )
#         ])
#     ]
# )


# @callback(
#     Output('bar-fig', 'figure'),
#     Input('day-choice', 'value')
# )
# def update_graph(value):
#     dff = df[df.day==value]
#     fig = px.bar(dff, x='smoker', y='total_bill')
#     return fig
