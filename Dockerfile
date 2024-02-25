FROM python:3.11-slim

RUN apt update
RUN apt install -y postgresql-client cron

RUN mkdir -p /home/app
WORKDIR /home/app

RUN pip install pipenv==2023.9.8
ENV PIPENV_VENV_IN_PROJECT=1
COPY Pipfile Pipfile.lock ./
RUN pipenv sync
ENV PATH=/home/app/.venv/bin:${PATH}

COPY . ./

# Add crontab entry. The following schedules the script to run daily at midnight.
RUN (echo "10 2 * * * /home/app/server_scripts/nightly.sh >> /home/app/server_scripts/log.txt 2>&1") | crontab -

# Start cron in the foreground
CMD cron -f
CMD touch /home/app/server_scripts/log.txt
