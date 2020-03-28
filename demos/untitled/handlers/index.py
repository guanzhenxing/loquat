import logging

from loquat.handlers.base import BaseHandler

logger = logging.getLogger(__name__)


class IndexHandler(BaseHandler):
    def get(self):
        print(">>>")
        self.render('index.html')
