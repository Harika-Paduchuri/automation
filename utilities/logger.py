import logging

def get_logger():
    logger = logging.getLogger("framework_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        console = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger