import os
import logging
import sys

LOG_FORMAT = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"

log_dir = "./logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("PureNote")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(LOG_FORMAT)

file_handler = logging.FileHandler(log_filepath)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
