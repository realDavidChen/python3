```

apt-get remove python3
apt-get install python3
pip3 install virtualenv
virtualenv -p python3 venv
. venv/bin/activate
```
# now you are in a nice python3 world, completely isolated from system python
# remember to say . venv/bin/python every time you do anything
# or you can even add it to your .bashrc
