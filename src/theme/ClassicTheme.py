from termcolor import colored, cprint
from src.LoggyTheme import LoggyTheme


class ClassicTheme(LoggyTheme):

    def apply_theme(self, log_type, log, *texts, name=None):
        render_log = ""
        render_log += self.render_name(log_type, name)
        if name is not None:
            render_log += colored(" ", color="green")
        render_log += self.render_log_text(log_type, log, texts)

        return render_log

    def theme_name(self, log_type, name):
        return colored(" " + name + " ", color="green", attrs=['reverse', 'blink', 'bold'])

    def theme_log(self, log_type, log_text):
        return colored(log_text, color="green")
