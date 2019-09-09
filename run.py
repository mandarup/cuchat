#!/bin/env python
import os
import blackchat
from blackchat import socketio
# from flask_sslify import SSLify


app = blackchat.create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    # socketio.run(app, host='0.0.0.0', port=port, threaded=True)
    socketio.run(app, host=host, port=port)

    # if os.environ['ENV'] in ('prod', 'production'):
    #     sslify = SSLify(app=app, subdomains=True)
    #     # sslify.init_app(app)

    # app.run( host='0.0.0.0', port=port)
