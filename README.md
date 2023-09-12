# BAHIS Data Pipeline

This repository contains the data pipeline for the BAHIS project. It is a collection of scripts that download data from the BAHIS postgreSQL database, process it, and export it as csv files that can be used by the dashboard.

## Local Installation

First [install pipenv](https://pipenv.pypa.io/en/latest/install/). If you installed pipenv using `sudo apt install pipenv` and [getting this error](https://github.com/pypa/pipenv/issues/5133) install using `pip` instead.

1. `pipenv install`
2. copy data from `output` to `bahis-dash/exported_data/` if running the dashboard

If you get an error when running install like this:

```bash
Resolving dependencies...
✘ Locking Failed!
```

remove the `Pipfile.lock` file and run again.

## Local development

Run `pipenv run python pipeline.py`. (If you get a `Permission denied` error you may need to run as `sudo`)

This will run a development server with hot reloading and other useful features.

## Deployment

To run the system in a local "deployment" you can use the Dockerfile with `docker build -t data . && docker run -p 80:80 --name bahis-data data:latest`. Note this will fail if `bahis_creds_file.cnf` is not valid, i.e. points to a local postgreSQL instance. You will also need to make sure the backup sql file is in the `input` directory.

Cloud deployment is done (currently manually) using bahis-infra. Only the latest release will be deployed - releases are created automatically when a PR is successfully merged into `main`.

The following is a cronjob that is added to crontab in the docker that will run the scripts each night at 23:00:

```cron
0 23 * * * cd /home/app && sh nightly.sh >> log.txt
```

If you need to run the script immediately just run `docker exec bahis-data sh nightly.sh` from your terminal.

## Known missing files

The following files are needed to run prep_data.py:

1. newbahis_bahis_patient_registrydyncsv_live_table.csv;
2. newbahis_bahis_species_table.csv;
3. newbahis_bahis_diagnosis_table.csv;
4. newbahis_geo_cluster.csv.

Put the stated files in the "output" folder.

## Adding pipeline scripts

Add new pipelines scripts to the `pipeline_scripts` folder. The script should have a `main()` function that is called by `pipeline.py`. The `main()` function should read inputs from the `input` folder and save outputs to the `output` folder. We currently don't have chained pipelines.

## Lookup tables

The file named "bahis_data_lovi_top_diagnosis.xlsx" contains the lookup table for correcting the spellings of diseases. Put this file in the "lookup" folder.
