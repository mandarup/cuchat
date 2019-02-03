#!/bin/env python
import blackchat
from blackchat import socketio

app = blackchat.create_app()

if __name__ == '__main__':
    socketio.run(app)
