import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

req = requests.get("http://"+sys.argv[1])
print("\n"+str(req.headers))

gethostby_ = socket.gethostbyname(sys.argv[1]) 
print("\nThe IP address of"+sys.argv[1]+" is: "+gethostby_ + "\n")

req_two = requests.get("https://ipinfo.io/"+gethostby_+"/json")
resp_ = json.load(req_two.text)

print("location: "+resp_["loc"])
print("region: ")

