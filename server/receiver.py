# Sairam! Sri Gurubyo Namaha!

# receiver.py
# Author: Sahanav Sai Ramesh
# Description: Receives data from the front end


# Sairam! Sri Gurubyo Namaha
# simplehttpserver.py
# Author: Sahanav Sai Ramesh
# Purpose: A web server that can collect data submitted
# Version Alpha
# NOT TO BE USED IN PRODUCTION
from http.server import BaseHTTPRequestHandler, HTTPServer
import server.serverConstants
import json
import database
hostName = server.serverConstants.HOST_NAME
port = server.serverConstants.PORT
# Required Packages: http, requests, and json

class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            database.storeItem(data)
            
        
        


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
            
        
