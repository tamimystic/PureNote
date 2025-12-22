from PureNote.logger import logger
from PureNote.custom_exception import InvalidURLException

# logger.info("This is a test log message from test.py")

try:
    raise InvalidURLException("The provided URL is invalid.")
except Exception as e:
    logger.error(f"Caught an exception: {e}")
