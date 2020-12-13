## create run.sh file to run app by terminal

### 1.create server.py like:
```
from flask import Flask

app = Flask(__name__)

# http://localhost:8000/


@app.route("/abc", methods=['GET'])
def hello_world():
    # run other code here.
    return "Hello, world. this is Flask"

```




### 2. create run.sh and add content:
```
uvicorn server:app

```

### 3. add execution authority to run.sh

$ chmod +x run.sh

### 4. running server.py

$ ./run.sh

or

$ bash run.sh

### check browser

in browser open http://127.0.0.1:8000 if seccessd, browser will show content

