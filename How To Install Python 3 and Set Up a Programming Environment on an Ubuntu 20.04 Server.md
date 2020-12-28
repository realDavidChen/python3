
# How To Install Python 3 and Set Up a Programming Environment on an Ubuntu 20.04 Server

### Step 1 --- Setting Up Python 3


$ sudo apt update

$ sudo apt -y upgrade

$ python3 -V

$ sudo apt install -y python3-pip

$ pip3 install package_name

$ sudo apt install -y build-essential libssl-dev libffi-dev python3-dev


### Step 2 — Setting Up a Virtual Environment

$ sudo apt install -y python3-venv

$ mkdir environments

$ cd environments

Once you are in the directory where you would like the environments to live, you can create an environment by running the following command:

$ python3 -m venv my_env

Essentially, pyvenv sets up a new directory that contains a few items which we can view with the ls command:

$ ls my_env

$ source my_env/bin/activate

### Step 3 — Creating a “Hello, World” Program

$ nano hello.py

```
print("Hello, World!")
```

$ python hello.py

======more===================

## 搭建python运行虚拟环境


$ sudo apt install python3-virtualenv

$ virtualenv -p python3 venv

$ source ./venv/bin/activate

安装并运行flask
$ pip install Flask

$ pip list

创建一个实例 app.py
新建 app.py 在内容中输入：

```

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello world!"


if __name__ == '__main__':
    app.run(debug=True)

```

$ source venv/bin/activate

停止WARNING警告提示
export FLASK_ENV=development

