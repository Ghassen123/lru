FROM python:3.8-slim-buster
RUN pip install --upgrade pip
RUN adduser  ghassen
USER ghassen
WORKDIR /app
ENV PATH="/home/ghassen/.local/bin:${PATH}"
COPY --chown=ghassen:ghassen . /app
RUN pwd
RUN ls -l
RUN pip install --user -r /app/requirements.txt
ENTRYPOINT ["python3","main.py"]
