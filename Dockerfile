FROM python:3.8
EXPOSE 8080

COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt
COPY ./src/ /data/src/

RUN python -m pytest /data/src/tests
RUN flake8 --ignore E501 ./data/src
RUN isort ./data/src

ENV PYTHONPATH=/data/

WORKDIR /data/
CMD ["python", "src/app/main.py"]