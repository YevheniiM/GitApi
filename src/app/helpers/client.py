from abc import abstractmethod
from typing import List

from aiohttp import ClientSession

from src.app.helpers.exceptions import ApiError
from src.app.helpers.serialization import GithubSerializer, GitlabSerializer
from src.app.models import Repository
from src.app.settings import config


class GitClientBase:
    """The base class for GitClients."""

    @abstractmethod
    async def search(self, search_queue: str, session: ClientSession):
        """
        Override this method to define you own behaviour of how the
        search should be performed.
        """
        pass

    @staticmethod
    def check_response(response: [list, dict]) -> bool:
        """Checks if response has the error messages. If so, raises an error."""
        if isinstance(response, list):
            return True

        error_message = response.get("message")
        if error_message:
            raise ApiError(error_message)

        return True


class GithubClient(GitClientBase):
    """The client class for Github integration."""

    def __init__(self):
        self.url = "https://api.github.com/search/repositories"

    async def search(self, search_queue: str, session: ClientSession) -> List[Repository]:
        """Perform search with the search_queue in Github platform."""
        async with session.get(url=self.url + search_queue) as resp:
            resp = await resp.json()
            if self.check_response(resp):
                return GithubSerializer().serialize(resp["items"])


class GitlabClient(GitClientBase):
    """The client class for Gitlab integration."""

    def __init__(self):
        self.url = "https://gitlab.com/api/v4/search"
        self.token = config["GITLAB_TOKEN"]

    async def search(self, search_queue: str, session: ClientSession) -> List[Repository]:
        """Perform search with the search_queue in Gitlab platform."""
        headers = {"PRIVATE-TOKEN": self.token}
        async with session.get(url=self.url + search_queue, headers=headers) as resp:
            resp = await resp.json()
            if self.check_response(resp):
                return GitlabSerializer().serialize(resp)
