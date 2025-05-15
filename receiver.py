import pyaudio
import socket

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
PORT = 5000
IP = "0.0.0.0"  # Listen on all interfaces

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(1)

print("Waiting for connection...")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

try:
    while True:
        data = conn.recv(CHUNK)
        if not data:
            break
        stream.write(data)
except KeyboardInterrupt:
    print("Receiving stopped.")

stream.stop_stream()
stream.close()
p.terminate()
conn.close()
server_socket.close()
