from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return "Port test page"

if __name__ == "__main__":
    print("Testing port 5000 availability...")
    
    # Test if port 5000 is available
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('0.0.0.0', 5000))
    sock.close()
    
    if result == 0:
        print("✓ Port 5000 is AVAILABLE and reachable")
    else:
        print("✗ Port 5000 is NOT reachable (this is strange!)")
    
    print("Starting Flask app on port 5000...")
    app.run(host="0.0.0.0", port=5000, debug=True)