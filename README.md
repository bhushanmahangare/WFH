# WFH
mkdir WFH

cd WFH

python3 -m venv env


virtualenv --version


source source env/bin/activate

pip3 install -r requirements.txt

pip3 freeze

django-admin.py startproject core

django-admin.py startapp authentication
