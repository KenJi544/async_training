import requests
from .util.loggin_util import logger


def download_page(url):
    logger.info("downloading the page")
    page = request.get(url)
    logger.debug(f"page status : {page.status_code}")
    if page.status_code == 200:
        logger.info("page downloaded with succes")
    else:
        logger.warning("page didn't downloaded")
