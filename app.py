from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Flask app developed by upendra sir!"

if __name__ == '__main__':
    app.run(debug=True)