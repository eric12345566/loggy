from src.theme.ClassicTheme import ClassicTheme
from src.module.LogLevelEnum import LogLevel
import time


class Loggy:
    def __init__(self, module_name=None, theme=ClassicTheme, show_log_time=False):
        self.__theme = theme()
        self.__module_name = module_name
        self.__show_log_time = show_log_time
        self.__log_time_struct = "%m/%d %H:%M:%S"

    @staticmethod
    def __print_log(log_text):
        print(log_text)

    def set_theme(self, loggyTheme):
        self.__theme = loggyTheme()

    def set_log_time(self, log_time):
        self.__show_log_time = log_time

    def set_log_time_struct(self, time_struct):
        self.__log_time_struct = time_struct

    def info(self, log, *texts, name=None):
        log_time = time.localtime()
        log_time_string = time.strftime(self.__log_time_struct, log_time)
        
        if name is not None:
            render_log = self.__theme.apply_theme(LogLevel.INFO, log, *texts, name=name
                                                  , show_log_time=self.__show_log_time, log_time_string=log_time_string)
        else:
            render_log = self.__theme.apply_theme(LogLevel.INFO, log, *texts, name=self.__module_name
                                                  , show_log_time=self.__show_log_time, log_time_string=log_time_string)

        self.__print_log(render_log)

    def debug(self, log, *texts, name=None):
        log_time = time.localtime()
        log_time_string = time.strftime(self.__log_time_struct, log_time)

        if name is not None:
            render_log = self.__theme.apply_theme(LogLevel.DEBUG, log, *texts, name=name
                                                  , show_log_time=self.__show_log_time, log_time_string=log_time_string)
        else:
            render_log = self.__theme.apply_theme(LogLevel.DEBUG, log, *texts, name=self.__module_name
                                                  , show_log_time=self.__show_log_time, log_time_string=log_time_string)

        self.__print_log(render_log)

    def warning(self, log, *texts, name=None):
        log_time = time.localtime()
        log_time_string = time.strftime(self.__log_time_struct, log_time)

        if name is not None:
            render_log = self.__theme.apply_theme(LogLevel.WARNING, log, *texts, name=name
                                                  , show_log_time=self.__show_log_time, log_time_string=log_time_string)
        else:
            render_log = self.__theme.apply_theme(LogLevel.WARNING, log, *texts, name=self.__module_name
                                                  , show_log_time=self.__show_log_time, log_time_string=log_time_string)

        self.__print_log(render_log)

    def error(self, log, *texts, name=None):
        log_time = time.localtime()
        log_time_string = time.strftime(self.__log_time_struct, log_time)

        if name is not None:
            render_log = self.__theme.apply_theme(LogLevel.ERROR, log, *texts, name=name
                                                  , show_log_time=self.__show_log_time, log_time_string=log_time_string)
        else:
            render_log = self.__theme.apply_theme(LogLevel.ERROR, log, *texts, name=self.__module_name
                                                  , show_log_time=self.__show_log_time, log_time_string=log_time_string)

        self.__print_log(render_log)

    def critical(self, log, *texts, name=None):
        log_time = time.localtime()
        log_time_string = time.strftime(self.__log_time_struct, log_time)

        if name is not None:
            render_log = self.__theme.apply_theme(LogLevel.CRITICAL, log, *texts, name=name
                                                  , show_log_time=self.__show_log_time, log_time_string=log_time_string)
        else:
            render_log = self.__theme.apply_theme(LogLevel.CRITICAL, log, *texts, name=self.__module_name
                                                  , show_log_time=self.__show_log_time, log_time_string=log_time_string)

        self.__print_log(render_log)


if __name__ == '__main__':
    logger = Loggy("Loggy Test", show_log_time=True)
    # logger.set_theme(ClassicTheme)
    logger.info("This is the info", " hello")
    logger.debug("This is the info")
    logger.warning("This is the info")
    logger.error("This is the info")
    logger.critical("This is the info")
