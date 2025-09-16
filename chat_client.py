import socket
import threading

HOST = "127.0.0.1"
PORT = 5002

def handle_receive(s):
    """Thread for receiving messages from server"""
    while True:
        try:
            msg = s.recv(1024).decode()
            if not msg:
                break
            print(f"\n[Onkar]: {msg}")
        except:
            break

def handle_send(s):
    """Thread for sending messages to server"""
    while True:
        try:
            msg = input("[Avinash]: ")
            s.sendall(msg.encode())
        except:
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"[+] Connected to server at {HOST}:{PORT}")

    # Start threads
    threading.Thread(target=handle_receive, args=(s,), daemon=True).start()
    threading.Thread(target=handle_send, args=(s,), daemon=True).start()

    # Keep main thread alive
    while True:
        pass
