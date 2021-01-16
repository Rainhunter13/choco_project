FROM python:3
ENV PYTHONBUFFERED=1
WORKDIR /
COPY requirements.txt ./
RUN pip install -r requirements.txt
