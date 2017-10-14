from random import randint

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/current_temperature')
def current_temperature():
    return jsonify(result=randint(-31, 32))


@app.route('/add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@app.route('/random')
def random():
    return jsonify(rgit aesult=randint(1, 100))


@app.route('/')
def index():
    return render_template('index.html')


def main():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
