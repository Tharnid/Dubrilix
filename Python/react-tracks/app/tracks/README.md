# create app 
python manage.py startapp XXXX

# migrate db
python manage.py makemigrations

python manage.py migrate <app> (leave app blank for all migrations)