import logging

from .config import PROJECT_VERSION, settings


class SkipHealthFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        req = (
            getattr(record, "request_line", "")
            or getattr(record, "raw_path", "")
            or getattr(record, "path", "")
            or getattr(record, "message", "")
        )
        return "/health-check" not in req


log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": (
                "%(asctime)s - %(levelname)s "
                f"- app-version:{PROJECT_VERSION}  %(filename)s:%(lineno)d - %(funcName)s - %(message)s"
            )
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(asctime)s - %(levelname)s - %(client_addr)s - "%(request_line)s" %(status_code)s',
        },
    },
    "filters": {
        "skip_health_check": {
            "()": "core.logging_config.SkipHealthFilter",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": "ext://sys.stdout",
            "level": settings.log_level,
        },
        "access": {
            "class": "logging.StreamHandler",
            "formatter": "access",
            "stream": "ext://sys.stdout",
            "level": "INFO",
            "filters": ["skip_health_check"],
        },
    },
    "loggers": {
        "uvicorn": {"handlers": ["console"], "level": settings.log_level, "propagate": False},
        "uvicorn.error": {"handlers": ["console"], "level": settings.log_level, "propagate": False},
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},
    },
    "root": {
        "handlers": ["console"],
        "level": settings.log_level,
        "propagate": True,
    },
}
