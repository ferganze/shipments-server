# shipments-server

## Project setup
```
python3 -m venv env

```
```
source env/bin/activate
```

Install packages:
```
pip install django
pip install django-rest-framework
pip install django-cors-headers
```

Run Migration:
```
python3 manage.py makemigrations shipments_api
python3 manage.py migrate
```

### Run Server
```
python3 manage.py runserver
```

### Run Tests
```
python3 manage.py test
```
