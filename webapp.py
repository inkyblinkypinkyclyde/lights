#!/usr/bin/python3
from flask import Flask, render_template, request, redirect
from LightsClass import Lights

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/green', methods = ['POST'])	
def green():
	Lights.green_on()
	return redirect('/')

@app.route('/amber', methods = ['POST'])	
def amber():
	Lights.yellow_on()
	return redirect('/')

@app.route('/red', methods = ['POST'])
def red():
    Lights.red_on()
    return redirect('/')

@app.route('/off', methods = ['POST'])	
def off():
	Lights.off()
	return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

