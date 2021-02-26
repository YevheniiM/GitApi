import aiohttp

from serialization import GitlabSerializer, GithubSerializer
from settings import config


class BaseClient:
    def __init__(self, loop):
        self.loop = loop


class GithubClient(BaseClient):
    def __init__(self, loop, token=""):
        super().__init__(loop)
        self.url = "https://api.github.com/search/repositories"

    async def search(self, search_queue):
        async with aiohttp.ClientSession(loop=self.loop) as session:
            async with session.get(url=self.url + search_queue) as resp:
                return GithubSerializer().serialize((await resp.json())["items"])


class GitlabClient(BaseClient):
    def __init__(self, loop):
        super().__init__(loop)
        self.url = "https://gitlab.com/api/v4/search"
        self.token = config["GITLAB_TOKEN"]

    async def search(self, search_queue):
        headers = {"PRIVATE-TOKEN": self.token}
        async with aiohttp.ClientSession(loop=self.loop) as session:
            async with session.get(url=self.url + search_queue, headers=headers) as resp:
                return GitlabSerializer().serialize(await resp.json())
