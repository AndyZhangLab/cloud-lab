import psutil
import datetime

now = datetime.datetime.now()
cpu = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory()

with open("system_log.txt", "a") as f:
    f.write(f"{now} | CPU: {cpu}% | Memory: {mem.percent}%\n")