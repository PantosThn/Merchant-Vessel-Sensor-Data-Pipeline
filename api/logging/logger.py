import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

host_data_path = os.getenv('HOST_DATA_PATH', 'logs/app.log')

log_file_path = os.path.join(host_data_path, 'api/logs/app.log')

os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

# Ensure the directory for the log file exists
log_directory = os.path.dirname(log_file_path)
os.makedirs(log_directory, exist_ok=True)

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path, mode="a", delay=True),  # Use mode="a" for append
        logging.StreamHandler(stream=None)
    ]
)

# Create a logger
logger = logging.getLogger(__name__)
