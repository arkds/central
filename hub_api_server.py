from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/temperature', methods=['POST'])
def temperature():
    content = request.json
    print(content)
    return jsonify({'all_good': True})


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
