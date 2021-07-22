import abc


class LoggyTheme(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def apply_theme(self, log_level, log, *texts, name=None):
        """
        Theme Designer can customize the beautiful logs in this function, Implementation details on github repo wiki
        for tutorial and api docs.
        :param log_level: enum LogLevel
        :param log: log text
        :param texts: log text list
        :param name: user can change the module_name with temporary this param
        :return: rendered colorful log string
        """
        return NotImplemented

    @abc.abstractmethod
    def theme_name(self, log_level, name):
        """
        Render the module name to the color for output string. Implementation details on github repo wiki for tutorial
        and api docs.
        :param log_level: enum LogLevel
        :param name: log text
        :return: rendered colorful log string
        """
        return NotImplemented

    @abc.abstractmethod
    def theme_log_level(self, log_level):
        """
        Render the log level to the color for output string. Implementation details on github repo wiki for tutorial and
        api docs.
        :param log_level: enum LogLevel
        :return: rendered colorful log level string
        """
        return NotImplemented

    @abc.abstractmethod
    def theme_log(self, log_level, log_text):
        """
        Render the log to the color for output string. Implementation details on github repo wiki for tutorial and api
        docs.
        :param log_level: enum LogLevel
        :param log_text: log text
        :return: rendered colorful log string
        """
        return NotImplemented

    def render_name(self, log_level, name):
        """
        Render the name into colorful text. Normally you won't need to override this function
        :param log_level: log type
        :param name: name of module or user customize name
        :return: rendered name text
        """
        if name is None:
            r_name = ""
        else:
            r_name = self.theme_name(log_level, name)
        return r_name

    def render_log_level(self, log_level):
        """
        Render the log level into colorful string. Normally you won't need to override this function
        :param log_level: LogLevelEnum
        :return: rendered log level string
        """
        return self.theme_log_level(log_level)

    def render_log_text(self, log_level, log_text, *logs):
        """
        Render the log into colorful text. Normally you won't need to override this function
        :param log_level: log type
        :param log_text: log text
        :param logs: logs array
        :return: rendered log text
        """
        r_log = self.theme_log(log_level, log_text)

        for log in logs:
            r_log += self.theme_log(log_level, log)

        return r_log
