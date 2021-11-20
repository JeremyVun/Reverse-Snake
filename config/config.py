# Game Configuration
import json

def get_config():
  with open('config/config.json', 'r') as f:
    return json.load(f)


# Unpack our configurations
config = get_config()