#!/usr/bin/env python3

from backend.server.server import main as server_main
from frontend.start import start as frontend_main
from multiprocessing import Process
import subprocess
from selenium import webdriver
import time
import sys
import os


if __name__ == "__main__":
    server = Process(target=server_main)
    frontend = Process(target=frontend_main)

    server.start()
    frontend.start()

    time.sleep(3)

    # open chrome in new process
    chrome_process = subprocess.Popen(
        [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "--new-window",
            "--app=http://localhost:3000",
        ]
    )

    server.join()
    frontend.join()
