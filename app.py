from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize seed value
seed_value = 0

@app.route("/", methods=["POST"])
def update_seed():
    global seed_value
    data = request.get_json()
    if "num" in data and isinstance(data["num"], int):
        seed_value = data["num"]
        return jsonify({"message": "Seed value updated successfully"}), 200
    else:
        return jsonify({"error": "Invalid input, expected JSON with an integer field 'num'"}), 400

@app.route("/", methods=["GET"])
def get_seed():
    return str(seed_value), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
