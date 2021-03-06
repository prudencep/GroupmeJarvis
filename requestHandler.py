from Jarvis import Jarvis
import os, logging
from flask import Flask, request, json

app = Flask(__name__)
jarvis = Jarvis(app.logger)
app.debug = True

@app.route('/', methods=['POST'])
def requestHandler():
    incoming = request.get_json(force=True)
    app.logger.debug(incoming)
    if incoming["name"] != "Jarvis":
        jarvis.ParseAndRespond(incoming)

    return ""