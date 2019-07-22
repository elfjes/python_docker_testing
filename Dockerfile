FROM python:3.7
RUN apt-get update && apt-get install -y \
    dumb-init \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /
RUN pip install -r requirements.txt
COPY app /app
ENTRYPOINT ["dumb-init", "--"]
CMD ["flask", "--help"]

