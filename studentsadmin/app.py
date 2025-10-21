
from flask import Flask


app=Flask(__name__)

@app.route('/')
def home():
    pass


@app.route('/create',methods=['GET', 'POST'])
def create_user():
    pass


@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit_user(id):
    pass

@app.route('/delete/<int:id>',methods=['GET','POST'])
def delete_user(id):
    pass

