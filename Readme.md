# BAHIS Data Processing Pipelines

##  Setting up the environment for data pipeline for Ubuntu

###  Install python 3.10 or later versions
To install python for your system please refer to the official documents. The link to the installation guide is given below:

https://realpython.com/installing-python/

###  Install pipenv
To install pipenv for your system please refer to the official documents. The link to the installation guide is given below:

https://pypi.org/project/pipenv/#installation

###  Use pipenv shell to activate the environment
Go inside the bahis-data directory and run the following command to activate the environment to install the required modules

`pipenv shell`

in order to use correctly server scripts, clone the repository to `/bahis-data` and create a directory `/bahis-data/.venv` so the virtual environment is available in the predictable location for cron jobs.

The following is a cronjob to run:
```
0 23 * * * cd /bahis-data/server-scripts/ && sh otter-nightly.sh >> log.txt
```
## Known missing files
The following files are needed to run prep_data.py:
	1. newbahis_bahis_patient_registrydyncsv_live_table.csv
	2. newbahis_bahis_species_table.csv
	3. newbahis_bahis_diagnosis_table.csv
	
Put the stated files in the "output" folder inside the "prep_dash" folder.

## Lookup table
The file named "bahis_data_lovi_top_diagnosis.xlsx" contains the lookup table for correcting the spellings of diseases. Put this file in the "output" folder inside the "prep_dash" folder.
	
## Running pre-processing and downloading
```
pipenv shell
python server-scripts/import_data.py
python prep_dash/prep_data.py
python prep_dash/prepgeojson.py
```

## Known issues
Despite Pandas being specified as `1.5`, pipenv installs version `'2.0.1'`.
