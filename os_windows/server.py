import xmlrpc.server
from xmlrpc.server import SimpleXMLRPCServer
import os

# Create an XML-RPC server
server = SimpleXMLRPCServer(("192.168.1.95", 8000), allow_none=True)

def send_file(filename):
    try:
        with open(filename, 'rb') as file:
            file_data = xmlrpc.client.Binary(file.read())
            return file_data
    except Exception as e:
        return str(e)

# Register the 'send_file' function
server.register_function(send_file, 'send_file')

print("Server is ready to send files.")
# Start serving requests
server.serve_forever()