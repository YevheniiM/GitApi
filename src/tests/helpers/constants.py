VALID_REQUEST_DATA_GITLAB = [
    {
        "name": "name",
        "path_with_namespace": "full-name",
        "description": "description",
        "forks_count": 0,
        "star_count": 0,
        "default_branch": None,
        "ssh_url_to_repo": "git@gitlab.com:blah.git",
        "http_url_to_repo": "https://gitlab.com/blah.git",
        "created_at": "2021-03-01T14:10:48.528Z",
        "last_activity_at": "2021-03-01T14:10:48.528Z",
    }
]

VALID_REQUEST_DATA_GITHUB = {
    "items": [
        {
            "name": "name",
            "full_name": "full-name",
            "description": "description",
            "avatar_url": None,
            "forks": 0,
            "stargazers_count": 0,
            "default_branch": None,
            "ssh_url": "git@gitlab.com:blah.git",
            "html_url": "https://gitlab.com/blah.git",
            "created_at": "2021-03-01T14:10:48.528Z",
            "updated_at": "2021-03-01T14:10:48.528Z",
        }
    ]
}

VALID_RESPONSE_DATA_GITLAB = [
    {
        "name": "name",
        "full_name": "full-name",
        "description": "description",
        "forks_count": 0,
        "stars_count": 0,
        "default_branch": None,
        "ssh_url": "git@gitlab.com:blah.git",
        "http_url": "https://gitlab.com/blah.git",
        "created_at": "2021-03-01T14:10:48.528Z",
        "updated_at": "2021-03-01T14:10:48.528Z",
    }
]

VALID_RESPONSE_DATA_GITHUB = [
    {
        "name": "name",
        "full_name": "full-name",
        "description": "description",
        "forks_count": 0,
        "stars_count": 0,
        "default_branch": None,
        "ssh_url": "git@gitlab.com:blah.git",
        "http_url": "https://gitlab.com/blah.git",
        "created_at": "2021-03-01T14:10:48.528Z",
        "updated_at": "2021-03-01T14:10:48.528Z",
    }
]
