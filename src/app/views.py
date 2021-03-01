import aiohttp
from aiohttp import web
from aiohttp.web_response import Response

from src.app.helpers.client import GithubClientBase, GitlabClientBase
from src.app.helpers.query_parser import GithubQueryParser, GitlabQueryParser
from src.app.helpers.serialization import GithubSerializer, GitlabSerializer

# to add a new supported platform, you just need need to write custom
# Client, QueryParser and Serializer.
# the logic of an app should not be changed.
PLATFORMS = {
    "github": (GithubClientBase, GithubQueryParser, GithubSerializer),
    "gitlab": (GitlabClientBase, GitlabQueryParser, GitlabSerializer),
}


def get_error_response(error: str, status: int) -> Response:
    """
    The function return the json response given the error
    message and the status code.
    """
    return web.json_response({"error": error}, status=status)


async def search_repositories(request):
    """
    ---
    description: This end-point allows to search repositories on different git platforms
    tags:
    - Search repositories
    parameters:
    - in: query
      name: platform
      description: the platform (github and gitlab are supported)
      type: string
    - in: query
      name: name
      description: the name of the repository to search
      type: string
    produces:
    - application/json
    responses:
        "200":
            description: when the query is correct and the response has been returned
        "404":
            description: probably invalid query, check the json error text
    """
    request_query = request.rel_url.query
    try:
        client, parser, serializer = PLATFORMS.get(request_query.get("platform"))
    except TypeError:
        return get_error_response(
            f"{request_query.get('platform')} platform is not supported", 404
        )

    try:
        search_query = parser.parse(request_query)
    except KeyError:
        return get_error_response("The request query is incorrect", 404)

    async with aiohttp.ClientSession() as session:
        data = await client().search(search_query, session)

    return web.json_response(serializer().deserialize(data))
