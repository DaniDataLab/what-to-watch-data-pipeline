import requests
import logging.config
import os 
import traceback

logging_path = os.path.abspath('./src/config/logging.ini')
logging.config.fileConfig(logging_path, disable_existing_loggers=False)
logger = logging.getLogger(__name__)
 
def main():
    pass

def make_request(url:str, headers:dict) -> dict:
    """
    Makes a get request to the specified URL with the given headers.

    Args:
        url (str): The URL to make the request to.
        headers (dict): The headers to include in the request.
    
    Returns:
        Dict: The JSON response as a dictionary.
    """

    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        logging.error("HTTP error ocurred: %s", errh, exc_info=True)
    except requests.exceptions.ConnectionError as errc:
        logging.error("Connection error ocurred: %s", errc, exc_info=True)
    except requests.exceptions.Timeout as errt:
        logging.error("Timeout error: the request took too long to complete: %s", errt, exc_info=True)
    except requests.exceptions.RequestException as err:
        logging.error("An unexpected error ocurred with the request: %s", err, exc_info=True)
    return {}

if __name__ == '__main__':
    main()