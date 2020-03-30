import logging
import os

from loquat.log import initialize_logging
from loquat.web import DeploymentType

from handlers.index import IndexHandler
from handlers.middlewares.after_response_mw import AfterResponseMW0, AfterResponseMW1, AfterResponseMW2
from handlers.middlewares.before_request_mw import BeforeRequestMW0, BeforeRequestMW1, BeforeRequestMW2

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
        (r"/", IndexHandler, dict(database="this is database"))
    ]


def init_app_settings():
    return {
        'debug': True,
        'static_path': abs_path(here, 'static'),
        'template_path': abs_path(here, 'templates')
    }


def init_middlewares():
    return [
        BeforeRequestMW2,
        BeforeRequestMW0,
        BeforeRequestMW1,
        AfterResponseMW0,
        AfterResponseMW2,
        AfterResponseMW1,

    ]
