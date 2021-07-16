# Dash app coopy the code of dash app
import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


app = dash.Dash()
stock = 'BitCoin'
start = datetime.datetime(2021, 6, 1)
end = datetime.datetime(2021, 6, 30)
#df = web.DataReader(stock, 'yahoo', start, end)


#URL = 'https://drive.google.com/file/d/1xlnGC_cpA7-kojByP0Msg_gMvOEwYMJi/view?usp=sharing'
URL = 'https://drive.google.com/file/d/1ZEC-qq73OKDgpQC2FfgKt-HsNgXbCVyf/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+URL.split('/')[-2]
df=pd.read_csv(path)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)


def create_dash_application(flask_app):
    dash_app=dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash/")

    dash_app.layout = html.Div(
           children=[
            html.H1(children='BitCoin Prediction'),

            html.Div(children='''
                     Line Graph.
                     '''),

            dcc.Graph(
                id='example-graph',
                   figure={
                      'data': [
                          {'x': df.index, 'y': df.Close, 'type': 'line', 'name': stock},
                            ],
                        'layout': {
                            'title': stock
                                   }
                           }
                     ),
                 ]
           )
    return dash_app

#if __name__ == '__main__':
 #   app.run_server(debug=True)