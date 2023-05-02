# BAHIS Data Processing Pipelines

## Data
Available here: https://drive.google.com/drive/folders/1l5AL2O7nnpnsh73UjqjLYcBotwdthsWs?usp=sharing

## Comment
I've pulled data from static bahis and had some fun formatting it (all the different forms submissions are in one table with the actual data stored as key:value pairs). I have uploaded the data for you into google drive, those are files in a format `formdata_*.csv`.
You will notice however that it is not possible to find out what different indexes mean in many cases. I leave that for you to find out as you go through whichever dataset you find most interesting. The tables that contain keys for submitted data are in `input/STATICBAHIS*.csv` files, though at this point I'm not sure what is what.

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

