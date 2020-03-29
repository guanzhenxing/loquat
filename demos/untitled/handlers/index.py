import logging

from loquat.handlers.base import BaseHandler


# logger = logging.getLogger(__name__)


class IndexHandler(BaseHandler):
    def get(self):
        self.application.log.info('>>>>>>>>>>>')
        self.render('index.html')
