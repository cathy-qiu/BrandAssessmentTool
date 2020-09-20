import pandas as pd  # (version 1.0.0)
import plotly.express as px  # (version 4.7.0)
import plotly.io as pio
import numpy as np
import plotly.graph_objects as go
import dash  # (version 1.9.1) pip install dash==1.9.1
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# df = df.groupby(['ID','CUISINE DESCRIPTION','CAMIS'], as_index=False)['SCORE'].mean()
# df = df.set_index('INSPECTION DATE')
# df = df.loc['2016-01-01':'2019-12-31']
# df = df.groupby([pd.Grouper(freq="M"),'CUISINE DESCRIPTION'])['SCORE'].mean().reset_index()
# print (df[:5])

df = pd.read_csv('Brand_EPA_Cars.csv')
app = dash.Dash(__name__)

x_eye = -1.25
y_eye = 2
z_eye = 0.5

app.layout = html.Div([

    html.Div([
        dcc.Graph(id='our_graph')
    ], className='nine columns'),

    html.Div([

        html.Br(),
        # html.Div(id='output_data'),
        # html.Br(),

        html.Label(['Choose column:'], style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='option1',
                     options=[{'label': 'ID', 'value': 'ID'}],
                     # optionHeight=35,                    #height/space between dropdown options
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
        dcc.Dropdown(id='option2',
                     options=[{'label': 'Sex', 'value': 'Sex'}],
                     # optionHeight=35,                    #height/space between dropdown options
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
                     persistence_type='memory',
                     ),

        dcc.Dropdown(id='option3',
                     options=[{'label': 'Age', 'value': 'Age'}],
                     # optionHeight=35,                    #height/space between dropdown options
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
                     persistence_type='memory',
                     ),

        dcc.Dropdown(id='option4',
                     options=[{'label': 'Education', 'value': 'Education'}],
                     # optionHeight=35,                    #height/space between dropdown options
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
                     persistence_type='memory',
                     ),

        dcc.Dropdown(id='option5',
                     options=[{'label': 'Income', 'value': 'Income'}],
                     # optionHeight=35,                    #height/space between dropdown options
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
                     persistence_type='memory',
                     ),

        # 'local': browser cookies are deleted
    ], className='five columns'),

])


# ---------------------------------------------------------------
# Connecting the Dropdown values to the graph
# @app.callback(
#     Output(component_id='our_graph', component_property='figure'),
#     [Input(component_id='my_dropdown', component_property='value')]
# )

@app.callback(
    Output('our_graph', 'figure'),
    [Input('option1', 'value'),
     Input('option2', 'value'),
     Input('option3', 'value'),
     Input('option4', 'value'),
     Input('option5', 'value')]
)
def build_graph(option1, option2, option3, option4, option5):
    dff = df
    fig = px.scatter_3d(
        data_frame=df,
        x='Evaluation',
        y='Potency',
        z='Activity',
        color="Brand",
        color_discrete_sequence=['magenta', 'green', 'blue', 'yellow'],
        color_discrete_map={'Toyota': 'red', 'Ford': 'blue', 'BMW': 'gold', 'Mercedes': 'black'},
        opacity=0.7,  # opacity values range from 0 to 1
        # symbol='Year',            # symbol used for bubble
        # symbol_map={"2005": "square-open", "2010": 3},
        # size='resized_pop',       # size of bubble
        # size_max=5,              # set the maximum mark size when using size
        # log_x=True,  # you can also set log_y and log_z as a log scale
        range_y=[-4, 4],  # you can also set range of range_y and range_x
        template='seaborn',  # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
        # 'plotly_white', 'plotly_dark', 'presentation',
        # 'xgridoff', 'ygridoff', 'gridon', 'none'
        title='Database 1: Brand EPA ratings',
        # labels={'Years in school (avg)': 'Years Women are in School'},
        hover_data={'Brand': False},
        hover_name='Brand',  # values appear in bold in the hover tooltip
        height=700,  # height of graph in pixels

        # animation_frame='Year',   # assign marks to animation frames
        # range_x=[500,100000],
        # range_z=[0,14],
        # range_y=[5,100]

    )  # fig.update_traces(textinfo='label')
    fig.update_layout(scene_camera_eye=dict(x=x_eye, y=y_eye, z=z_eye),
                      updatemenus=[dict(type='buttons',
                                        showactive=False,
                                        y=1,
                                        x=0.8,
                                        xanchor='left',
                                        yanchor='bottom',
                                        pad=dict(t=45, r=10),
                                        buttons=[dict(label='Play',
                                                      method='animate',
                                                      args=[None, dict(frame=dict(duration=250, redraw=True),
                                                                       transition=dict(duration=0),
                                                                       fromcurrent=True,
                                                                       mode='immediate'
                                                                       )]
                                                      )
                                                 ]
                                        )
                                   ]
                      )

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
