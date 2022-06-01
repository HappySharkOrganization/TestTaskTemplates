FROM continuumio/miniconda3

COPY requirements.txt .
COPY packages.txt .

RUN apt-get update && apt-get install -y < packages.txt


RUN conda update -n base -c defaults conda
RUN conda create -n dsp_py python=3.9

SHELL ["/bin/bash", "--login", "-c"]
RUN conda init bash
RUN echo "conda activate dsp_py" > ~/.bashrc

RUN pip install -r requirements.txt


ADD . /runtime/task
WORKDIR /runtime/task/src

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "dsp_py", "bash", "main.sh"]
