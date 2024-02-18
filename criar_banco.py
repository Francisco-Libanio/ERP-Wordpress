from ERP import database, app
from ERP.models import Usuario, Produto

with app.app_context():
    database.create_all()
