from loquat import web

from config import init_handlers, init_app_settings, untitled_logger

handlers = init_handlers()
app_settings = init_app_settings()
app_properties = {
    'log': untitled_logger
}

app_config = web.AppConfig(handlers=handlers, app_settings=app_settings,
                           port=8080, env='DEV', app_name='untitled', app_properties=app_properties)


def main():
    untitled_logger.info('Will run.....')
    web.run(app_config=app_config)


if __name__ == "__main__":
    main()
