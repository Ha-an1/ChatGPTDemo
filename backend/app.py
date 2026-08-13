from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory

from calculator import calculate

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

app = Flask(__name__, static_folder=str(FRONTEND_DIR), static_url_path="")


@app.get("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")


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
