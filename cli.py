import typer
import subprocess

def start_pong():
    subprocess.run(["python3", "pong.py"])

if __name__ == "__main__":
    typer.run(start_pong)
