# Installation Notes

#### Setup virtual environment

```
python -m virtualenv venv
source venv/bin/activate.fish
```

#### Initialize the database (sqlite3)

```
python manage.py migrate
```

#### Load seed data

```
python manage.py loaddata first_start
```

#### Create superuser

```
python manage.py createsuperuser
```
