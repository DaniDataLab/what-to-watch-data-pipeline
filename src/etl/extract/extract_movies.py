from dotenv import load_dotenv 
import requests
import logging.config
import os 
from sqlalchemy import create_engine, Engine
from sqlalchemy.exc import SQLAlchemyError

load_dotenv()

logging_path = os.path.abspath('./src/config/logging.ini')
logging.config.fileConfig(logging_path, disable_existing_loggers=False)
logger = logging.getLogger(__name__)
 
def main():
    pass

def create_db_connection(
        db_server:str,
        db_name:str,
        db_username:str,
        db_password:str
    ) -> Engine: 
    """
    Creates a connection to a PostgreSQL database.

    Args:
        db_server (str): The server address of the PostgreSQL database.
        db_name (str): The name of the database to connect to.
        db_username (str): The username for authentication.
        db_password (str): The password for authentication.

    Returns:
        Engine: The SQLAlchemy engine object if the connection is successful, 
                 or None if the connection fails.
    """
    connection_string = f"postgresql+psycopg2://{db_username}:{db_password}@{db_server}/{db_name}"
    try:
        engine = create_engine(connection_string)
        connection = engine.connect()
        logging.info("Connection successful to: %s", db_server)
        connection.close()
        return engine 
    except SQLAlchemyError as err:
        logging.error("SQLAlchemy error ocurred: %s. Server name: %s", err, exc_info=True)
    except Exception as e:
        logging.error("An unexpected error occurred during connection: %s", e, exc_info=True)
    return None 
    
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
    except requests.exceptions.Timeout as errt:
        logging.error("Timeout error: the request took too long to complete: %s", errt, exc_info=True)
    except requests.exceptions.RequestException as err:
        logging.error("An unexpected error ocurred with the request: %s", err, exc_info=True)
    return {} 

if __name__ == '__main__':
    main()