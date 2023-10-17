import xmlrpc.client

while True:
    try:
        # Create an XML-RPC client proxy
        proxy = xmlrpc.client.ServerProxy(f"http://192.168.1.95:8000")


        filename = input("Please enter the filename to request (or 'exit' to quit): ")
        if filename.lower() == 'exit':
            break

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