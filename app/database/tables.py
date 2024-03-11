from app import db

"""
    ADICIONAR, REMOVER OU MELHORAR:
        + image (str, opcional, padrão=None): Caminho da imagem relacionada à tarefa.
        + created_at (str): Data de criação da tarefa (formato a ser definido).
        + status (str): Status da tarefa (Concluida, não concluida e etc)
"""

class Tasks(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120))
    priority = db.Column(db.String(24))
    description = db.Column(db.String(255))
    image = db.Column(db.String(255))

    def __init__(self, name, priority=None, description=None, image=None):
        self.name = name
        self.priority = priority
        self.description = description
        self.image = image

    def __repr__(self):
        return "<tasks %r>" % self.name
