## create run.sh file to run app by terminal

### create app.py like:
```
from flask import Flask

app = Flask(__name__)

# http://localhost:8000/


@app.route("/abc", methods=['GET'])
def hello_world():
    # run other code here.
    return "Hello, world. this is Flask"

```




1. create run.sh and add content:
```
uvicorn server

