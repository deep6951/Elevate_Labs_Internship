from flask import Flask, render_template, request
from services.abuseipdb import check_ip

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    status = None

    if request.method == "POST":

        ip = request.form["ip"]

        result = check_ip(ip)

        score = result["data"]["abuseConfidenceScore"]

        if score <= 25:
            status = "Safe"
        elif score <= 60:
            status = "Suspicious"
        else:
            status = "Malicious"

    return render_template(
        "index.html",
        result=result,
        status=status
    )

if __name__ == "__main__":
    app.run(debug=True)