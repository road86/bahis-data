set -xe
date
sudo -u postgres psql -f init.sql
cd ../input
# copying local file 
cp /home/bahis/backups/coredb_bup.tar.gz .
tar xf coredb_bup.tar.gz
sudo -u postgres psql -d coredb -f coredb_bup.sql
cd /bahis-data/
/bahis-data/.venv/bin/python server-scripts/import_data.py
/bahis-data/.venv/bin/python prep_dash/prepgeojson.py
/bahis-data/.venv/bin/python prep_dash/prep_data.py
cp -r /bahis-data/output/* /bahis-dash/exported_data/