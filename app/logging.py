import logging
import os
import structlog
import json
from pygments import highlight, lexers, formatters

ENV = os.getenv("ENV", "dev")

logging.basicConfig(
    format="%(message)s",
    level=logging.INFO,
)

# 👇 Custom renderer for pretty, colored JSON output in console
def pretty_console_json_renderer(_, __, event_dict):
    """Render JSON logs with indentation and colors for console."""
    formatted_json = json.dumps(event_dict, indent=2, ensure_ascii=False)
    colorful_json = highlight(
        formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter()
    )
    return colorful_json.strip()

# 👇 Choose format depending on environment
if ENV == "prod":
    processors = [
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_log_level,
        structlog.processors.JSONRenderer(),  # compact JSON (machine logs)
    ]
else:
    processors = [
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        pretty_console_json_renderer,  # 👈 colorful, indented JSON in console
    ]

structlog.configure(
    processors=processors,
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()
