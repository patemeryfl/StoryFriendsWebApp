from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")

@app.route('/')
def hello():
     return render_template('index.html')

@app.route('/display', methods=["GET", "POST"])
def display():
     return jsonify(request.form)

if __name__ == "__main__":
    app.run()
