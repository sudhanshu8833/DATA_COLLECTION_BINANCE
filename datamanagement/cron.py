
import json
import requests
import pandas as pd
import logging
import traceback
logger = logging.getLogger('dev_log')

def scheduled_job():
    try:
        pass

    except Exception:
        logger.error(str(traceback.format_exc()))
        