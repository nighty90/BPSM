#!/usr/local/bin/python3

from subprocess import run

if __name__ == "__main__":
    cap = run("efetch -h", shell=True, capture_output=True)
    print(cap.stdout.decode("utf-8"))