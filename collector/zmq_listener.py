import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect("tcp://0.0.0.0:28334")
socket.setsockopt_string(zmq.SUBSCRIBE,"hashblock")

while True:
    topic, body = socket.recv_multipart()
    blockhash = body.hex()