"" 
setup:
    - pip install django
    - pip install django-allauth
    - pip install extensions
    - pip install pyOpenSSL
    - pip install facebook-sdk
script:
    - manage.py runserver_plus --cert-file CERT_PATH