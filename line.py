import export as export
import flask
import pandas as pd  # (version 1.0.0)
import plotly  # (version 4.5.4) pip install plotly==4.5.4
import plotly.express as px
from flask import Flask
from gevent.pywsgi import WSGIServer
import dash  # (version 1.9.1) pip install dash==1.9.1
import dash_core_components as dcc
import dash_html_components as html
from dash import development
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
# export FLASK_ENV=development
# flask run

# ---------------------------------------------------------------
# Taken from https://opendata.cityofnewyork.us/
df = pd.read_csv("Brand_EPA_Cars.csv")

# ---------------------------------------------------------------
app.layout = html.Div([

    html.Div([
        dcc.Graph(id='our_graph')
    ], className='nine columns'),

    html.Div([

        html.Br(),
        html.Div(id='output_data'),
        html.Br(),

        html.Label(['Choose column:'], style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='my_dropdown',
                     options=[
                         {'label': 'ID', 'value': 'ID'},
                         {'label': 'Sex', 'value': 'Sex'},
                         {'label': 'Age', 'value': 'Age'},
                         {'label': 'Education', 'value': 'Education'},
                         {'label': 'Income', 'value': 'Income'}
                     ],
                     optionHeight=35,  # height/space between dropdown options
                     value='ID',  # dropdown value selected automatically when page loads
                     disabled=False,  # disable dropdown value selection
                     multi=False,  # allow multiple dropdown values to be selected
                     searchable=True,  # allow user-searching of dropdown values
                     search_value='',  # remembers the value searched in dropdown
                     placeholder='Please select...',  # gray, default text shown when no option is selected
                     clearable=True,  # allow user to removes the selected value
                     style={'width': "100%"},  # use dictionary to define CSS styles of your dropdown
                     # className='select_box',           #activate separate CSS document in assets folder
                     persistence=True,  # remembers dropdown value. Used with persistence_type
                     persistence_type='memory'  # remembers dropdown value selected until...
                     ),  # 'memory': browser tab is refreshed
        # 'session': browser tab is closed
        # 'local': browser cookies are deleted
    ], className='three columns'),

])


# ---------------------------------------------------------------
# Connecting the Dropdown values to the graph
@app.callback(
    Output(component_id='our_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)
def build_graph(column_chosen):
    dff = df
    fig = px.scatter_3d(dff, names=column_chosen)
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(title={'text': 'Database 2: Entities EPA scores',
                             'font': {'size': 28}, 'x': 0.5, 'xanchor': 'center'})
    return fig


# ---------------------------------------------------------------
# For tutorial purposes to show the user the search_value

@app.callback(
    Output(component_id='output_data', component_property='children'),
    [Input(component_id='my_dropdown', component_property='search_value')]
)
def build_graph(data_chosen):
    return 'Search value was: " {} "'.format(data_chosen)


# ---------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
