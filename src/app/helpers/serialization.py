from abc import abstractmethod, ABC
from typing import List

from src.app.models import Repository


class RepositorySerializer(ABC):
    @property
    @abstractmethod
    def mapper(self) -> dict:
        """
        Return the dict object with mapping between the
        generalized Repository fields and the actual fields returned
        by the actual API.
        """
        pass

    def serialize(self, api_data: List[dict]) -> List[Repository]:
        data = []
        for repository in api_data:
            repository_info = {}
            for internal_field, api_field in self.mapper.items():
                repository_info[internal_field] = repository[api_field]
            data.append(Repository(**repository_info))
        return data

    @staticmethod
    def deserialize(data: List[Repository]) -> List[dict]:
        api_data = []
        for repository in data:
            api_data.append(repository.dict())
        return api_data


class GithubSerializer(RepositorySerializer):
    mapper = {
        "name": "name",
        "full_name": "full_name",
        "description": "description",
        "forks_count": "forks",
        "stars_count": "stargazers_count",
        "default_branch": "default_branch",
        "ssh_url": "ssh_url",
        "http_url": "html_url",
        "created_at": "created_at",
        "updated_at": "updated_at",
    }


class GitlabSerializer(RepositorySerializer):
    mapper = {
        "name": "name",
        "full_name": "path_with_namespace",
        "description": "description",
        "forks_count": "forks_count",
        "stars_count": "star_count",
        "default_branch": "default_branch",
        "ssh_url": "ssh_url_to_repo",
        "http_url": "http_url_to_repo",
        "created_at": "created_at",
        "updated_at": "last_activity_at",
    }
