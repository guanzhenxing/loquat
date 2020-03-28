import logging
import os

from loquat.log import initialize_logging
from loquat.web import DeploymentType

from handlers.index import IndexHandler

here = os.path.dirname(os.path.abspath(__file__))
abs_path = lambda root, *a: os.path.join(root, *a)

ENV = 'SOLO'

# 配置logging
initialize_logging(options={
    'log_file_path': '/Users/Jesen/Workspace/mine/my-pyfuse/loquat_log.log',
    'logging_level': 'INFO',
    'log_to_stream': True if ENV == DeploymentType.SOLO else False
})

untitled_logger = logging.getLogger('untitled')


def init_handlers():
    return [
        (r"/", IndexHandler)
    ]


def init_app_settings():
    return {
        'debug': True,
        'static_path': abs_path(here, 'static'),
        'template_path': abs_path(here, 'templates')
    }
