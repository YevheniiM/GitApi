from aiohttp import web
from aiohttp.web_response import Response

from app.helpers.serialization import GithubSerializer, GitlabSerializer
from app.helpers.client import GithubClient, GitlabClient
from app.helpers.query_parser import GitlabQueryParser, GithubQueryParser

PLATFORMS = {
    "github": (GithubClient, GithubQueryParser, GithubSerializer),
    "gitlab": (GitlabClient, GitlabQueryParser, GitlabSerializer),
}


def get_error_response(error: str, status: int) -> Response:
    return web.json_response({"error": error}, status=status)


async def search_repositories(request):
    request_query = request.rel_url.query
    try:
        client, parser, serializer = PLATFORMS.get(request_query.get("platform"))
    except TypeError:
        return get_error_response(f"{request_query.get('platform')} platform is not supported", 404)

    try:
        search_query = parser.parse(request_query)
    except KeyError:
        return get_error_response("The request query is incorrect", 404)

    data = await client().search(search_query)

    return web.json_response(serializer().deserialize(data))
