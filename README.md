# WFH
mkdir WFH

cd WFH

python3 -m venv env


virtualenv --version


source env/bin/activate

pip3 install -r requirements.txt

pip3 freeze

django-admin.py startproject src
cd src

django-admin.py startapp authentication
django-admin.py startapp network
