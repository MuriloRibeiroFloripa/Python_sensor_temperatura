from flask import Flask, request
import time
import numpy as np
import matplotlib.pyplot as plt
import requests


app = Flask(__name__)


def Gerar_Analogico ():
	np.random.seed(5)
	        
	T = 80
	N = 300 # Number of points, number of subintervals = N-1
	dt = T/(N-1) # Time step
	return np.linspace(0,T,N)

# Analógico
_TEMPERATURA = Gerar_Analogico()
 
# Digital
_LIGADO = 1

def Simula_Liga_Desliga ():
	global _LIGADO
	_LIGADO += 1
	_LIGADO = _LIGADO%2
	print("\n___Troca valor da variavel _LIGADO para: " + str(_LIGADO))
	

_TEMPO = 0
_TEMPO_MAXIMO = 5
i=0

while True:
	if _LIGADO == 1:
		if _TEMPERATURA[i] < 80.0:
			print("\n- Temperatura: " + str(_TEMPERATURA[i]) + " Graus")
			time.sleep(0.01)
			i+=1

		else:
			print("\n- Temperatura Lmite: " + str(_TEMPERATURA[i]) + " Graus")
			time.sleep(2)
			i=0

	if _TEMPO%_TEMPO_MAXIMO==0:
		Simula_Liga_Desliga ()
		_TEMPO = 0

	time.sleep(1)
	_TEMPO+=1
	_INFORMACAO_SENSOR = {"LIGADO":str(_LIGADO),"TEMPERATURA":str(_TEMPERATURA[i])}
	r = requests.post('http://127.0.0.1:8000/postandoJson', json=_INFORMACAO_SENSOR)
	print("\nAguardando " + str(_TEMPO_MAXIMO) + " Secs para alterar o estado: " + str(_TEMPO) + " Secs")
		
# @app.route('/hello')
# def hello():
# 	return '<H2>________SINAL DIGITAL!_________</H2><br><H3> de valor: </H3>'

@app.route('/recebeComandoDigital', methods=['POST'])
def recebeDigital():
	
	if request.method == 'POST':
		valor1 = request.form.get('valor1')
		print("\n\n________SINAL DIGITAL!_________ ")

		if valor1 == '1':
			
			print("Valor: "+ str(valor1)+"\n\n")
			print("Ligando Sensor"+"\n\n")
			# _LIGADO = int(valor1)
			return '<H2>________SINAL DIGITAL Recebido equipamento Ligado!_________</H2><br><H3> de valor: ' + str(valor1)+'</H3>'

		elif valor1 == '0':
			print("Valor: "+ str(valor1)+"\n\n")
			print("Ligando Sensor"+"\n\n")
			# _LIGADO = int(valor1)
			return '<H2>________SINAL DIGITAL Recebido equipamento Desligado!_________</H2><br><H3> de valor: ' + str(valor1)+'</H3>'


@app.route('/recebeComandoAnalogico', methods=['POST'])
def recebeAnalogico():
	
	if request.method == 'POST':
		valor1 = request.form.get('valor1')
		print("\n\n________SINAL ANALÓGICO!_________ ")

		if valor1 == '1':
			
			print("Valor: "+ str(valor1)+"\n\n")
			print("Ligando Sensor"+"\n\n")
			# _LIGADO = int(valor1)
			return '<H2>________SINAL ANALÓGICO Recebido!_________</H2><br><H3> de valor: ' + str(valor1)+'</H3>'

		elif valor1 == '0':
			print("Valor: "+ str(valor1)+"\n\n")
			print("Ligando Sensor"+"\n\n")
			# _LIGADO = int(valor1)
			return '<H2>________SINAL ANALÓGICO Recebido!_________</H2><br><H3> de valor: ' + str(valor1)+'</H3>'


if __name__ == '__main__':
    app.run( debug=True, port=5000 )
