# django_celery
This project is about to send email to user on user's specific time daily or weekly.

Install all the packages from requirements.txt
```
pip3 install -r requirements.txt
```

For making migrations 
```
python3 manage.py makemigrations
```
To apply migrations
```
python3 manage.py migrate
```
To run local server
```
python3 manage.py runserver
```
Install redis-server
```
sudo apt-get install redis-server
```
Run django celery worker
```
celery -A django_celery worker --pool=solo -l info
```
Run celery beat
```
celery -A django_celery beat -l INFO
```
# django_celery
