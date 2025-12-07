from flask import Flask, request, abort

app = Flask(__name__)

# Example list of valid licenses
VALID_LICENSES = {
    "ABC123",
    "XYZ789",
    "LICENSE2025"
}

@app.route("/check", methods=["GET"])
def check_license():
    key = request.args.get("key")
    if not key:
        abort(400, "License key missing")

    if key in VALID_LICENSES:
        return "License valid", 200
    else:
        return "Invalid license", 403

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
