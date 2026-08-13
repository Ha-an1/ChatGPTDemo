from flask import Flask, jsonify, request
from flask_cors import CORS

from calculator import calculate

app = Flask(__name__)
CORS(app)


@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.post("/api/calculate")
def calculate_endpoint():
    data = request.get_json(silent=True) or {}

    try:
        result = calculate(
            data.get("operation"),
            float(data.get("a")),
            float(data.get("b")),
        )
        return jsonify({"result": result})
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        return jsonify({"error": str(exc)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
