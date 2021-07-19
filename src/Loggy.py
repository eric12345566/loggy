from termcolor import colored, cprint
from src.theme.ClassicTheme import ClassicTheme


class Loggy:
    def __init__(self, module_name=None, theme=None):
        self.__theme = theme
        self.__module_name = module_name

    def __printLog(self, log_text):
        print(log_text)

    def set_theme(self, loggyTheme):
        self.__theme = loggyTheme()

    # def info(self, log, *texts, name=None):
    #     if name is None:
    #         log_text = colored(" " + __name__ + " ", color="green", attrs=['reverse', 'blink', 'bold'])
    #     else:
    #         log_text = colored(name, color="green", attrs=['reverse', 'blink', 'bold'])
    #     log_text += colored(" ", color="green")
    #     log_text += colored(log, color="green")
    #     for text in texts:
    #         log_text += colored(text, color="green")
    #     self.__printLog(log_text)

    def info(self, log, *texts, name=None):
        if name is not None:
            render_log = self.__theme.apply_theme("info", log, texts, name=name)
        else:
            render_log = self.__theme.apply_theme("info", log, texts, name=self.__module_name)

        self.__printLog(render_log)


if __name__ == '__main__':
    logger = Loggy("Loggy Test")
    logger.set_theme(ClassicTheme)
    logger.info_theme("This is the info")