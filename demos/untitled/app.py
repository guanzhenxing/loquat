import logging

import loquat
from loquat import web

from settings import config

logger = logging.getLogger(__name__)


class UntitledApplication(loquat.web.Application):

    def __init__(self):
        handlers = config['handlers']
        port = config['port']
        app_settings = config['app_settings']

        super().__init__(port=port, handlers=handlers, **app_settings)


def main():
    app = UntitledApplication()
    web.run(application=app)


if __name__ == "__main__":
    main()
