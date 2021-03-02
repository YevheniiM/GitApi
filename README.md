# GitApi

### A mini API that functions as a layer between an application and several integrations (Gitlab, Github) and allows searching for repositories.

###### [aiohttp](https://docs.aiohttp.org/en/stable/) - asynchronous HTTP Client/Server was used.

---

## Run the project

Firstly, you need to generate
the [Gitlab](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#personal-access-tokens)
API key and paste it to `src/config/config.yaml`

Then, to build the docker image, run the following command:

`docker build -t git_api .`

When the image is built run:

`docker run -p 8080:8080 -t git_api`

After that you can access an API with the `http://hostname:8080/api/search/?{search_query}` link.

---

## Possibilities

The detailed info about search_query params is in the docs section, here are a few examples:

`http://hostname:8080/api/search/?platfotm=github&name=tetris`

`http://hostname:8080/api/search/?platfotm=gitlab&name=tictactoe`

The API allows choosing between platforms and specify the name of the repository.

---

## Tests

Tests are run automatically on image build. You can run them manually with a command:
`python -m pytest src/tests/`

---

## Documentation

Docs are available here: `http://hostname:8080/api/doc/` under the **Search repositories**
section.

---

## Pros and cons of the chosen approach

The main efforts here were to build a high level of abstraction to be able to add new platforms without modifying the
logic of views and without adding new url patterns. For example, to add a Bitbucket platform, you just need to add:

1. BitbucketClient class, with defined `search` method, where the url is specified, and the request is performed.

2. BitbucketQueryParser, with defined `parse` method, where the mapping from the internal API format to an external one
   is done.

3. BitbucketSerializer, with defined mapper attribute in such format:

```
    mapper = {
        "name": "bitbucker_name",
        "full_name": "bitbucker_full_name",
        "description": "bitbucker_description",
        "forks_count": "bitbucker_forks",
        "stars_count": "bitbucker_stargazers_count",
        "default_branch": "bitbucker_default_branch",
        "ssh_url": "bitbucker_ssh_url",
        "http_url": "bitbucker_html_url",
        "created_at": "bitbucker_created_at",
        "updated_at": "bitbucker_updated_at",
    }
```

All the logic is written in the base class, where all the actual mapping between those fields is performed, so no
worries about that.

---
The pros of such an approach are obvious:

1. The code is scalable.
2. No need to copy-paste views when some new platform are added (all the logic is written in one view).
3. The request query is unified. So, no matter which platform you're using underneath, your request query remains the
   same. It's then parsed in the QueryParser object independently for each platform.
4. Adding new query parameters is also pretty easy.

The cons are also here:

1. Lots of abstractions. For such a small task there was really no need to use those abstractions and just a one view.
   The project got pretty big because of them. But they were added because of the potential of future scalability.
2. There is only one query parameter `name` in the API. That is because of the lack of my time. It's not a big problem
   to add a several ones with this kind of architecture.
3. I was focused on separating the platforms and working with them independently. That's why there is no possibility to
   get some merged results from them (it's not a problem to add if I had more time).
4. Tests are pretty incomplete because of lack of time.
5. Docs also could be better :)
   