## uninstall_python3 and install new python

** recommend using virtualenv, and never modifying the system python, except to install pip and virtualenv if necessary.
As was alluded to above, many OSes count on having a working python2 in order to function


$ apt-get remove python3

$ apt-get install python3

$ pip3 install virtualenv

$ virtualenv -p python3 venv
$ . venv/bin/activate

now you are in a nice python3 world, completely isolated from system python
remember to say . venv/bin/python every time you do anything
or you can even add it to your .bashrc
