# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout=html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                             style={'textAlign':'center', 'color':'#503D36','font-size':40}),
                              # Add a dropdown list to enable Launch Site selection
                              dcc.Dropdown(id='site-dropdown',
                                           options=[
                                               {'label':'All Sites', 'value':'All'},
                                               {'label':'CCAFS LC-40','value':'CCAFS LC-40'},
                                               {'label':'VAFB SLC-4E', 'value':'VAFB SLC-4E'},
                                               {'label':'KSC LC-39A', 'value':'KSC LC-39A'},
                                               {'label':'CCAFS SLC-40', 'value':'CCAFS SLC-40'}
                                           ],
                                           value='ALL',
                                           placeholder="Select a Launch Site here",
                                           searchable=True
                                          ),
                             html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),
                               html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                min=0,
                                max=10000,
                                step=1000,
                                value=[min_payload,max_payload],
                                marks={
                                0: '0 kg',
                                2500: '2500',
                                5000: '5000',
                                7500: '7500',
                                10000: '10000'
                                }),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])
 #TASK 2: Add a callback function to render success-pie-chart based on selected site dropdown

# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))

def get_pie(value):
    filtered_df = spacex_df
    if value == 'All':
        filtered_df = spacex_df.groupby('Launch Site').sum().reset_index()
        #fig = px.pie(filtered_df, values='Launch Site', names='class', title='Total Success Launches By Site')
        fig = px.pie(filtered_df, values='class', names='Launch Site', title='Total Success Launches By Site')
        return fig

    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == value].groupby(['Launch Site', 'class']). \
        size().reset_index(name='class count')
        title = f"Total Success Launches for site {value}"
        fig = px.pie(filtered_df,values='class count', names='class', title=title)
        return fig
#TASK 3: Add a Range Slider to Select Payload
                              
         

#TASK 4: Add a callback function to render the success-payload-scatter-chart scatter plot    
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id='payload-slider', component_property='value')])
def get_scatter_chart(selected_site, payload_range):
    low, high = payload_range
    if selected_site == 'All':
        df = spacex_df
    else:
        df = spacex_df[spacex_df['Launch Site'] == selected_site]
    df_mask = df[(df['Payload Mass (kg)'] >= low) & (df['Payload Mass (kg)'] <= high)]

    fig = px.scatter(df_mask, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                     title='Correlation between Payload and Success')
    
    return fig           


# Run the app
if __name__ == '__main__':
    app.run_server()
