import abc
from termcolor import colored


class LoggyTheme(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def apply_theme(self, log_type, log, *texts, name=None):
        return NotImplemented

    def render_name(self, log_type, name):
        """
        Render the name into colorful text, normally you won't need to override this function
        :param log_type: log type
        :param name: name of module or user customize name
        :return: rendered name text
        """
        if name is None:
            r_name = ""
        else:
            r_name = self.theme_name(log_type, name)
        return r_name

    def render_log_text(self, log_type, log_text, *logs):
        """
        Render the log into colorful text, normally you won't need to override this function
        :param log_type: log type
        :param log_text: log text
        :param logs: logs array
        :return: rendered log text
        """
        r_log = self.theme_log(log_type, log_text)

        for log in logs:
            r_log += self.theme_log(log_type, log_text)

        return r_log

    @abc.abstractmethod
    def theme_name(self, log_type, name):
        return NotImplemented

    @abc.abstractmethod
    def theme_log(self, log_type, log_text):
        return NotImplemented



