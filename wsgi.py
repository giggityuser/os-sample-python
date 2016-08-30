import time

from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    time.sleep(10) # delays for 10 seconds
    return "Hello Universe!"

if __name__ == "__main__":
    application.run()
