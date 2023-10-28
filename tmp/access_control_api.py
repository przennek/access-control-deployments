import subprocess

from flask_cors import CORS
from flask_socketio import SocketIO
from gevent import monkey

from aca.api.controllers.call_control_controllers import call_api_bp
from aca.api.controllers.enrollment_controllers import enrollment_api_bp
from aca.api.controllers.internal_controllers import api_bp
from aca.api.controllers.lock_control_controllers import lock_api_bp
from aca.api.controllers.media_api_controllers import media_api_bp
from aca.api.controllers.status_controllers import status_api_bp

monkey.patch_all()

import logging.handlers
import os

from flask import Flask
from flask_injector import FlaskInjector

from aca.application_context import context

# logging
logging.basicConfig(level=os.environ.get("LOG_LEVEL", "DEBUG"))

# app
app = Flask(__name__, static_folder="static", static_url_path="/static")

# blueprints
app.register_blueprint(api_bp)
app.register_blueprint(media_api_bp)
app.register_blueprint(call_api_bp)
app.register_blueprint(lock_api_bp)
app.register_blueprint(enrollment_api_bp)
app.register_blueprint(status_api_bp)

# Dependency injection
app.config["iocc"] = FlaskInjector(app=app, modules=[context])

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app, resources={r'/*': {'origins': '*'}})

logger = logging.getLogger(__name__)
socketio = SocketIO(app)


@socketio.on('audio_sink')
def handle_audio_sink(audio_data):
    try:
        # logger.info("Connected WEBSOCKET")
        # # Use subprocess to send the received audio data to aplay
        # audio_process = subprocess.Popen(["aplay", "-f", "FLOAT_LE", "-r", "44100"],
        #                                  stdin=subprocess.PIPE)
        # audio_process.stdin.write(audio_data.encode())
        # audio_process.stdin.flush()
        # audio_process.stdin.close()
        # audio_process.wait()
        subprocess.run(["aplay", "/app/aca/StarWars3.wav"])
        return "Audio has been played."
    except Exception as e:
        logger.error("Error playing audio:", str(e))


if __name__ == '__main__':
    socketio.run(app, threaded=True)
    # app.run(threaded=True)
