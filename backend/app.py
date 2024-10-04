from flask import Flask, jsonify

app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the News Aggregator API"})

# Define a test route to check if the server is running
@app.route('/news')
def get_news():
    return jsonify({"news": "Sample news data will go here."})

if __name__ == '__main__':
    app.run(debug=True)

