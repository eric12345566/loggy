from .theme.ClassicTheme import ClassicTheme
from .module.LogLevelEnum import LogLevel
import time


class Loggy:
    _theme = ClassicTheme
    _show_log_time = True
    _log_time_struct = "%m/%d %H:%M:%S"

    def __init__(self, module_name=None, theme=None, show_log_time=None, log_time_struct=None):
        if theme is not None:
            self.__theme = theme()
        else:
            self.__theme = Loggy._theme()

        if show_log_time is not None:
            self.__show_log_time = show_log_time
        else:
            self.__show_log_time = Loggy._show_log_time

        self.__module_name = module_name

        if log_time_struct is not None:
            self.__log_time_struct = log_time_struct
        else:
            self.__log_time_struct = Loggy._log_time_struct

    @staticmethod
    def __print_log(log_text):
        print(log_text)

    def set_theme(self, loggyTheme):
        self.__theme = loggyTheme()

    def set_show_log_time(self, log_time):
        self.__show_log_time = log_time

    @classmethod
    def class_set_log_time_struct(cls, time_struct):
        cls._log_time_struct = time_struct

    @classmethod
    def class_get_log_time_struct(cls):
        return cls._log_time_struct

    @classmethod
    def class_set_show_log_time(cls, show_log_time):
        cls._show_log_time = show_log_time

    @classmethod
    def class_get_show_log_time(cls):
        return cls._show_log_time

    @classmethod
    def class_set_theme(cls, theme):
        cls._theme = theme

    @classmethod
    def class_get_theme(cls):
        return cls._theme

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

