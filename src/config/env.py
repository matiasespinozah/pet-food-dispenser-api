from os import environ

def get_env():
  try:
    return environ.get('ENV')
  except:
    return 'develop'
