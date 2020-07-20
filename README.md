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



=-=-=-=-=-=-=-=-=-=-=-=
How To Use MySQL or MariaDB with your Django Application on Ubuntu
Mysql
sudo apt-get update
sudo apt-get install python-pip python-dev libmysqlclient-dev
pip install django mysqlclient



MariaDB
sudo apt-get update
sudo apt-get install python-pip python-dev libmariadbclient-dev libssl-dev
pip install django mysqlclient

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
