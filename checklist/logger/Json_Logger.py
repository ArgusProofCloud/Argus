from distutils.sysconfig import customize_compiler
import json
import sys
import json_logging
import logging

class CustomLogging(json_logging.JSONLogFormatter):
    """
    Class to customise json logging
    """
    def format(self, record):
        """"
        all the properties displayed when logging
        """
        json_customized_log_object = ({
            "level": record.levelname,
            "logfile": record.name,
            "message": record.msg,
            "timestamp": record.created     #in UNIX time
        })
        return json.dumps(json_customized_log_object)

    def getLogger(self, name, level):
        """"
        return logger
        """
        json_logging.init_non_web(custom_formatter= CustomLogging, enable_json = True)
        logger = logging.getLogger(name)
        logger.setLevel(logging.level)
        logger.addHandler(logging.StreamHandler(sys.stdout))

        return logger


logger = CustomLogging.getLogger("test", "DEBUG")

logger.info("help")
