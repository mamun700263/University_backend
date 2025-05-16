
# 📝 Logger Setup & Usage Guide

Logging is 🔑 for tracking app behavior, debugging issues, and monitoring production health. This guide covers how to configure and use the new logger setup in our projects.

---

## 🎯 Why Use Custom Loggers?

- Separate logs by app/module to avoid noise.
- Control log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).
- Save logs to files, consoles, or external services.
- Improve debugging and monitoring efficiency.

---

## ⚙️ Configuration Overview

Our logger setup uses Python’s built-in `logging` module and Django’s logging config to:

- Keep Django default logs in the console.
- Direct app-specific logs (e.g., `university`, `payments`) to their own log files.
- Use different handlers and formatters for clarity.

---

## 🛠 How to Configure New Loggers

### 1. Define Logger in `settings.py`

Add or update the `LOGGING` dictionary:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '[{asctime}] {levelname} [{name}] {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname}: {message}',
            'style': '{',
        },
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'university_file': {
            'class': 'logging.FileHandler',
            'filename': 'logs/university.log',
            'formatter': 'verbose',
            'level': 'DEBUG',
        },
        # Add more handlers per app if needed
    },

    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'university': {
            'handlers': ['university_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # Add more app-specific loggers here
    },
}
````

---

### 2. Use Logger in Your App

In your app (e.g., `university`), create and use a logger instance:

```python
import logging

logger = logging.getLogger('university')

def some_function():
    logger.debug('Debug info: function started')
    try:
        # Your logic here
        logger.info('Operation successful')
    except Exception as e:
        logger.error(f'Error occurred: {e}', exc_info=True)
```

---

## 💡 Best Practices

* Use appropriate log levels:

  * `DEBUG` for detailed debugging info.
  * `INFO` for general events.
  * `WARNING` for unexpected issues that are not errors.
  * `ERROR` for serious problems.
  * `CRITICAL` for fatal errors causing program termination.
* Avoid logging sensitive info (passwords, tokens).
* Use `exc_info=True` in error logs to capture traceback.
* Keep log files rotated or archived (consider tools like `logging.handlers.RotatingFileHandler` if needed).
* Don’t spam logs — be purposeful and concise.

---

## 🚀 Quick Start Checklist

* [ ] Update `LOGGING` in `settings.py` with app-specific handlers/loggers.
* [ ] Create log files directory (`logs/`) with proper permissions.
* [ ] Use `logging.getLogger('app_name')` in your app modules.
* [ ] Log meaningful messages with correct log levels.
* [ ] Monitor logs regularly for warnings and errors.

---

## 📚 Additional Resources

* [Python Logging HOWTO](https://docs.python.org/3/howto/logging.html)
* [Django Logging Docs](https://docs.djangoproject.com/en/stable/topics/logging/)
* [Logging Cookbook - RotatingFileHandler](https://docs.python.org/3/howto/logging-cookbook.html#using-rotatingfilehandler)

---

Logging is your frontline for staying on top of bugs and understanding app flow. Get comfy with it, and you’ll save tons of time troubleshooting.

> Got questions? Hit up Mamun anytime.
> Keep logging clean & meaningful! 🚀

```
