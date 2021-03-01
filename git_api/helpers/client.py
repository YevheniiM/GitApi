import aiohttp

from helpers.serialization import GitlabSerializer, GithubSerializer
from settings import config


class GithubClient:
    def __init__(self):
        self.url = "https://api.github.com/search/repositories"

    async def search(self, search_queue):
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.url + search_queue) as resp:
                return GithubSerializer().serialize((await resp.json())["items"])


class GitlabClient:
    def __init__(self):
        self.url = "https://gitlab.com/api/v4/search"
        self.token = config["GITLAB_TOKEN"]

    async def search(self, search_queue):
        headers = {"PRIVATE-TOKEN": self.token}
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.url + search_queue, headers=headers) as resp:
                return GitlabSerializer().serialize(await resp.json())
