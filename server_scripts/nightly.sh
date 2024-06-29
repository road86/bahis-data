PATH=/home/app/.venv/bin:$PATH
set -xe
date
cd /home/app/server_scripts
psql -U postgres -h dashdb -f init.sql
cd ../input
tar xf coredb_bup.tar.gz
psql -U postgres -h dashdb -d coredb -f coredb_bup.sql
cd ..
python3 server_scripts/import_data.py
python3 pipeline.py
