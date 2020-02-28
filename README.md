# Python
```sh
cd django-app
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

# Angular
```sh
cd ng-app
apt-get install npm
npm install -g @angular/cli
npm install --save-dev @angular-devkit/build-angular
ng build
```