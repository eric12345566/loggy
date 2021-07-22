from termcolor import colored
from src.LoggyTheme import LoggyTheme
from src.LogLevelEnum import LogLevel


class ClassicTheme(LoggyTheme):

    def apply_theme(self, log_level, log, *texts, name=None):
        render_log = ""
        render_log += self.render_name(log_level, name)
        if name is not None:
            render_log += colored(" ", color="green")
        render_log += self.render_log_text(log_level, log, *texts)

        return render_log

    def theme_name(self, log_level, name):
        render_name = ""
        if log_level == LogLevel.INFO:
            render_name = colored(" " + name + " ", color="green", attrs=['reverse', 'blink', 'bold'])
        elif log_level == LogLevel.DEBUG:
            render_name = colored(" " + name + " ", color="blue", attrs=['reverse', 'blink', 'bold'])
        elif log_level == LogLevel.WARNING:
            render_name = colored(" " + name + " ", color="yellow", attrs=['reverse', 'blink', 'bold'])
        elif log_level == LogLevel.ERROR:
            render_name = colored(" " + name + " ", color="red", attrs=['reverse', 'blink', 'bold'])
        elif log_level == LogLevel.CRITICAL:
            render_name = colored(" " + name + " ", color="magenta", attrs=['reverse', 'blink', 'bold'])

        return render_name

    def theme_log(self, log_level, log_text):
        render_log = ""
        if log_level is LogLevel.INFO:
            render_log = colored(log_text, color="green")
        elif log_level is LogLevel.DEBUG:
            render_log = colored(log_text, color="blue")
        elif log_level is LogLevel.WARNING:
            render_log = colored(log_text, color="yellow", attrs=['bold'])
        elif log_level is LogLevel.ERROR:
            render_log = colored(log_text, color="red", attrs=['bold'])
        elif log_level is LogLevel.CRITICAL:
            render_log = colored(log_text, color="magenta", attrs=['bold'])

        return render_log
