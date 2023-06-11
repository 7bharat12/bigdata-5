# -*- coding: utf-8 -*-
"""
Created on Wed May 24 00:17:41 2023

@author: bharat
"""


import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objs as go

dataset = pd.read_csv(r'C:\Users\bhara\Desktop\BharatChandra_AWSBigData5\sales.csv')

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Sales Analysis Dashboard"),
        html.Div(
            children=[
                dcc.Graph(
                    figure=go.Figure(
                        data=[go.Bar(
                            x=dataset['genre'],
                            y=dataset['global_sales'],
                        )],
                        layout=go.Layout(
                            title='Sales by Genre',
                            xaxis={'title': 'Genre'},
                            yaxis={'title': 'Global Sales'}
                        )
                    )
                ),
                dcc.Graph(
                    figure=go.Figure(
                        data=[go.Pie(
                            labels=dataset['platform'],
                            values=dataset['global_sales'],
                            hole=0.3
                        )],
                        layout=go.Layout(
                            title='Sales by Platform'
                        )
                    )
                ),
                dcc.Graph(
                    figure=go.Figure(
                        data=[go.Scatter(
                            x=dataset['year'],
                            y=dataset['global_sales'],
                            mode='lines',
                            marker={'color': 'blue'}
                        )],
                        layout=go.Layout(
                            title='Sales over Years',
                            xaxis={'title': 'Year'},
                            yaxis={'title': 'Global Sales'}
                        )
                    )
                ),
                dcc.Graph(
                    figure=go.Figure(
                        data=[go.Scatter(
                            x=dataset['na_sales'],
                            y=dataset['eu_sales'],
                            mode='markers',
                            marker={'color': 'red'}
                        )],
                        layout=go.Layout(
                            title='Sales in North America vs. Europe',
                            xaxis={'title': 'Sales in North America'},
                            yaxis={'title': 'Sales in Europe'}
                        )
                    )
                )
            ],
            style={'display': 'flex', 'flex-wrap': 'wrap'}
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
