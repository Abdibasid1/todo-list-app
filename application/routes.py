from application import app, db
from application.models import Task
from application.forms import TaskForm
from flask import render_template, request, redirect, url_for

@app.route("/")
#@app.route("/home")
def home():
    all_tasks = Task.query.all() #will return a list of all tasks
    output = ""
    return render_template("index.html", title="Home", all_tasks=all_tasks)

#    for task in all_tasks:
#        output += task.description +  " - Completed?" + str(task.completed) + "<br>"
#    return output

@app.route("/create", methods=["GET","POST"])
def create():
    form = TaskForm()
    if request.method == "POST": 
        if form.validate_on_submit():
            new_task = Task(description=form.description.data)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("home")) 
    return render_template("add.html", title="Create a Task", form=form)


#    new_todo = Task(description = "New Task")
#    db.session.add(new_todo)
#    db.session.commit()
 #return "New task added"  

@app.route("/complete/<int:id>")
def complete(id):
    task = Task.query.filter_by(id=id).first()
    task.complete = True
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/incomplete/<int:id>")
def incomplete(id):
    task = Task.query.filter_by(id=id).first()
    task.complete = False
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    form = TaskForm()
    task = Task.query.filter_by(id=id).first()
    if request.method == "POST":
        task.description = form.description.data
        db.session.commit()
        return redirect(url_for("home")) 

    return render_template("update.html", form=form, title="Update Task", task=task)
    
@app.route("/delete/<int:id>")
def delete(id):
    task = Task.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home")) 
    






