import pytest
from aiohttp import web

from src.app.routes import setup_routes
from src.tests.helpers.constants import (
    VALID_RESPONSE_DATA_GITLAB,
    VALID_RESPONSE_DATA_GITHUB,
    VALID_REQUEST_DATA_GITLAB,
    VALID_REQUEST_DATA_GITHUB,
)
from src.tests.helpers.mock_response import MockResponse


@pytest.fixture
def client(loop, aiohttp_client):
    app = web.Application()
    setup_routes(app)
    return loop.run_until_complete(aiohttp_client(app))


async def test_get_without_platform(client):
    resp = await client.get("/")
    assert resp.status == 404
    resp_json = await resp.json()
    assert resp_json == {"error": "None platform is not supported"}


async def test_get_with_incorrect_platform(client):
    resp = await client.get("/?platform=bitbucket")
    assert resp.status == 404
    resp_json = await resp.json()
    assert resp_json == {"error": "bitbucket platform is not supported"}


async def test_get_without_required_params_gitlab(client):
    resp = await client.get("/?platform=gitlab")
    assert resp.status == 404
    resp_json = await resp.json()
    assert resp_json == {"error": "The request query is incorrect"}


async def test_get_without_required_params_github(client):
    resp = await client.get("/?platform=github")
    assert resp.status == 404
    resp_json = await resp.json()
    assert resp_json == {"error": "The request query is incorrect"}


async def test_github_get_success_response(client, mocker):
    resp = MockResponse(VALID_REQUEST_DATA_GITHUB, 200)
    mocker.patch("aiohttp.ClientSession.get", return_value=resp)

    resp = await client.get("/?platform=github&name=name")
    data = await resp.json()

    assert resp.status == 200
    assert data == VALID_RESPONSE_DATA_GITHUB


async def test_gitlab_get_success_response(client, mocker):
    resp = MockResponse(VALID_REQUEST_DATA_GITLAB, 200)
    mocker.patch("aiohttp.ClientSession.get", return_value=resp)

    resp = await client.get("/?platform=gitlab&name=name")
    data = await resp.json()

    assert resp.status == 200
    assert data == VALID_RESPONSE_DATA_GITLAB
