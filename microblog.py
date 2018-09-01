from app import app
from app.models import Post, User, db


@app.shell_context_processor
def make_shell():
    return {'db': db, 'User': User, 'Post': Post}
