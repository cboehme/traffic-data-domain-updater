FROM python:3.13-slim
LABEL authors="christoph"

WORKDIR /usr/src/app

COPY dist/ecocounterdomainupdater-1.0.0.tar.gz dist/

RUN pip install --root-user-action=ignore --no-cache-dir dist/ecocounterdomainupdater-1.0.0.tar.gz

COPY fargate.py ./

CMD ["python", "./fargate.py"]
