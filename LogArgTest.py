#!/usr/bin/env python3
print("LogTest.py")

import logging
import argparse

LOG_LEVEL = logging.ERROR #Default logging level; should be ERROR
LOGGER = logging.getLogger(__name__)


def main():
    arg_parser()
    log_setup()
    LOGGER.debug("Debug message")
    LOGGER.info("Info message")
    LOGGER.warning("Warning message")
    LOGGER.error("Error message")
    LOGGER.critical("Critical message")

#Set up Argument Parser
def arg_parser():
    parser = argparse.ArgumentParser(description="A test of logging and argparse")
    parser.add_argument("-a", "--auto", help="Automatically sync previously set courses", action="store_true")
    parser.add_argument("-l", "--log", help="Log output to file", action="store_true")
    parser.add_argument("-v", "--verbose", help="Verbose output", action="store_true")
    parser.add_argument("-d", "--debug", help="debug output", action="store_true")
    args=parser.parse_args()
    return args

def log_setup():
    global LOG_LEVEL
    if arg_parser().debug:
        LOG_LEVEL = logging.DEBUG
    elif arg_parser().verbose:
        LOG_LEVEL = logging.INFO
    LOGGER.setLevel(LOG_LEVEL)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    if arg_parser().log: #Only log to file if log is set
        # create file handler that logs at configured log_level to file 'run.log'
        fh = logging.FileHandler('run.log')
        fh.setLevel(LOG_LEVEL)
        fh.setFormatter(formatter)
        LOGGER.addHandler(fh)
    
    # create console handler for iostream.
    ch = logging.StreamHandler()
    ch.setLevel(LOG_LEVEL)
    ch.setFormatter(formatter)
    

    # create formatter and add it to the handlers
    # Uses time.strftime(format[, t]), see
    # https://docs.python.org/3/library/time.html#time.strftime
    
    if arg_parser().auto:
        LOGGER.info("Auto is set")

    # add the handlers to the logger
    
    LOGGER.addHandler(ch)

    


if __name__ == "__main__":
    main()