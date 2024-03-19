#!/bin/sh
cd applications/sistema_escolar 
alembic upgrade 65c1fad9444a
cd ../..
python web2py.py -a '<recycle>' -i 0.0.0.0 -p 8000
