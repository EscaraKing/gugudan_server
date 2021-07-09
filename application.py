from flask import Flask, render_template, url_for, redirect
import sys
application = Flask(__name__)


@application.route("/")
def home():
    return render_template('main.html')


@application.route("/test")
def test():
    return render_template('test.html', content="testing")


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]))
