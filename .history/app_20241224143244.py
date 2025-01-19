from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Sample driver data
drivers = [
    {"name": "John Doe", "experience": 5},
    {"name": "Jane Smith", "experience": 3},
    {"name": "James Brown", "experience": 8},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/drivers", methods=["GET"])
def get_drivers():
    return jsonify(drivers)

if __name__ == "__main__":
    app.run(debug=True)
