from loquat import web

from config import init_handlers, init_app_settings, untitled_logger


def main():
    untitled_logger.info('Will run.....')

    handlers = init_handlers()
    app_settings = init_app_settings()
    app_config = web.AppConfig(handlers=handlers, app_settings=app_settings, port=8080, env='DEV', app_name='untitled')
    web.run(app_config=app_config)


if __name__ == "__main__":
    main()
