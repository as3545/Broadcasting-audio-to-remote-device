import pyaudio
import socket

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
IP = "127.0.0.1"  # Replace with remote IP if needed
PORT = 5000

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

print("Sending audio... Press Ctrl+C to stop.")

try:
    while True:
        data = stream.read(CHUNK)
        client_socket.sendall(data)
except KeyboardInterrupt:
    print("Streaming stopped.")

stream.stop_stream()
stream.close()
p.terminate()
client_socket.close()
