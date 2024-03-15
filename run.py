from app_page.database import app, db

from app_page.models import *

from app_page.views import *

if __name__ == "__main__":
    with app.app_context():
        db.create_all()    
    app.run(host='0.0.0.0', debug=True)