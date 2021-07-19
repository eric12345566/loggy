from theme.ClassicTheme import ClassicTheme
from LogLevelEnum import LogLevel


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
            render_log = self.__theme.apply_theme(LogLevel.INFO, log, texts, name=name)
        else:
            render_log = self.__theme.apply_theme(LogLevel.INFO, log, texts, name=self.__module_name)

        self.__print_log(render_log)


if __name__ == '__main__':
    logger = Loggy("Loggy Test")
    # logger.set_theme(ClassicTheme)
    logger.info("This is the info")
