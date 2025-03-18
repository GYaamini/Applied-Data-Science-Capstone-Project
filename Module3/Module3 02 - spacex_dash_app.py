# Import required libraries
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
# spacex_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")
max_payload = spacex_df["Payload Mass (kg)"].max()
min_payload = spacex_df["Payload Mass (kg)"].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1("SpaceX Launch Records Dashboard",
                                        style={"textAlign": "center", "color": "#503D36",
                                               "font-size": 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id="site-dropdown",
                                            options=[
                                                {"label": "All Sites", "value": "All"},
                                                {"label": "CCAFS LC-40", "value": "CCAFS LC-40"},
                                                {"label": "VAFB SLC-4E", "value": "VAFB SLC-4E"},
                                                {"label": "KSC LC-39A", "value": "KSC LC-39A"},
                                                {"label": "CCAFS SLC-40", "value": "CCAFS SLC-40"}
                                            ],
                                            value="All",
                                            placeholder="Launch Siyes",
                                            searchable=True
                                ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id="success-pie-chart")),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id="payload-slider",
                                                min=0,
                                                max=10000,
                                                step=1000,
                                                value=[min_payload, max_payload],
                                                marks={0: "0(Kg)",2500: "2500 (Kg)", 5000: "5000 (Kg)",7500: "7500 (Kg)", 10000: "10000 (Kg)"}
                                ),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id="success-payload-scatter-chart")),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(
    Output(component_id="success-pie-chart", component_property="figure"),
    Input(component_id="site-dropdown", component_property="value")  
)
def get_pie_chart(input_site):
    df = spacex_df
    if input_site == "All":
        df = df[df["class"] == 1]
        fig = px.pie(df,
            values="class",
            names="Launch Site",
            title="Total Succes Launch by Sites"
        )
    else:
        df = df[df["Launch Site"] == input_site].groupby(["class"]).size()
        fig = px.pie(df,
            values=df.values,
            names=df.index,
            title=f"Total Succes Launch by {input_site}"
        )
    return fig

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id="success-payload-scatter-chart", component_property="figure"),
    [Input(component_id="site-dropdown", component_property="value"),
    Input(component_id="payload-slider", component_property="value")]
)
def get_scatter_chart(input_site,payload):
    minload, maxload = payload[0], payload[1]
    df = spacex_df[spacex_df["Payload Mass (kg)"].between(minload,maxload)]
    if input_site == "All":
        fig = px.scatter(df,
            x="Payload Mass (kg)",
            y="class",
            color="Booster Version Category",
            title="Payload vs. Success for All Sites"
        )
    else:
        df = df[df["Launch Site"] == input_site]
        fig = px.scatter(df,
            x="Payload Mass (kg)",
            y="class",
            color="Booster Version Category",
            title=f"Payload vs. Success for {input_site}"
        )
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
