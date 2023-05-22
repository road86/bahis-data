set -e
date
#we are killing the dashboard to be able to perform data processing withoug running out of memory
pkill -f index.py
sudo -u postgres psql -f init.sql
cd ../input
# copying on local network from weasel
rsync --append --partial -chvP -e "ssh" root@192.168.0.7:/home/habis/coredb_bup.tar.gz .
tar xf coredb_bup.tar.gz
sudo -u postgres psql -d coredb -f coredb_bup.sql
sudo -u postgres psql -d bahistot -f bahistot.sql
cd ..
.venv/bin/python server-scripts/import_data.py
.venv/bin/python prep_dash/prepgeojson.py
.venv/bin/python prep_dash/prep_data.py
