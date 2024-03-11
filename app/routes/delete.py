from flask import render_template, request
from app import app, db
from app.database.tables import Tasks
from app.forms import Delete_task

"""
    MELHORAR O FORMULARIO
"""

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    form = Delete_task(request.form)

    all_tasks = Tasks.query.all()

    if request.method == 'POST' and form.validate():
        task_name = form.task_name.data
        confirm_task_name = form.confirm_task_name.data

        if task_name == confirm_task_name:
            task_delete = db.session.query(Tasks).filter_by(name=task_name).first()

            if task_delete:
                db.session.delete(task_delete)
                db.session.commit()

                form = Delete_task()
                all_tasks = Tasks.query.all()
                return render_template('delete.html', form=form, all_tasks=all_tasks)

    return render_template('delete.html', form=form, all_tasks=all_tasks)
