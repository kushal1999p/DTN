from flask import Flask
from config import Config
from database import db
from flask_cors import CORS

from routes.auth import auth_bp
from routes.citizen import citizen_bp
from routes.voting import voting_bp
from routes.whistleblower import whistle_bp

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(citizen_bp)
app.register_blueprint(voting_bp)
app.register_blueprint(whistle_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
