from websocket import create_connection

ws = create_connection("ws://localhost:34242/test")
ws.recv()
