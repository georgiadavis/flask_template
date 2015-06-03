import os # to access ports
from flask import Flask #importing flask
from flask import render_template
from flask import request
from other_file import otherFileFunction #file 

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['POST']) #Recieves request from the browser and renders result.html in template folder
def handle_input():
  form1 = request.form['noun1']
  form2 = request.form['activity']
  form3 = request.form['teacher']
  form4 = request.form['celebrity']
  form5 = request.form['show']
  return render_template('results.html', noun1=form1, activity=form2, teacher=form3, celebrity=form4, show=form5)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 3000)),debug=True)
