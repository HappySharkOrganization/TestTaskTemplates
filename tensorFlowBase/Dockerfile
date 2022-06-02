FROM tensorflow/tensorflow:latest-jupyter

COPY requirements.txt .
COPY packages.txt .

RUN apt-get update && apt-get install -y < packages.txt



RUN python3 -m pip install --no-cache-dir -r requirements.txt

ADD . /runtime/task
WORKDIR /runtime/task/src

ENTRYPOINT ["python3", "-m", "main"]

