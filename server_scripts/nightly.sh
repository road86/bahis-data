set -xe
date
psql -U postgres -h pgdb -f init.sql
cd ../input
tar xf coredb_bup.tar.gz
psql -U postgres -h pgdb -d coredb -f coredb_bup.sql
cd ..
python3 server_scripts/import_data.py
python3 pipeline.py
