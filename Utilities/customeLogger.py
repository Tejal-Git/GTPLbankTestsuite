import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=r"D:\Tejal\software projects\Selenium_Projects\Git\GTPLbankTestsuite\Logs\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S',force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger