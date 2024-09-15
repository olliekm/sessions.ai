import os
import subprocess

def start():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    subprocess.check_call("npm run dev", shell=True)

if __name__ == "__main__":
    start()
