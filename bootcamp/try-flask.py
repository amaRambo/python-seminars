from flask import Flask


app = Flask(__name__)

@app.route('/')
def main():
    return '<h1>hello!<h1><br><a href ="/index">перейти на 2-ую страницу</a>'

@app.route('/index')
def index():
    return "hello it's my firts project!"

if __name__ == '__main__':
    app.run()