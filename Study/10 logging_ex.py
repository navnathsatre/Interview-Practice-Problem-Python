import logging

'''
LEVELS:
debug 10
info  20
warning 30
error 40
critical 50
'''
logging.basicConfig(filename = "output.log",
                     level=logging.DEBUG,
                     format = "%(levelname)s %(asctime)s - %(message)s")
logger = logging.getLogger()
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
