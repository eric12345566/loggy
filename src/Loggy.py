from src.theme.ClassicTheme import ClassicTheme
from src.LogLevelEnum import LogLevel


class Loggy:
    def __init__(self, module_name=None, theme=ClassicTheme):
        self.__theme = theme()
        self.__module_name = module_name

    def __print_log(self, log_text):
        print(log_text)

    def set_theme(self, loggyTheme):
        self.__theme = loggyTheme()

    def info(self, log, *texts, name=None):
        if name is not None:
            render_log = self.__theme.apply_theme(LogLevel.INFO, log, *texts, name=name)
        else:
            render_log = self.__theme.apply_theme(LogLevel.INFO, log, *texts, name=self.__module_name)

        self.__print_log(render_log)

    def debug(self, log, *texts, name=None):
        if name is not None:
            render_log = self.__theme.apply_theme(LogLevel.DEBUG, log, *texts, name=name)
        else:
            render_log = self.__theme.apply_theme(LogLevel.DEBUG, log, *texts, name=self.__module_name)

        self.__print_log(render_log)

    def warning(self, log, *texts, name=None):
        if name is not None:
            render_log = self.__theme.apply_theme(LogLevel.WARNING, log, *texts, name=name)
        else:
            render_log = self.__theme.apply_theme(LogLevel.WARNING, log, *texts, name=self.__module_name)

        self.__print_log(render_log)

    def error(self, log, *texts, name=None):
        if name is not None:
            render_log = self.__theme.apply_theme(LogLevel.ERROR, log, *texts, name=name)
        else:
            render_log = self.__theme.apply_theme(LogLevel.ERROR, log, *texts, name=self.__module_name)

        self.__print_log(render_log)

    def critical(self, log, *texts, name=None):
        if name is not None:
            render_log = self.__theme.apply_theme(LogLevel.CRITICAL, log, *texts, name=name)
        else:
            render_log = self.__theme.apply_theme(LogLevel.CRITICAL, log, *texts, name=self.__module_name)

        self.__print_log(render_log)


if __name__ == '__main__':
    logger = Loggy("Loggy Test")
    # logger.set_theme(ClassicTheme)
    logger.info("This is the info", " hello", "gopood")
    logger.debug("This is the info")
    logger.warning("This is the info")
    logger.error("This is the info")
    logger.critical("This is the info")
