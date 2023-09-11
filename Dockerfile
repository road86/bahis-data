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
RUN (echo "0,5,10,15,20,25,30,35,40,45,50,55  * * * * cd /home/app/server_scripts && sh ./nightly.sh >> log.txt") | crontab -

# Start cron in the foreground
# CMD cron -f
WORKDIR /home/app/server_scripts
CMD sh ./nightly.sh
