from config import DATABASE_URL
from flask import Flask, jsonify, request
from models import Temperature
from sqlalchemy.exc import IntegrityError

from src.repository import Repository

app = Flask(__name__)

repo = Repository(DATABASE_URL)


@app.route('/temperature', methods=['POST'])
def temperature():
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
    app.run(debug=True)


if __name__ == '__main__':
    main()
