"""
Planet Feedback: Intelligent Employer Profiling Platform

Module Name: Interface Module
Source Path: interface.py

This file is Copyright (c) 2022 Harvey Ronan Donnelly and Ewan Robert Jordan.
"""

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from dash import Input, Output, dcc, html
import json
from plotly.subplots import make_subplots

f = open('data/output.json')
employers = json.load(f)
employer_names = employers.keys()

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

controls = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("Employer Name"),
                dcc.Dropdown(
                    id="employer-name",
                    options=[
                        {"label": col, "value": col} for col in employer_names
                    ],
                    value="Nokia",
                ),
            ]
        ),
    ],
    body=True,
)

app.layout = dbc.Container(
    [
        dbc.Container([
        html.Br(),
        html.Hr(),
        html.Img(src='https://raw.githubusercontent.com/HarveyRDonnelly/planet-feedback/master/graphics/logo.png',
                 style={'height': '100px'}),
        html.Hr(),
        html.H1("Intelligent Employer Profiling Platform"),
        html.H3("Daisy Intelligence Hackathon 2022 Prototype"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(dbc.Card([html.H2("Search Employers"), controls]), md=4, style={'height': '80vh'}),
                dbc.Col(dbc.Card([html.H2("Employer Metrics"), dcc.Graph(id="planet-feedback-metrics",
                                                                        style={'width': '70vh', 'height': '80vh'})]),
                        md=8),
            ],
            align="center",
        )]),
        html.Hr(),
        html.H3("Copyright © 2022 Harvey Ronan Donnelly and Ewan Robert Jordan", style={"text-align": "center"}),
        html.Hr()

    ],
    fluid=True,
)


@app.callback(
    Output("planet-feedback-metrics", "figure"),
    [
        Input("employer-name", "value"),
    ],
)
def make_graph(employer_name: str):
    # Create subplots, using 'domain' type for pie charts

    current_employer = employers[employer_name]

    pf_score = current_employer['pf_score']
    pay_score = current_employer['pay_score'][2]
    equality_score = current_employer['equality_score'][2]
    workload_score = current_employer['workload_score'][2]
    work_environment_score = current_employer['work_environment_score'][2]
    employees_score = current_employer['employees_score'][2]
    job_requirements_score = current_employer['job_requirements_score'][2]
    management_score = current_employer['management_score'][2]


    specs = [[{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}], [{'type': 'domain'}, {'type': 'domain'},
                                                                                                {'type': 'domain'},
                                                                                                {'type': 'domain'}],
             [{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}], [{'type': 'domain'}, {'type': 'domain'},
                                                                                                {'type': 'domain'},
                                                                                                {'type': 'domain'}]]
    fig = make_subplots(rows=4, cols=4, specs=specs)

    # Define pie charts
    fig.add_trace(go.Pie(title="OVERALL", values=[1],
                         marker_colors=['rgb(255, 255, 255)'], name="OVERALL"), 1, 1)
    fig.add_trace(go.Pie(title=str(round(pf_score, 1)), values=[pf_score + 5, 5 - pf_score], name='PF Score',
                         marker_colors=['rgb(0, 119, 91)', 'rgb(133, 214, 195)']), 1, 2)
    fig.add_trace(go.Pie(title="PAY", values=[1],
                         marker_colors=['rgb(255, 255, 255)'], name="PAY"), 1, 3)
    fig.add_trace(go.Pie(title=str(round(pay_score, 1)), values=[pay_score + 5, 5 - pay_score], name='Pay Score',
                         marker_colors=['rgb(0, 119, 91)', 'rgb(133, 214, 195)']), 1, 4)

    fig.add_trace(go.Pie(title="EQUALITY", values=[1],
                         marker_colors=['rgb(255, 255, 255)'], name="EQUALITY"), 2, 1)
    fig.add_trace(go.Pie(title=str(round(equality_score, 1)), values=[equality_score + 5, 5 - equality_score], name='Equality Score',
                         marker_colors=['rgb(0, 119, 91)', 'rgb(133, 214, 195)']), 2, 2)
    fig.add_trace(go.Pie(title="WORKLOAD", values=[1],
                         marker_colors=['rgb(255, 255, 255)'], name="WORKLOAD"), 2, 3)
    fig.add_trace(go.Pie(title=str(round(workload_score, 1)), values=[workload_score + 5, 5 - workload_score], name='Workload Score',
                         marker_colors=['rgb(0, 119, 91)', 'rgb(133, 214, 195)']), 2, 4)

    fig.add_trace(go.Pie(title="WORK ENV.", values=[1],
                         marker_colors=['rgb(255, 255, 255)'], name="WORK ENV."), 3, 1)
    fig.add_trace(go.Pie(title=str(round(work_environment_score, 1)), values=[work_environment_score + 5, 5 - work_environment_score], name='Work Environment',
                         marker_colors=['rgb(0, 119, 91)', 'rgb(133, 214, 195)']), 3, 2)
    fig.add_trace(go.Pie(title="EMPLOYEES", values=[1],
                         marker_colors=['rgb(255, 255, 255)'], name="EMPLOYEES"), 3, 3)
    fig.add_trace(go.Pie(title=str(round(employees_score, 1)), values=[employees_score + 5, 5 - employees_score], name='Employees Score',
                         marker_colors=['rgb(0, 119, 91)', 'rgb(133, 214, 195)']), 3, 4)

    fig.add_trace(go.Pie(title="JOB REQ.", values=[1],
                         marker_colors=['rgb(255, 255, 255)'], name="JOB REQ."), 4, 1)
    fig.add_trace(go.Pie(title=str(round(job_requirements_score, 1)), values=[job_requirements_score + 5, 5 - job_requirements_score], name='Job Requirement Score',
                         marker_colors=['rgb(0, 119, 91)', 'rgb(133, 214, 195)']), 4, 2)
    fig.add_trace(go.Pie(title="MANAGEMENT.", values=[1],
                         marker_colors=['rgb(255, 255, 255)'], name="MANAGEMENT."), 4, 3)
    fig.add_trace(go.Pie(title=str(round(management_score, 1)), values=[management_score + 5, 5 - management_score], name='Management Score',
                         marker_colors=['rgb(0, 119, 91)', 'rgb(133, 214, 195)']), 4, 4)

    # Tune layout and hover info
    fig.update_traces(hole=.5, hoverinfo='percent+name', textinfo='none')
    fig.update(layout_showlegend=False)

    fig = go.Figure(fig)

    return fig


if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
