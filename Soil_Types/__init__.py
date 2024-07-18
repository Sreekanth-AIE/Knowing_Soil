import os
import sys
import logging

# creating logging config
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# creating log directory 
log_dir = "logs"
log_filepath = os.path.join(log_dir,"dev_logs.log")
os.makedirs(log_dir, exist_ok=True)

# initializing logging function
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        # log into log-file
        logging.FileHandler(log_filepath),

        # printing or logging into the stdout
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("soil_types_logger")

