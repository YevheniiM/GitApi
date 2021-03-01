from copy import deepcopy

import pytest

from src.app.helpers.serialization import GithubSerializer, GitlabSerializer
from src.app.models import Repository
from src.tests.helpers.constants import (VALID_REQUEST_DATA_GITHUB,
                                         VALID_REQUEST_DATA_GITLAB,
                                         VALID_RESPONSE_DATA_GITHUB,
                                         VALID_RESPONSE_DATA_GITLAB)


def test_success_serialization_gitlab():
    serialized_data = GitlabSerializer().serialize(VALID_REQUEST_DATA_GITLAB)
    assert serialized_data == [Repository(**VALID_RESPONSE_DATA_GITLAB[0])]


def test_success_serialization_github():
    serialized_data = GithubSerializer().serialize(VALID_REQUEST_DATA_GITHUB["items"])
    assert serialized_data == [Repository(**VALID_RESPONSE_DATA_GITHUB[0])]


def test_failed_serialization_gitlab():
    incorrect_data = deepcopy(VALID_REQUEST_DATA_GITLAB)
    incorrect_data[0].pop("name")
    with pytest.raises(KeyError):
        GitlabSerializer().serialize(incorrect_data)


def test_failed_serialization_github():
    incorrect_data = deepcopy(VALID_REQUEST_DATA_GITHUB["items"])
    incorrect_data[0].pop("name")
    with pytest.raises(KeyError):
        GithubSerializer().serialize(incorrect_data)
