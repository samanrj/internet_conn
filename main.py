#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Saman Rajaei"
__version__ = "0.1.0"
__license__ = "MIT"

from logzero import logger
import socket

def internet_on():
    try:
        logger.info("checking internet connection..")
        socket.setdefaulttimeout(5)
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        s.close()
        logger.info('internet on.')
        return True

    except Exception as e:
        logger.info(e)
        logger.warning("internet off.")
        return False

def main():
    """ Main entry point of the app """
    logger.info("coming at ya...")
    internet_on()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
