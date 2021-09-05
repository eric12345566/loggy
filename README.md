# Loggy - Convenient, friendly and clean logger for Python

<p align="center">
  <img src="https://raw.githubusercontent.com/eric12345566/loggy/master/img/Logo-v1.png" alt="Loggy Logo" width="300"/>
</p>

![PyPI](https://img.shields.io/pypi/v/LoggyLogger?style=for-the-badge)
![License MIT](https://img.shields.io/github/license/eric12345566/loggy?style=for-the-badge)
![python version](https://img.shields.io/github/pipenv/locked/python-version/eric12345566/loggy?style=for-the-badge)
[![codacy grade](https://img.shields.io/codacy/grade/729be4751aaa4a48922ade27d1a2855b?style=for-the-badge)](https://app.codacy.com/gh/eric12345566/loggy/commits)
[![DeepSource](https://deepsource.io/gh/eric12345566/loggy.svg/?label=resolved+issues&show_trend=true)](https://deepsource.io/gh/eric12345566/loggy/?ref=repository-badge)

Sometimes, you need a logger for your program for a better coding experience.
Something like multiple type of logging(debug, info, warning, or you can define your type), better with different colors. Maybe more,
have some theme for the cute log. Right now, Loggy can be your second choice.

## Install

Right now, we are still in early dev. version. We don't recommend using it in serious project.

If you really have interest to test it, please clone it with git and run our test py file for demo.
You can also import the Loggy Class to new the logger object into your other python code
(See Wiki file for more info).

In the future, we will upload Loggy to pip so everyone can install in one command. 

```shell
pip install LoggyLogger
```

## Quick Usage

First, lets born a Loggy object.

```python
from Loggy import Loggy

loggy = Loggy("main.py") # The string is the module name what you log from
```

That's it! Now you can use let loggy to print the colorful and beautiful log at the console.

We have 5 logging level in Loggy. Different logging level have the different color in the default logging theme.

```python
loggy.info("This is info log")
loggy.debug("This is debug log")
loggy.warning("This is warning log")
loggy.error("This is error log")
loggy.critical("This is critical log")
```

If you want to make your own Loggy logging theme. You can implement the abstract class "LoggyTheme". You can check out our Wiki tutorial (its building right now..... coming soon!).

## TODO Features

-   Multiple logging type: default we have "debug", "info", "warning" and "error". User can define their new type of logging for more use case.
-   Different type, different color: multiple colors for multiple logging type
-   Customize Logging format is easy: using easy structure to define format
-   Theme System: you can customize theme for your logger, Highly customized
-   Log into logfile: all your log will log into the file, in the feature, you can easily connect to online monitor with our APIs

## Contributor

If you want to contribute this project, please contact me with Email. We can talk about how to play the game.

## Source

Logo: Icon made by [Freepik](https://www.flaticon.com/authors/freepik) from [www.flaticon.com](www.flaticon.com)
