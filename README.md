# Mail-Archive

My personal, read-only mirror for mailing list archives.

https://mail-archive.mozz.us

## Installation Notes

### Initialize the database (sqlite3)

```
python manage.py migrate
```

### Load seed data

```
python manage.py loaddata first_start
```

### Create superuser

```
python manage.py createsuperuser
```

### Build static assets

```
python manage.py collectstatic
python manage.py compress
```