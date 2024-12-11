FROM python:3.13-slim
LABEL authors="christoph"

WORKDIR /usr/src/app

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

#COPY ecocounterdomainupdater ecocounterdomainupdater/
COPY dist/ecocounterdomainupdater-1.0.0.tar.gz dist/

RUN pip install --no-cache-dir dist/ecocounterdomainupdater-1.0.0.tar.gz

#CMD ["python", "-m", "ecocounterdomainupdater"]
CMD "ec-domain-updater"
