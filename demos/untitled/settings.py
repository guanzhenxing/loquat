# Make filepaths relative to settings.
import json
import os

from tornado.options import options, define
from loquat.utils import utils
from loquat.settings import DeploymentType

from environment import init_environment
from handlers.index import IndexHandler

define("config_file", default=None, help="filename for additional configuration")
options.parse_command_line()

init_environment()  # 初始化环境参数

here = os.path.dirname(os.path.abspath(__file__))
pardir = os.path.abspath(os.path.join(here, os.path.pardir))


def _init_config():
    """
    init config
    :return: config
    """
    config_file = utils.abs_path(here, 'conf/application.json')
    if options.config_file:
        config_file = options.config_file
    with open(config_file) as f:
        _config = json.load(f)
    return _config


custom_config = _init_config()


def _init_handlers():
    return [
        (r"/", IndexHandler)
    ]


def _init_app_settings():
    return {
        'debug': True if custom_config['env'] in [DeploymentType.PROD, DeploymentType.UAT] else False,
        'static_path': utils.abs_path(here, 'static'),
        'template_path': utils.abs_path(here, 'templates')
    }


default_config = {
    'port': 8080,
    'handlers': _init_handlers(),
    'app_settings': _init_app_settings()
}

config = {**default_config, **custom_config}
