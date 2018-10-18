import asyncio
import logging
import time
from datetime import datetime

logger = logging.getLogger(__name__)

handler = logging.StreamHandler()
formater = logging.Formatter('%(asctime)s:%(pathname)s <- %(funcName)s:%(levelname)s... %(message)s')
handler.setFormatter(formater)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

