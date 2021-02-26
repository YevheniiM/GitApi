from abc import ABC, abstractmethod

from multidict import MultiDictProxy


class BaseQueryParser(ABC):
    @staticmethod
    @abstractmethod
    def parse(query: MultiDictProxy) -> str:
        pass


class GithubQueryParser(BaseQueryParser):
    @staticmethod
    def parse(query: MultiDictProxy) -> str:
        search_query = f"?q={query.get('name')}+language:{query.get('language')}"
        return search_query


class GitlabQueryParser(BaseQueryParser):
    @staticmethod
    def parse(query: MultiDictProxy) -> str:
        return f"?scope=projects&search={query.get('name')}"
