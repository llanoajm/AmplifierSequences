# peppercorn_runner.py
import subprocess

class PeppercornRunner:

    def __init__(self, configuration):
        self.configuration = configuration

    def run(self):
        command = ["peppercorn", "-o", "enum.pil"]

        if self.configuration == "default":
            command.extend(["-c", "-L", "7", "--ignore-branch-4way", "main.pil"])
        elif self.configuration == "shadow":
            command = [
                "peppercorn",
                "-o",
                "enum.pil",
                "--reject-remote",
                "--ignore-branch-4way",
                "--k-slow",
                "1e-5",
                "--k-fast",
                "1e-1",
                "-c",
                "--complex-prefix",
                "EC",
                "main.pil",
            ]
        else:
            raise ValueError("Invalid configuration value. It should be 'default' or 'shadow'.")

        try:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20)  # Add timeout=60 (seconds)
        except subprocess.TimeoutExpired:
            print("Command timed out.")
            return
       
        

        if result.returncode == 0:
            print("Command executed successfully.")
            
        else:
            print("An error occurred.")
            print("Error message:", result.stderr.decode("utf-8"))


