from abc import abstractmethod

import aiohttp
from aiohttp import ClientSession

from app.helpers.exceptions import ApiError
from app.helpers.serialization import GitlabSerializer, GithubSerializer
from app.settings import config


class GitClient:
    @abstractmethod
    async def search(self, search_queue: str, session: ClientSession):
        pass

    @staticmethod
    def parse_response(response):
        if isinstance(response, list):
            return True

        error_message = response.get("message")
        if error_message:
            raise ApiError(error_message)

        return True


class GithubClient(GitClient):
    def __init__(self):
        self.url = "https://api.github.com/search/repositories"

    async def search(self, search_queue, session):
        async with session.get(url=self.url + search_queue) as resp:
            resp = await resp.json()
            if self.parse_response(resp):
                return GithubSerializer().serialize(resp["items"])


class GitlabClient(GitClient):
    def __init__(self):
        self.url = "https://gitlab.com/api/v4/search"
        self.token = config["GITLAB_TOKEN"]

    async def search(self, search_queue, session):
        headers = {"PRIVATE-TOKEN": self.token}
        async with session.get(url=self.url + search_queue, headers=headers) as resp:
            resp = await resp.json()
            if self.parse_response(resp):
                return GitlabSerializer().serialize(resp)
