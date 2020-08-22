FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /kios
RUN mkdir /kios/db-kios
WORKDIR /kios
COPY requirements.txt /kios/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /kios/
EXPOSE 8080
