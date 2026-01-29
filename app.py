from flask import Flask, request, jsonify

app = Flask(__name__)

# Priority order: smaller number = higher priority
PRIORITY = {
    "emergency": 1,
    "paid": 2,
    "followup": 3,
    "walkin": 4
}

# Maximum patients allowed in one slot
CAPACITY = 3

# Doctors and their available time slots
doctors = {
    "D1": {"9-10": [], "10-11": []},
    "D2": {"9-10": [], "10-11": []},
    "D3": {"9-10": [], "10-11": []}
}

def allocate_token(doctor, slot, patient):
    slot_list = doctors[doctor][slot]
    slot_list.append(patient)
    slot_list.sort(key=lambda x: PRIORITY[x["type"]])

    if len(slot_list) > CAPACITY:
        return False
    return True

@app.route("/book", methods=["POST"])
def book():
    data = request.json
    if not allocate_token(data["doctor"], data["slot"], data):
        return jsonify({"status": "failed", "message": "Slot is full"}), 400
    return jsonify({"status": "confirmed", "message": "Token booked successfully"})

@app.route("/cancel", methods=["POST"])
def cancel():
    data = request.json
    doctors[data["doctor"]][data["slot"]] = [
        p for p in doctors[data["doctor"]][data["slot"]]
        if p["id"] != data["id"]
    ]
    return jsonify({"status": "cancelled", "message": "Token cancelled"})

@app.route("/status", methods=["GET"])
def status():
    return jsonify(doctors)

if __name__ == "__main__":
    app.run(debug=True)