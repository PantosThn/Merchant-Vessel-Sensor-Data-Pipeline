import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the log file path from the environment variable, default to 'logs/app.log'
log_file_path_env = os.getenv('LOG_FILE_PATH', 'logs/app.log')

# Get the directory of the interpreter
interpreter_dir = os.path.dirname(os.path.abspath(__file__))

# Create the log file path based on the interpreter's directory
log_file_path = os.path.join(interpreter_dir, log_file_path_env)

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

# Test log message
logger.info("Logging test message")
