import logging
import sys

logging.getLogger(__name__).addHandler(logging.NullHandler())

logging.debug("fix the path")
sys.path.insert(0, "logging_playground")
