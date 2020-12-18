#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Saman Rajaei"
__version__ = "0.1.0"
__license__ = "MIT"

import errno, os, socket, sys, time
from logzero import logger
# from telnetlib import Telnet

""" load in env vars, set sensible defaults for it to need minimal config to run """
# reuqest_timeout = os.getenv('_REQ_TIMEOUT_SECS', 1)
# preferred_host = os.getenv('_PREFERRED_HOST', '1.1.1.1')
# preferred_port = os.getenv('_PREFERRED_PORT', 80)
## preferred_port = int(os.environ['_PREFERRED_PORT'])

reuqest_timeout_secs = 5
preferred_host = '1.1.1.1'
preferred_port = 80
how_frequently_secs = 3

"""
Right, skeleton of the function stolen from this answer: https://stackoverflow.com/a/33117579 and added my own tweaks to it.
I quite liked the thinking behind:

    "... Avoid DNS resolution (we will need an IP that is well-known and guaranteed to be available for most of the time)
     Avoid application layer connections (connecting to an HTTP/FTP/IMAP service)
     Avoid calls to external utilities from Python or other language of choice (we need to come up with a language-agnostic solution that doesn't rely on third-party solutions)"

Function will exit with appropriate code if an issue happens but it won't exit with 0 if all ok, since I'm interested in seeing it carry on in a loop
"""
def is_able_to_connect(host = preferred_host, port = preferred_port, timeout = reuqest_timeout_secs):
    """
    defaults:
        Host: 1.1.1.1 (While above link suggests Google, I personally prefer CloudFlare's free public DNS)
        OpenPort: 80/tcp
        Service: domain (DNS/TCP)
    """
    time.sleep(how_frequently_secs)
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        # socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        logger.info('Was able to create outbound socket, internet ok. \n')

        return True

    except socket.error as so_ex:
        logger.error('socket faced an exception, high level: ' + str(so_ex))

        # got first line from https://stackoverflow.com/questions/5161167/python-handling-specific-error-codes
        # extended it to other potentual causes - cleaner than messing with the string itself IMO
        if so_ex.errno == errno.ECONNREFUSED:
            logger.info('Unlikely that remote host has gone down therefore probably internet connectivity issue, do a ping or a webpage check to ensure. \n')
            sys.exit(errno.ECONNREFUSED)

        elif so_ex.errno == errno.ENETDOWN:
            logger.info('Appears network is down, most likely an outbound connection issue, check whether any traffic leaving the routers/NAT. \n')
            sys.exit(errno.ENETDOWN)

        elif so_ex.errno == errno.ENETUNREACH:
            logger.info('Appears no network path to the host, most likely an internal network issue, check whether the path to the routers/NAT still in place. \n')
            sys.exit(errno.ENETUNREACH)

        elif so_ex.errno == errno.ENOTCONN:
            logger.info('Appears socket is not connected, remote host might have shut down our TCP connection, check whether we can create a new connection with netcat or /dev/tcp/. \n')
            sys.exit(errno.ENOTCONN)

        elif so_ex.errno == errno.ESHUTDOWN:
            logger.info('Appears remote host has shut down our TCP connection, check whether we can create a new connection with netcat or /dev/tcp/. \n')
            sys.exit(errno.ESHUTDOWN)

        elif so_ex.errno == errno.EHOSTDOWN:
            # icmp and telnet are different protocols than TCP so not the most reliable but for variety..
            logger.info('Appears eventhough path to host was found, that the remote host has gone down, check whether we can create a new connection with a ping or telnet. \n')
            sys.exit(errno.EHOSTDOWN)

        elif so_ex.errno == errno.EHOSTUNREACH:
            logger.info('Appears no network path to the host was found, do a traceroute to veirfy. \n')
            sys.exit(errno.EHOSTUNREACH)

        else:
            logger.info('Woah... don\'t know about this one I\'m afraid... \n')
            sys.exit(-1)

    except socket.timeout as to_ex:
        logger.error('socket faced timeout exception: ' + str(to_ex))
        logger.info('Similarly, check whether a new request reaches it. Otherwise no action here really. \n')

    finally:
        # de-allocate the resource
        s.close()

    # following won't really apply here.
    # except socket.herror as he_ex:
    #     logger.warning(he_ex)
    #     return False
    # except socket.gaierror as ga_ex:
    #     logger.warning(ga_ex)
    #     return False


def main():

    logger.info("Starting up...")

    # do forever until an issue happens, in which case it will exit
    while True:
        is_able_to_connect()
        # time.sleep(3)
        """
        You could sleep here but IMO it's cleaner to have inside the function
        stack itself, since like that it will be agnostic to the execution time of the function.
        You could also introduce a scheduler with a lock if you want to get very serious
        something like this: https://docs.python.org/3/library/sched.html
        but this should be good enough for this purpose
        """

if __name__ == "__main__":
    main()
