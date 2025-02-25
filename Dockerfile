# https://medium.com/@nicholaszolton/fastapi-on-aws-lambda-with-docker-5ca5f76a9880
# https://stackoverflow.com/questions/65608802/cant-deploy-container-image-to-lambda-function

FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /

RUN apt update && apt install -y --no-install-recommends \
  python3 python3-pip python3-dev libopenblas-dev liblapack-dev gfortran && \
  rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --no-cache-dir --upgrade pip

COPY requirements-prod.txt /requirements-prod.txt

RUN pip install --no-cache-dir --upgrade -r /requirements-prod.txt

COPY . /

RUN ls -l /scripts/
RUN ls -l /

RUN chmod +x /scripts/lambda_entry_script.sh

ENTRYPOINT ["/scripts/lambda_entry_script.sh", "main.handler"]
