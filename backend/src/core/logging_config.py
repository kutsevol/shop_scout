from .config import PROJECT_VERSION, settings

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": (
                f"%(asctime)s - %(levelname)s "
                f"- app-version:{PROJECT_VERSION}  %(filename)s:%(lineno)d - %(funcName)s - %(message)s"
            )
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": "ext://sys.stdout",
            "level": settings.log_level,
        }
    },
    "root": {
        "handlers": ["console"],
        "level": settings.log_level,
        "propagate": True,
    },
}
