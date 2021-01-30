## 先激活Pipenv环境
$ pipenv shell
## 获取当前虚拟环境的位置
$ pipenv --venv
/home/username/.local/share/virtualenvs/form-gOja0Zni

在settings.json 文件中，添加下面这段代码（路径为 pipenv --venv 查询到的真实路径替换）

"python.pythonPath": "/home/username/.local/share/virtualenvs/form-gOja0Zni",
