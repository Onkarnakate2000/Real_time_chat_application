import socket
import threading

HOST = "127.0.0.1"
PORT = 5002

def handle_receive(conn):
    """Thread for receiving messages from client"""
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print(f"\n[Avinash]: {msg}")
        except:
            break

def handle_send(conn):
    """Thread for sending messages to client"""
    while True:
        try:
            msg = input("[Onkar]: ")
            conn.sendall(msg.encode())
        except:
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[*] Server listening on {HOST}:{PORT}")

    conn, addr = s.accept()
    print(f"[+] Connected by {addr}")

    # Start threads
    threading.Thread(target=handle_receive, args=(conn,), daemon=True).start()
    threading.Thread(target=handle_send, args=(conn,), daemon=True).start()

    # Keep main thread alive
    while True:
        pass
