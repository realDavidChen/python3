
## config  django project env


$ mkdir django

$ code django

> open the folder in vs code

$ pipenv install -e .

$ pipenv shell

$ pip list

$ pip install django
  
## start django project



$ django-admin -h
> get django-helop, this is all help commands

```
Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
```

> start django project

$ django-admin startproject myproject

$ cd myproject

$ python manage.py runserver

all seting is finish, now open the browser , and type http://localhost:8000


## add apps inner myproject and runserver

$ cd myproject



$ django-admin startapp admin


## start run app server

$ python manage.py runserver

> now you can visit http://localhost:8000/admin






> you can get manage.py commends and help

$ python manage.py


```
Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
    
```
