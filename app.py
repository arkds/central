from flask import Flask, jsonify, redirect, render_template, request
from sqlalchemy.exc import IntegrityError

from config import DATABASE_URL, PORT
from models import Temperature
from repository import Repository

app = Flask(__name__)

repo = Repository(DATABASE_URL)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def redirect_to_index():
    return redirect('/')


@app.route('/temperature', methods=['GET'])
def get_temperature():
    return jsonify({'all_good': True})


@app.route('/temperature', methods=['POST'])
def post_temperature():
    content = request.json

    """
    Specification:
    
    The dictionary POSTed should be of the
    following structure:
    
    {
        'device_id': <integer>
        'temperature': <floating point>,
        'timestamp': <floating point>,
    }
    """

    print(content)

    try:
        repo.add(Temperature(
            device_id=0,  # content['device_id'],  # FIXME
            timestamp=content['timestamp'],
            temperature=content['temperature']
        ))
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


def main():
    app.run(debug=True, port=PORT, host='0.0.0.0')


if __name__ == '__main__':
    main()
