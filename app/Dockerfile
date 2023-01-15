FROM python:3.9

WORKDIR /WordGraph
COPY requirements.txt /WordGraph/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /WordGraph/requirements.txt

COPY . /WordGraph

CMD bash -c "while true; do sleep 1; done"