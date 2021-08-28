# flask imports
from flask_restful import Resource

# logger imports
from logzero import logger

# custom imports
from controllers.door_motor import open_door, close_door
from utils.constants import OPEN_STATE, CLOSE_STATE


class DoorApi(Resource):
  def put(self, state):
    if (state == OPEN_STATE):
      logger.info("open the door")
      open_door()
      return 'puerta abierta'

    elif (state == CLOSE_STATE):
      logger.info("close the door")
      close_door()
      return 'puerta cerrada'
    else:
      logger.error("parameter not valid: " + state)
      return 'param no valid'