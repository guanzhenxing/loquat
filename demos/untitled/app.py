import os

from loquat import web
from loquat.utils import utils

from handlers.index import IndexHandler

here = os.path.dirname(os.path.abspath(__file__))


def _init_handlers():
    return [
        (r"/", IndexHandler)
    ]


def _init_app_settings():
    return {
        'debug': True,
        'static_path': utils.abs_path(here, 'static'),
        'template_path': utils.abs_path(here, 'templates')
    }


def main():
    handlers = _init_handlers()
    app_settings = _init_app_settings()
    app_config = web.AppConfig(handlers=handlers, app_settings=app_settings, port=8080, env='DEV', app_name='untitled')
    web.run(app_config=app_config)


if __name__ == "__main__":
    main()
