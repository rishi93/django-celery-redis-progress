FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /mysite
WORKDIR /mysite
COPY requirements.txt /mysite/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /mysite/
