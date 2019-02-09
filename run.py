#!/bin/env python
import os
import blackchat
from blackchat import socketio

app = blackchat.create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)
