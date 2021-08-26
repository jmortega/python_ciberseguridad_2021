from pathlib import Path
import subprocess

source = Path("/home/linux")

cmd = ["ls", "-l", source]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
print(proc)
stdout, stderr = proc.communicate()
print(stdout.decode("utf-8").split('\n')[:-1])









