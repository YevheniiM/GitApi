from abc import ABC, abstractmethod

from multidict import MultiDictProxy


class BaseQueryParser(ABC):
    @staticmethod
    @abstractmethod
    def parse(query: MultiDictProxy) -> str:
        """Parse the parameters of the internal API to the external query format"""
        pass


class GithubQueryParser(BaseQueryParser):
    @staticmethod
    def parse(query: MultiDictProxy) -> str:
        """Parse the parameters of the internal API to the Github query format"""
        search_query = f"?q={query['name']}"
        return search_query


class GitlabQueryParser(BaseQueryParser):
    @staticmethod
    def parse(query: MultiDictProxy) -> str:
        """Parse the parameters of the internal API to the Gitlab query format"""
        return f"?scope=projects&search={query['name']}"
