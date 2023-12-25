import sys
from configparser import ConfigParser

config = ConfigParser()

try:
    config.read('config.ini')

    # Check for the existence of the 'keys' section
    if 'keys' not in config:
        raise ValueError("Missing 'keys' section in config.ini")

    # Check for the presence of 'api_key' and 'api_secret' keys
    if 'api_key' not in config['keys'] or 'api_secret' not in config['keys']:
        raise ValueError("Missing 'api_key' or 'api_secret' in the 'keys' section")

    print("Config validation successful")

except Exception as e:
    print(f"Config validation failed: {str(e)}")
    sys.exit(1)
