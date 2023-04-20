FROM python:3.9

RUN ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime

WORKDIR /app

COPY app/requirements.txt .
RUN pip3 --no-cache-dir install -r requirements.txt

COPY app .

CMD ["python3", "-u", "/app/app.py"]