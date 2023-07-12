# use flask as simple backend to get things running faster
# boilerplate python hello world structrue

# import time for sleep or wait function
import time
from flask import Flask

# lazy but didnt really find a better way that is not 100 lines of code & this was simple :S
time.sleep(30)

app = Flask(__name__)

@app.route('/')
def home():
    #return "Get to the choppaaa!"
    return os.getenv('CUSTOM_MESSAGE', 'Hello!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
