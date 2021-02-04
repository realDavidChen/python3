You may need to install the Python 3 and MySQL development headers and libraries like so: 

1.1 For UBUNTU or Debian

$ sudo apt-get install python3-dev default-libmysqlclient-dev build-essential

1.2 Red Hat / CentOS

$ sudo yum install python3-devel mysql-devel

2. Then try

$ pip install mysqlclient
