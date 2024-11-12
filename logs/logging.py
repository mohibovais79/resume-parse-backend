import logging
import os
from logging.handlers import TimedRotatingFileHandler


# Define a function to configure the logger
def setup_logger(name: str):
    """Sets up a logger for the given name."""
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Set logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

    # Create console handler with a higher log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a file handler that logs messages to a file
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)  # Ensure the logs directory exists
    file_handler = TimedRotatingFileHandler(
        os.path.join(log_dir, f"{name}.log"),
        when="midnight",
        interval=1,
        backupCount=7,  # Keep logs for 7 days
    )
    file_handler.setLevel(logging.DEBUG)

    # Create a logging format
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
