FROM python:3.9-slim as base

RUN mkdir /autocut_fix
COPY ./ /autocut
WORKDIR /autocut

RUN apt update && \
    apt install -y git && \
    apt install -y ffmpeg

RUN pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu && \
    pip install .