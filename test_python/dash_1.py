#!/usr/bin/python
# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go

import pandas as pd

# задаём лейаут (макет)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[

    # формируем заголовок
    html.H1(children='Линейная функция'),

    # график
    dcc.Graph(
        figure={
            'data': [go.Scatter(x=pd.Series(range(-100, 100, 1)),
                                y=pd.Series(range(-100, 100, 1)),
                                mode='lines',
                                name='linear_func')],
            'layout': go.Layout(xaxis={'title': 'x'},
                                yaxis={'title': 'y'})
        },
        id='linear_func_id'
    ),

])

# описываем логику дашборда
if __name__ == '__main__':
    app.run_server(debug=True)