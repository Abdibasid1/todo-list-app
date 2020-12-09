from application import app, db
from application.models import Task
from flask import render_template

@app.route("/")
#@app.route("/home")
def home():
    all_tasks = Task.query.all() #will return a list of all tasks
    output = ""
    return render_template("index.html", title="Home", all_tasks=all_tasks)

#    for task in all_tasks:
#        output += task.description +  " - Completed?" + str(task.completed) + "<br>"
#    return output

@app.route("/create")
def create():
    new_todo = Task(description = "New Task")
    db.session.add(new_todo)
    db.session.commit()
    return "New task added"

@app.route("/complete/<int:id>")
def complete(id):
    task = Task.query.filter_by(id=id).first()
    task.complete = True
    db.session.commit()
    return f"Task {id} is now completed"

@app.route("/incomplete/<int:id>")
def incomplete(id):
    task = Task.query.filter_by(id=id).first()
    task.complete = False
    db.session.commit()
    return f"Task {id} is now incompleted"

@app.route("/update/<new_description>")
def update(new_description):
    task = Task.query.order_by(Task.id.desc()).first()
    task.description = new_description
    db.session.commit()
    return f"Most recent task was updated with the description: {new_description}"

@app.route("/delete/<int:id>")
def delete(id):
    task = Task.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return f"Task {id} was deleted"






