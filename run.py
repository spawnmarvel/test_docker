# https://realpython.com/python-requests/
import time
import logging
import signal
from app_logs.app_logger import Logger
from app_exceptions.custom_exceptions import CustomShutDownExceptions
logger = Logger().get()


def handler_stop_signals(signum, frame):
    logger.info("Got Signal:" + str(signum)+ " " + str(frame))
    logger.info("The SIGTERM(15) signal is a generic signal used to terminate a program. SIGTERM provides an elegance way to kill program")
    time.sleep(2)
    logger.info("Starting to stop, throw exception to main for clean up")
    raise CustomShutDownExceptions("SIGTERM")

# docker stop sends SIGTERM
signal.signal(signal.SIGTERM, handler_stop_signals) # (SIGTERM): terminate the process in a soft way


if __name__ == "__main__":
    logger.info("Main")
    count = 0
    work = True
    try:
        while work:
            logging.info("loop " + str(count))
            time.sleep(5)
            count += 1
    except CustomShutDownExceptions as ex:
        work = False
        logger.info(ex)
