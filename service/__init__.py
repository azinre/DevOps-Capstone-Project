"""
Service Package
"""
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS


app = Flask(__name__)


# --- Security with Flask-Talisman ---
talisman = Talisman(app)

# --- CORS Policy ---
CORS(app)

# Imports that must occur after app creation
from service import routes  # noqa: F401,E402
from service.common import log_handlers  # noqa: E402

# Initialize logging
log_handlers.init_logging(app, "gunicorn.error")

# Startup logs
app.logger.info(70 * "*")
app.logger.info("  S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")
