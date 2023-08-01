import pandas as pd
import datetime as dt
import dash
from dash import dcc, html, callback, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   path='/Demo3',
                   name='Demo - Chained Callback',
                   title='Demo3',
                   description='Chained Callback Demo'
) 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# layout = html.Div([
#     dcc.Markdown('### Chained callback demo here...'),
#     html.Hr(),
# ])

# Data from U.S. Congress, Joint Economic Committee, Social Capital Project. https://www.jec.senate.gov/public/index.cfm/republicans/2018/4/the-geography-of-social-capital-in-america
df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Callbacks/chained_callback/social-capital-project.csv")

layout = html.Div([
    dcc.Markdown('### Chained Callback Demo'),
    html.Hr(),
    html.Label("State:", style={'fontSize':24, 'textAlign':'center'}),
    dcc.Dropdown(
        id='states-dpdn',
        options=[{'label': s, 'value': s} for s in sorted(df.State.unique())],
        value='Alaska',
        clearable=False
    ),

    html.Label("Counties:", style={'fontSize':24, 'textAlign':'center'}),
    dcc.Dropdown(id='counties-dpdn', options=[], multi=True),

    dcc.Graph(id='display-map', figure={})
])


# Populate the options of counties dropdown based on states dropdown
@callback(
    Output('counties-dpdn', 'options'),
    Input('states-dpdn', 'value')
)
def set_cities_options(chosen_state):
    dff = df[df.State==chosen_state]
    return [{'label': c, 'value': c} for c in sorted(dff.County.unique())]


# populate initial values of counties dropdown
@callback(
    Output('counties-dpdn', 'value'),
    Input('counties-dpdn', 'options')
)
def set_cities_value(available_options):
    return [x['value'] for x in available_options]


@callback(
    Output('display-map', 'figure'),
    Input('counties-dpdn', 'value'),
    Input('states-dpdn', 'value')
)
def update_grpah(selected_counties, selected_state):
    if len(selected_counties) == 0:
        return dash.no_update
    else:
        dff = df[(df.State==selected_state) & (df.County.isin(selected_counties))]

        fig = px.scatter(dff, x='% without health insurance', y='% in fair or poor health',
                         color='% adults graduated high school',
                         trendline='ols',
                         size='bubble_size',
                         hover_name='County',
                         # hover_data={'bubble_size':False},
                         labels={'% adults graduated high school':'% graduated high school',
                                 '% without health insurance':'% no health insurance',
                                 '% in fair or poor health':'% poor health'}
                         )
        return fig
