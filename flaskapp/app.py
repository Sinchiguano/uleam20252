
from flask import Flask
from flask import render_template

name='cesar'

people={'juan':25,
        'juana':35}

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',nameHtml=name)

@app.route('/user')
def userpage():
    return render_template('user.html',data=people)

if __name__=='__main__':
    app.run(debug=True)