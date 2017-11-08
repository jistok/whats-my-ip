#!/usr/bin/env python

from flask import (Flask, request, jsonify)
import os

app = Flask(__name__)
port = int(os.getenv("PORT", 8888))

@app.route("/", methods=["GET"])
def whats_my_ip():
  return request.access_route[0], 200

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=port, threaded=True)

