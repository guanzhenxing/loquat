from loquat.handlers.base import BaseHandler


class IndexHandler(BaseHandler):

    def initialize(self, database):
        self.database = database

    def get(self):
        self.application.log.info('>>>>>>>>>>>')
        self.application.log.info(self)
        self.application.log.info('>>>>>>>>>>>')
        self.write("<<<<")
