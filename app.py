import socket
from uuid import getnode as get_mac
from flask import Flask, jsonify


# Device details

def getDeviceDetails():
    hostname = socket.gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    MAC_adress = get_mac()
    MAC_adress = (':'.join(("%012X" % MAC_adress)[i:i+2] for i in range (0, 12, 2)).replace(":", "-"))
    return hostname, ip, MAC_adress

app = Flask(__name__)


# Return device hostname, ip and mac address.
@app.route("/details")
def details():
    hostname,ip,mac = getDeviceDetails()
    out = "Hello I'm "+ hostname +" my mac is "+ mac+" my ip is "+ip
    return out

@app.route("/health")
def health():
    return jsonify(
        status = "up"
    )

@app.route("/")
def home():
    return "Welcome to argoCD"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug= True)


