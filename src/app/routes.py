from .views import search_repositories


def setup_routes(app):
    app.router.add_get("/api/search/", search_repositories)
