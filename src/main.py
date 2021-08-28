# flask imports
from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

# Gpio imports
from RPi.GPIO import cleanup

# custom imports
from controllers.door_motor import close_door
from routes.door_api import DoorApi
from config.env import get_env

# server
app = Flask(__name__)
CORS(app)
api = Api(app)

# cerrando la puerta al inicio
close_door()

api.add_resource(DoorApi, '/door', '/door/<string:state>' )

if __name__ == '__main__':
  try:
    if (get_env() == 'production'):
      app.run(host='0.0.0.0', port=3000, debug=False, use_reloader=False)
    else:
      app.run(host='0.0.0.0', port=3000, debug=True, use_reloader=True)
  except KeyboardInterrupt:
    cleanup()
