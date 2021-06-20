import logging
logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)
#logger.trace("Trace Message!");
logger.debug("Debug Message!");
logger.info("Info Message!");
logger.warning("Warn Message!");
logger.error("Error Message!");
logger.fatal("Fatal Message!");