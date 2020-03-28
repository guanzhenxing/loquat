# Loquat

A simple web framework based on Tornado.

## Introduce

Loquat is a web framework based on Tornado.

## Installation

```shell
pip install loquat
```

## Simple uses

```python
import loquat
from loquat import web
from loquat.handlers.base import BaseHandler
from loquat.utils import utils

class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html')

def _init_handlers():
    return [
        (r"/", IndexHandler)
    ]

def _init_app_settings():
    return {
        'debug': True
    }

def main():
    handlers = _init_handlers()
    app_settings = _init_app_settings()
    app_config = web.AppConfig(handlers=handlers, app_settings=app_settings, port=8080, env='DEV', app_name='untitled')
    web.run(app_config=app_config)

if __name__ == "__main__":
    main()

```