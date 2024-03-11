from flask import render_template, request
from app import app, db
from app.database.tables import Tasks
from app.forms import Edit_task

"""
    MELHORAR O FORMULARIO
    ADICIONAR, REMOVER OU MELHORAR (ADD, RM, M+):
        ADD: ADICIONAR IMAGEM
        ADD: EDITAR IMAGEM
"""

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = Edit_task(request.form)

    all_tasks = Tasks.query.all()

    if request.method == 'POST' and form.validate():
        current_name = form.current_name.data
        new_name = form.new_name.data

        task = Tasks.query.filter_by(name=current_name).first()

        if task:
            task.name = new_name
            task.priority = form.task_priority.data
            task.description = form.task_description.data

            db.session.commit()
            all_tasks = Tasks.query.all()

            form = Edit_task(request.form)  

            return render_template('edit.html', form=form, all_tasks=all_tasks)

    return render_template('edit.html', form=form, all_tasks=all_tasks)

