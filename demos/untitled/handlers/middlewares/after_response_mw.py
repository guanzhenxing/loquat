import logging

from middlewares.base import BaseMiddleware, MiddlewareType

logger = logging.getLogger(__name__)


class AfterResponseMW0(BaseMiddleware):

    def __init__(self, mw_order=0, mw_type=MiddlewareType.AFTER_RESPONSE):
        super().__init__(mw_order, mw_type)

    def should_run(self, handler, *args, **kwargs) -> bool:
        return True

    def run(self, handler, *args, **kwargs):
        logger.info('')
        logger.info('after_response_mw_0')
        logger.info(args)
        logger.info(kwargs)
        logger.info(self)
        logger.info(handler)
        logger.info('end run a middleware...............')


class AfterResponseMW1(BaseMiddleware):

    def __init__(self, mw_order=1, mw_type=MiddlewareType.AFTER_RESPONSE):
        super().__init__(mw_order, mw_type)

    def should_run(self, handler, *args, **kwargs) -> bool:
        return False

    def run(self, handler, *args, **kwargs):
        logger.info('')
        logger.info('after_response_mw_1')
        logger.info(args)
        logger.info(kwargs)
        logger.info(self)
        logger.info(handler)
        logger.info('end run a middleware...............')


class AfterResponseMW2(BaseMiddleware):

    def __init__(self, mw_order=2, mw_type=MiddlewareType.AFTER_RESPONSE):
        super().__init__(mw_order, mw_type)

    def should_run(self, handler, *args, **kwargs) -> bool:
        return True

    def run(self, handler, *args, **kwargs):
        logger.info('')
        logger.info('after_response_mw_2')
        logger.info(args)
        logger.info(kwargs)
        logger.info(self)
        logger.info(handler)
        logger.info('end run a middleware...............')
