# GitApi
A mini API that functions as a layer between an application and several integrations (Gitlab, Github) and allows to search for repositories.


## Run the project
To build the docker image, run the following command:
`docker build -t git_api  .`

When the image is built run:

`docker run -p 8080:8080 -t git_api`
