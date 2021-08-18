FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
# RUN pip install -r requirements.txt

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/

EXPOSE 5000
CMD ["python", "/app/main.py"]
