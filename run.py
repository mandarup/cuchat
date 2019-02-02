#!/bin/env python
import blackchat
from blackchat import socketio

app = blackchat.create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app)
