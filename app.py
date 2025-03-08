from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World111! This is a Dockerized Flask app deployed on Amazon ECS."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

