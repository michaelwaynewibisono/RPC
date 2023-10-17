import xmlrpc.client

# Replace <SERVER_IP> with the IP address of the server (e.g., 192.168.1.95)
server_ip = "192.168.1.95"

# Create an XML-RPC client proxy
proxy = xmlrpc.client.ServerProxy(f"http://{server_ip}:8000")

# Ask the user for the filename to request
filename = input("Please enter the filename to request: ")

try:
    file_data = proxy.send_file(filename)

    if file_data:
        # Write the received data to a local file
        with open(f"{filename}", "wb") as file:
            file.write(file_data.data)
        print(f"File '{filename}' has been received successfully.")
    else:
        print("File request failed.")
except Exception as e:
    print(f"Error: {e}")