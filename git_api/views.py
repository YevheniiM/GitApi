import asyncio

from aiohttp import web

from settings import config
from serialization import GithubSerializer, GitlabSerializer
from helpers.client import GithubClient, GitlabClient
from helpers.query_parser import GitlabQueryParser, GithubQueryParser

PLATFORMS = {
    "github": (GithubClient, GithubQueryParser, GithubSerializer),
    "gitlab": (GitlabClient, GitlabQueryParser, GitlabSerializer),
}


async def search_repositories(request):
    loop = asyncio.get_event_loop()

    request_query = request.rel_url.query
    client, parser, serializer = PLATFORMS.get(request_query.get("platform"))

    search_query = parser.parse(request_query)
    data = await loop.create_task(client(loop).search(search_query))

    return web.json_response(serializer().deserialize(data))
