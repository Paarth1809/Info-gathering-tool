import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

try:
    req = requests.get("http://" + sys.argv[1])
    print("\n" + str(req.headers))

    gethostby_ = socket.gethostbyname(sys.argv[1]) 
    print("\nThe IP address of " + sys.argv[1] + " is: " + gethostby_ + "\n")

    req_two = requests.get("https://ipinfo.io/" + gethostby_ + "/json")
    resp_ = json.loads(req_two.text)

    print("Location: " + resp_.get("loc", "N/A"))
    print("Region: " + resp_.get("region", "N/A"))

except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
except socket.gaierror:
    print("Error: Invalid domain")
except json.JSONDecodeError:
    print("Error parsing JSON response")
