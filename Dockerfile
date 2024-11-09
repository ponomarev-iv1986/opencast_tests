FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

CMD ["pytest", "--remote", "--url", "http://path_to_opencart", "--executor", "path_to_selenoid"]