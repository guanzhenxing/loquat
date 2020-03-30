import logging

from middlewares.base import BaseMiddleware, MiddlewareType

logger = logging.getLogger(__name__)


class BeforeRequestMW0(BaseMiddleware):

    def __init__(self, mw_order=0, mw_type=MiddlewareType.BEFORE_REQUEST):
        super().__init__(mw_order, mw_type)

    def should_run(self, handler, *args, **kwargs) -> bool:
        return False

    def run(self, handler, *args, **kwargs):
        logger.info('')
        logger.info('before_request_mw_0')
        logger.info(args)
        logger.info(kwargs)
        logger.info(self)
        logger.info(handler)
        logger.info('end run a middleware...............')


class BeforeRequestMW1(BaseMiddleware):

    def __init__(self, mw_order=1, mw_type=MiddlewareType.BEFORE_REQUEST):
        super().__init__(mw_order, mw_type)

    def should_run(self, handler, *args, **kwargs) -> bool:
        return True

    def run(self, handler, *args, **kwargs):
        logger.info('')
        logger.info('before_request_mw_1')
        logger.info(args)
        logger.info(kwargs)
        logger.info(self)
        logger.info(handler)
        logger.info('end run a middleware...............')


class BeforeRequestMW2(BaseMiddleware):

    def __init__(self, mw_order=2, mw_type=MiddlewareType.BEFORE_REQUEST):
        super().__init__(mw_order, mw_type)

    def should_run(self, handler, *args, **kwargs) -> bool:
        return True

    def run(self, handler, *args, **kwargs):
        logger.info('')
        logger.info('before_request_mw_2')
        logger.info(args)
        logger.info(kwargs)
        logger.info(self)
        logger.info(handler)
        logger.info('end run a middleware...............')
