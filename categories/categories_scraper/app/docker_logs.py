import logging

def get_logger(mod_name):
    logger = logging.getLogger(mod_name)
    logger.propagate = False
    # If this attribute evaluates to true, events logged to this logger
    # will be passed to the handlers of higher level (ancestor) loggers
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger