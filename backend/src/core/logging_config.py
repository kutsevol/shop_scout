from .config import PROJECT_VERSION, settings

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": (
                f"%(asctime)s - %(levelname)s "
                f"- app-version:{PROJECT_VERSION}  %(filename)s:%(lineno)d - %(funcName)s - %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": "ext://sys.stdout",
            "level": settings.log_level,
        }
    },
    "loggers": {
        "uvicorn": {
            "handlers": ["console"],
            "level": settings.log_level,
            "propagate": False,
        },
        "uvicorn.error": {
            "handlers": ["console"],
            "level": settings.log_level,
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["console"],
            "level": settings.log_level,
            "propagate": False,
        },
    },
    "root": {
        "handlers": ["console"],
        "level": settings.log_level,
        "propagate": True,
    },
}
