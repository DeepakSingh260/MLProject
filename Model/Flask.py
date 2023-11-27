from flask import Flask , request , jsonify


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/api/post_example', methods=['POST'])
def post_example():
    if request.method == 'POST':
        data = request.get_json()
        return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)

