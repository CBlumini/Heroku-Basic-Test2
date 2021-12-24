import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

server = app.server

test = pd.read_csv('s3://tridata/Santa-Cruz-Sprint.csv')
females = test[test['Gender']=='F']

#data = [[20, 10], [30, 15], [25, 14]]
#females = pd.DataFrame(data, columns = ['Age', 'Gender Place'])

#print(test)
#print(females)

fig = px.scatter(females, x=females['Age'], y=females['Gender Place'])

app.layout = html.Div(children=[
    html.H1(children='Hi Samantha!!!'),

    html.Div(children='''
        Here is some data from the Women at the Sata Cruz Sprint!
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

