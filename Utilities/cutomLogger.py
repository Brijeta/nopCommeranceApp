import logging

class LogGen:
    @staticmethod
    def loggen():
        filename ="./Logs/automation.log"
        logging.basicConfig(filename=filename,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filemode='a', force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger