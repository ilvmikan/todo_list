from flask import render_template, request
from app import app, db
from app.database.tables import Tasks
from app.forms import Create_task

"""
    MELHORAR O FORMULARIO

    ADICIONAR, REMOVER OU MELHORAR (ADD, RM, M+):
        ADD: CRIAR COM A OPÇÃO DE ESCOLHER IMAGEM
        ADD: CREATED_AT (HORA DE CRIAÇÃO
"""

@app.route("/create", methods=['GET', 'POST'])
def create():
    form = Create_task(request.form)

    all_tasks = Tasks.query.all()

    if request.method == 'POST' and form.validate():
        task = Tasks(
            form.task_name.data,
            form.task_priority.data,
            form.task_description.data
        )

        db.session.add(task)
        db.session.commit()

        form = Create_task()
        all_tasks = Tasks.query.all()
        return render_template('create.html', form=form, all_tasks=all_tasks)

    return render_template('create.html', form=form, all_tasks=all_tasks)
