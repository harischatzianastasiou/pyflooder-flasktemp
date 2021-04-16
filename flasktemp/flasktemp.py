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
    return "This is a test"

if __name__ == "__main__":
    app.run()
