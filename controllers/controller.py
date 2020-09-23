from app import app

@app.route('/')
def index():
    return "This is an awesome message because Hello World sucks"

@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"