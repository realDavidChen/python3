## basic env 


### 1. linux system(ubuntu system select 1.1)

1.1 For UBUNTU or Debian

$ sudo apt-get install python3-dev default-libmysqlclient-dev build-essential

1.2 Red Hat / CentOS

$ sudo yum install python3-devel mysql-devel

### 2. pip install mysqlclien

$ pip install mysqlclient

## in phpmyadmin create a new databases name: django

## django project/settings.py


```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': 'yourpastword',
        'HOST': 'localhost',
        'PORT': ''

    }
}

```

## migrate databases to mysql

$ python manage.py migrate


