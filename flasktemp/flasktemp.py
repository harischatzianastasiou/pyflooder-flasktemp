#!/usr/bin/python

from flask import Flask
import psutil
import pandas as pd
import time
import os
import argparse
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def main():
    return """
    <meta http-equiv="refresh" content={} />
         This is a simple flask page<br><br>.""".format(args.refresh)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("server", help="specify address and port")
    parser.add_argument("refresh", help="specify refresh rate",
                        type=int)
    args = parser.parse_args()
    app.config.update (
       SERVER_NAME=args.server)
    app.run()
