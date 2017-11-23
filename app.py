import matplotlib

# Use Agg as backend, necessary for Heroku
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from flask import Flask, jsonify, redirect, render_template, request, send_file
from sqlalchemy.exc import IntegrityError

from config import DATABASE_URL, PORT
from models import Temperature
from repository import Repository

app = Flask(__name__)

repo = Repository(DATABASE_URL)

plt.style.use('fivethirtyeight')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def redirect_to_index():
    return redirect('/')


@app.errorhandler(404)
def page_not_found(error):
    return redirect('/')


@app.route('/temperature/stats')
def get_plot():
    temps = repo.temperatures(0)[:100]
    print(temps)
    timestamps = []
    _temps = []
    for temp in temps:
        _temps.append(temp.temperature)
        timestamps.append(temp.timestamp)
    temps = _temps
    plt.plot(timestamps, temps)
    plt.savefig('tmp/0.png')
    plt.clf()
    return send_file('tmp/0.png', mimetype='image/jpg')


@app.route('/temperature', methods=['GET'])
def get_temperature():
    temps = []
    for temp in repo.temperatures(0):
        temps.append({
            'temperature': temp.temperature,
            'timestamp': temp.timestamp
        })
    return jsonify({
        'all_good': True,
        'temperatures': temps
    })


@app.route('/temperature/add', methods=['POST'])
def post_temperature():
    """
    Specification

    The dictionary POSTed should be of the following structure:

    {
        'device_id': <integer>
        'temperature': <float>,
        'timestamp': <float>,
    }
    """

    content = request.json

    try:

        """
        JSON to POST looks like this:
        
        {
            'temperatures': [
                {
                    'temperature': 25,
                    'timestamp': 1000000,
                },
                ...
            ]
        }
        """

        repo.add_all([
            Temperature(
                device_id=0,
                temperature=temp['temperature'],
                timestamp=temp['timestamp']
            ) for temp in content['temperatures']
        ])
    except IntegrityError:
        return jsonify({'all_good': False, 'error': 'Key already exists'})
    except KeyError:
        return jsonify({
            'all_good': False,
            'error': 'Invalid request'
        })
    else:
        return jsonify({
            'all_good': True
        })


@app.route('/temperature/delete', methods=['POST'])
def delete_temperature():
    """
    Specification

    The dictionary POSTed should be of following structure:

    {
        'temperatures': {
            'device_id': <integer>,
            'timestamp': <float>
        }
    }
    """

    temperatures = request.json['temperatures']
    try:
        repo.delete_temperatures(temperatures)
    except KeyError as error:
        return jsonify({
            'all_good': False,
            'error': error
        })


def main():
    app.run(debug=True, port=PORT, host='0.0.0.0')


if __name__ == '__main__':
    main()
