from ERP import database, app
from ERP.models import Usuario, Foto, Produto

with app.app_context():
    database.create_all()
