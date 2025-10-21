from flask import Flask
from flask import render_template, request, redirect, url_for



app=Flask(__name__)



# Sample data (in-memory list)
tasks = [
    {'title': 'Task 1', 'description': 'Complete Flask tutorial'},
    {'title': 'Task 2', 'description': 'Study for exams'}
]


@app.route('/')
def home():
    return render_template(
        'index.html',tasks=tasks
    )




@app.route('/add', methods=['GET','POST'])
def add_task():
    if request.method=='POST':
        title=request.form['title']
        description=request.form['description']
        tasks.append({'title':title,'description':description})
        return redirect(url_for('home'))
    return render_template('add_task.html')


@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit_task(id):
    if request.method=='POST':
        tasks[id]['title']=request.form['title']
        tasks[id]['description']=request.form['description']
        return redirect(url_for('home'))
    return render_template('edit_task.html', task=tasks[id])



@app.route('/delete/<int:id>')
def delete_task(id):
    tasks.pop(id)
    return redirect(url_for('home'))


if __name__=='__main__':
    print(
        'Everything is working fine...'
    )
    print(__name__)
    app.run(debug=True)
    
    
# RENDER 
# TO CAUSE SOMEONE OR SOMETHING TO BE IN A PARTICULAR STATE


