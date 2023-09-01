import pandas as pd
from dash import Dash, Input, Output, dcc, html

data = (
    pd.read_csv("Assets/Data/df_bp1.csv")
    .assign(Date=lambda data: pd.to_datetime(data["date"], format="%Y%m%d"))
    .sort_values(by="date")
)


teams = data["team_h"].sort_values().unique()
seasons = data["season"].sort_values().unique()
#avocado_types = data["type"].sort_values().unique()

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "MLB Game Prediction"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="⚾", className="header-emoji"),
                html.H1(
                    children="MLB Game Data", className="header-title"
                ),
                html.P(
                    children=(
                        "Analyze the game data from seasons 1980-2022"
                        " in order to build a model to predict metrics"
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        ),

 

        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Team", className="menu-title"),
                        dcc.Dropdown(
                            id="team-filter",
                            options=[
                                {"label": team, "value": team}
                                for team in teams
                            ],
                            value="ANA",
                            clearable=False,
                            className="dropdown",
                        ),
                       
                    ]
                ),
               
                
            ],
            className="menu",
        ),


        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="home-batting-chart",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="opp-batting-chart",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)


@app.callback(
    Output("home-batting-chart", "figure"),
    Output("opp-batting-chart", "figure"),
    Input("team-filter", "value"),
    
)
def update_charts(team):
    filtered_data = (
        data.query("team_h == @team")
        .assign(Date=lambda data: pd.to_datetime(data["date"], format="%Y%m%d"))
        .sort_values(by="date")
    
    )
    home_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["BATAVG_162_h"],
                "type": "lines",
                "hovertemplate": "%{y:.3f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Home Batting Average",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#17B897"],
        },
    }

    opp_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["BATAVG_162_v"],
                "type": "lines",
                "hovertemplate": "%{y:.3f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {"text": "Opp Batting Average", "x": 0.05, "xanchor": "left"},
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#E12D39"],
        },
    }
    return home_chart_figure, opp_chart_figure


if __name__ == "__main__":
    app.run_server(debug=True)
