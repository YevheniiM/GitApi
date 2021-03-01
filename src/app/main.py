from aiohttp import web

from src.app.settings import config
from src.app.routes import setup_routes

if __name__ == "__main__":
    app = web.Application()
    setup_routes(app)
    app["config"] = config
    web.run_app(app)
