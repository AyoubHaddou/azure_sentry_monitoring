from flask import Flask
from flask_login import LoginManager
import os
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
    app.config["WTF_CSRF_SECRET_KEY"] = os.getenv('WTF_CSRF_SECRET_KEY')
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from .routes import main
    app.register_blueprint(main)
    
    from .models import Users, db, init_db
    db.init_app(app)
    
    login_manager = LoginManager(app)
    login_manager.login_view = "login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))
    
    if os.path.isfile("App/database.db"):
        pass
    else:
        app.app_context().push()
        init_db()
        
    # Initialisation des rapports sur Sentry 
    sentry_sdk.init(
        dsn="https://b4f842a1561b40d9aa2056e45dddb116@o1297886.ingest.sentry.io/6527343",
        integrations=[FlaskIntegration()],
        traces_sample_rate=1.0)
    
    return app 