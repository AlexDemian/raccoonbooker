# Modify settings/secret.py
```python
EMAIL_HOST_PASSWORD = 'password'
```

# Python
```sh
cd django-app
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py collectstatic
python manage.py collectstatic_js_reverse --settings=config.settings.angular
python manage.py migrate
python manage.py runserver
```

# Angular
```sh
cd ng-app
sudo apt-get install npm
npm install -g @angular/cli
npm install
ng build
```