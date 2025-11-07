from flask import Flask, request, jsonify
# Simple AI serve stub (can be moved to FastAPI later)
app = Flask(__name__)

@app.route('/diagnose', methods=['POST'])
def diagnose():
    payload = request.json or {}
    # Placeholder: call real model here
    return jsonify({
        "suggestions": [
            {"issue": "Faulty charger", "confidence": 0.86, "parts": [{"sku": "CHG-001", "qty": 1}], "steps": ["Check charger", "Replace if faulty"]},
            {"issue": "Battery degraded", "confidence": 0.45, "parts": [{"sku": "BAT-123", "qty": 1}], "steps": ["Run battery diagnostics", "Replace battery if <80%"]}
        ],
        "model_version": "v0.0.1"
    })

@app.route('/forecast', methods=['GET'])
def forecast():
    return jsonify({"message": "forecast endpoint placeholder"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
