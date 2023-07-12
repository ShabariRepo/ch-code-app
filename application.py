# use flask as simple backend to get things running faster
# boilerplate python hello world structrue

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Get to the choppaaa!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
