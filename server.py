import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
from dash.exceptions import PreventUpdate

import numpy as np

import pandas as pd

import plotly
import plotly.graph_objects as go

from flask import Flask, request
from flask import render_template

import requests
import json

import plotly.graph_objects as go

# app = Flask(__name__)
app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    html.H1('Servidor do Sensor de temperatura'),
    html.H3('OBS: INICIAR o client.py'),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    html.H3('* 10 ultimos resultados na rota " /ultimosDezDados" '),
    html.H3('* Graficos na rota " /graficos" '),
    html.H3('* Botoes de envio de sinais na rota " /botoes" ')
])



# @app.route('/')
# def index():
# 	return '''<H1>Simulação Sistema Embarcado Client</H1>
# 				<H2>Sinal Digital</H2>
# 				<form action="http://127.0.0.1:8000/digital" method="GET">
# 						valor:<input type="text" value = "1" name="valor1" readonly>
# 						<input type="submit">
# 				</form>
# 				<form action="http://127.0.0.1:8000/digital" method="GET">
# 						valor:<input type="text" value = "0" name="valor1" readonly>
# 						<input type="submit">
# 				</form>
# 				<H2>Sinal Analógico</H2>
# 				<form action="http://127.0.0.1:8000/somar" method="GET">
# 					Sinal Analógico <input type="text" name="valor1" readonly>
# 					<input type="submit">
# 				</form>
# 				<form action="http://127.0.0.1:8000/somar" method="GET">
# 					Sinal Analógico <input type="text" name="valor1" readonly>
# 					<input type="submit">
# 				</form>'''

global informacao_sensor
ultimos_dez_dados = []
i = 0
@server.route('/postandoJson', methods=['POST'])
def recebeJson():
    # print (request.is_json)
    informacao_sensor = request.get_json()
    if len(ultimos_dez_dados)>9:
    	# print("len(ultimos_dez_dados): " +str(len(ultimos_dez_dados)))
    	ultimos_dez_dados.pop(0)
    	ultimos_dez_dados.append(request.get_json())
    else:
    	ultimos_dez_dados.append(request.get_json())

    print (informacao_sensor)
    return 'JSON postado'


global informacao_sensor
@server.route('/ultimosDezDados')
def ultimosDezDados():
	df = pd.DataFrame(data=ultimos_dez_dados)
	html = df.to_html()
	return "<H1>Informação do sensor de temperatura</H1>" + html

def geraGraph():
	return html.Div([
	    html.H1('TESTE'),
	    html.H3('OBS: INICIAR o client.py'),
	    dcc.Location(id='url', refresh=False),
	    html.Div(id='page-content'),
	])


def gerar_graficos():
    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame(data=ultimos_dez_dados)


    data = [
        go.Bar(
            x=y, # assign x as the dataframe column 'x'
            y=df['LIGADO'],
            marker_color='lightsalmon',
            text='Tempo X Ligado'
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    data2 = [
        go.Bar(
            x=y, # assign x as the dataframe column 'x'
            y=df['TEMPERATURA'],
            text='Tempo X Temperatura'
        )
    ]

    graphJSON1 = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(data2, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON1, graphJSON2

@server.route('/graficos')
def graficos():
	bar = gerar_graficos()
	return render_template('graficos.html', plot=bar[0], plot2=bar[1])
	


@server.route('/botoes')
def cria_botoes():
	return '''<H1>Simulação Sistema Embarcado (server)</H1>
				<H2>Sinal Digital</H2>
				<form action="http://127.0.0.1:5000/recebeComandoDigital" method="POST">
						valor:<input type="text" value = "1" name="valor1">
						<input type="submit">
				</form>
				<H2>Sinal Analógico</H2>
				<form action="http://127.0.0.1:5000/recebeComandoAnalogico" method="POST">
						valor:<input type="text" value = "50.12345" name="valor1">
						<input type="submit">
				</form>'''
	

# def json_post():
	
# 	if request.method == 'POST':
# 		valor1 = request.args.get('valor1')
		
# 		# print(json.dumps(request.json(), indent=2))

# 		# if valor1 == '1':
			
# 		# 	# valor2 = request.args.get('valor2')
# 		# 	# resultado = int(valor1) + int(valor2)
# 		# 	# _RESULTADO[0] = valor1 #Global
# 		# 	# _RESULTADO[1] = valor2 #Global
# 		# 	# _RESULTADO[2] = resultado #Global
# 		# 	print("\n\n________SINAL DIGITAL!_________ ")
# 		# 	print("Valor: "+ str(valor1)+"\n\n")

# 		# elif valor1 == '0':
# 		# 	print("\n\n________SINAL DIGITAL!_________ ")
# 		# 	print("Valor: "+ str(valor1)+"\n\n")

# 	return '<H2>________SINAL DIGITAL!_________</H2><br><H3> de valor: ' + str(valor1)+'</H3>'

# @app.route('/analogico', methods=['GET'])
# def analogico():
	
# 	if request.method == 'GET':
# 		valor1 = request.args.get('valor1')
# 		if valor1 == '1':
			
# 			# valor2 = request.args.get('valor2')
# 			# resultado = int(valor1) + int(valor2)
# 			# _RESULTADO[0] = valor1 #Global
# 			# _RESULTADO[1] = valor2 #Global
# 			# _RESULTADO[2] = resultado #Global
# 			print("\n\n________SINAL DIGITAL!_________ ")
# 			print("Valor: "+ str(valor1)+"\n\n")

# 		elif valor1 == '0':
# 			print("\n\n________SINAL DIGITAL!_________ ")
# 			print("Valor: "+ str(valor1)+"\n\n")

# 	return '<H2>________SINAL DIGITAL!_________</H2><br><H3> de valor: ' + str(valor1)+'</H3>'

# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     if pathname == '/ultimosDezDados':
#          ultimosDezDados()
#     elif pathname == '/graficos':
#          return layout2
#     else:
#         return app.layout

if __name__ == '__main__':
    app.run_server(port=8000, debug=True)
    # app.run( debug=True, port=8000 )