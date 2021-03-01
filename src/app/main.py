from aiohttp import web
from aiohttp_swagger import setup_swagger

from src.app.settings import config
from src.app.routes import setup_routes

if __name__ == "__main__":
    app = web.Application()
    setup_routes(app)
    app["config"] = config
    setup_swagger(app,
                  title="Git repositories search API",
                  description="Git repositories search API endpoints")
    web.run_app(app)
