from app import app


@app.route('/', methods=['GET'])
def index():
    return 'Welcome to Star Wars End point. Test the endpoint in postman'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
