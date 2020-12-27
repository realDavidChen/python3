### 搭建python运行虚拟环境


$ sudo apt install python3-virtualenv

$ virtualenv -p python3 venv

$ source ./venv/bin/activate

### 安装并运行flask 

$ pip install Flask

$ pip list

### 创建一个实例 app.py

新建 app.py 在内容中输入：

```
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Hello real time1140 world11</h1>"


if __name__ == '__main__':
    app.run(debug=True)


```

$ source venv/bin/activate

### 停止WARNING警告提示 

export FLASK_ENV=development

