set -xe
date
psql -U postgres -h dash-db -f init.sql
cd ../input
# copying local file 
cp /bahis-backup/coredb_bup.tar.gz .
tar xf coredb_bup.tar.gz
psql -U postgres -h dash-db -d coredb -f coredb_bup.sql
cd /bahis-data/
python3 server-scripts/import_data.py
python3 prep_dash/prepgeojson.py
python3 prep_dash/prep_data.py
mkdir -p /bahis-dash/exported_data
cp -r /bahis-data/output/* /bahis-dash/exported_data/
