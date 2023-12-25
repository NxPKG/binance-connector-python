import sys
from configparser import ConfigParser

config = ConfigParser()

try:
    config.read('examples/config.ini')

    # Check for the existence of the 'keys' section
    if 'keys' not in config:
        raise ValueError("Missing 'keys' section in examples/config.ini")

    # Check for the presence of 'api_key' and 'api_secret' keys
    if 'api_key' not in config['keys'] or 'api_secret' not in config['keys']:
        raise ValueError("Both 'api_key' and 'api_secret' are required in the 'keys' section")

    # Access the API_KEY and API_SECRET from examples/config.ini
    api_key = config['keys']['api_key']
    api_secret = config['keys']['api_secret']

    # ... Your additional validation logic here ...

    print("Config validation successful")

except Exception as e:
    print(f"Config validation failed: {str(e)}")
    sys.exit(1)
