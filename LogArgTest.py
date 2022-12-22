#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Test +2

import logging
import argparse


def main():
    print("LogTest.py")
    args = arg_parser()
    log_setup(args)

    LOGGER.debug("Debug message")
    LOGGER.info("Info message")
    LOGGER.warning("Warning message")
    LOGGER.error("Error message")
    LOGGER.critical("Critical message")


# Set up Argument Parser
def arg_parser():
    parser = argparse.ArgumentParser(description="A test of logging and argparse")
    parser.add_argument(
        "-a",
        "--auto",
        help="Automatically sync previously set courses",
        action="store_true",
    )
    parser.add_argument("-l", "--log", help="Log output to file", action="store_true")
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        help="Verbosity level: v=error, vv=warning, vvv=info, vvvv=debug (default: critical)",
        default=0,
    )
    args = parser.parse_args()
    return args


# Set up logging functions and set level
def log_setup(args):
    global LOGGER
    LOGGER = logging.getLogger(__name__)
    log_level = [
        logging.CRITICAL,
        logging.ERROR,
        logging.WARNING,
        logging.INFO,
        logging.DEBUG,
    ][args.verbose]
    LOGGER.setLevel(log_level)

    # create formatter and add it to the handlers
    # Uses time.strftime(format[, t]), see
    # https://docs.python.org/3/library/time.html#time.strftime

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    # create console handler for iostream.
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    LOGGER.addHandler(ch)

    if args.log:  # Setup file handler if arg is set
        # create file handler that logs at configured log_level to file 'run.log'
        fh = logging.FileHandler("run.log")
        fh.setLevel(log_level)
        fh.setFormatter(formatter)
        LOGGER.addHandler(fh)

    if args.auto:  # Log if auto is set
        LOGGER.info("Auto is set")


if __name__ == "__main__":
    main()
