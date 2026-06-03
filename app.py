from flask import Flask

app = Flask(__name__)

def devops_message():
    return "CI/CD Pipeline is Working!"

@app.route('/')
def home():
    return devops_message()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)