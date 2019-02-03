"" 
setup:
    - pip install django
    - pip install django-allauth
    - pip install extensions
    - pip install pyOpenSSL
    - pip install facebook-sdk
    - pip install django-mysql
    - pip install mysqlclient with binary 
    - pip install python-dev mysql-server libmysqlclient-dev
    - pip install mysqlclient
    
script:
    - manage.py runserver_plus --cert-file CERT_PATH