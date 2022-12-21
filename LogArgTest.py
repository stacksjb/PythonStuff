#!/usr/bin/env python3
print("LogTest.py")

import logging
import argparse

def main():
    args = arg_parser()
    log_setup(args)
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
    parser.add_argument('-v', '--verbose', action="count", help="Verbosity level: v=error, vv=warning, vvv=info, vvvv=debug, vvvvv=trace (default: error)", default=0)
    args=parser.parse_args()
    return args

#Set up logging functions and set level
def log_setup(args):
    global LOGGER
    LOGGER = logging.getLogger(__name__)
    log_level = [logging.CRITICAL, logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG][args.verbose]
    LOGGER.setLevel(log_level)
    # if args.verbose == 3:
    #     LOG_LEVEL = logging.DEBUG
    # elif args.verbose == 2:
    #     LOG_LEVEL = logging.INFO
    # elif args.verbose == 1:
    #     LOG_LEVEL = logging.WARNING
    # elif args.verbose == 0:
    #     LOG_LEVEL = logging.ERROR
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    if args.log: #Only log to file if log is set
        # create file handler that logs at configured log_level to file 'run.log'
        fh = logging.FileHandler('run.log')
        fh.setLevel(log_level)
        fh.setFormatter(formatter)
        LOGGER.addHandler(fh)

    # create console handler for iostream.
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    ch.setFormatter(formatter)
    
    # create formatter and add it to the handlers
    # Uses time.strftime(format[, t]), see
    # https://docs.python.org/3/library/time.html#time.strftime
    
    if args.auto:
        LOGGER.info("Auto is set")
    # add the handlers to the logger
    LOGGER.addHandler(ch)

    


if __name__ == "__main__":
    main()