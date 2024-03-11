from flask import render_template
from app import app
from app.database.tables import Tasks

"""
    ADICIONAR, REMOVER OU MELHORAR (ADD, RM, M+)
        ADD: CSS
"""

@app.route("/")
def index():
    all_tasks = Tasks.query.all()
    return render_template('index.html', all_tasks=all_tasks)



