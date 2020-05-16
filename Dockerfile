from alpine:latest
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app
COPY . /app

EXPOSE 4000

ENTRYPOINT ["python3"]
CMD ["receive.py"]
