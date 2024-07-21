import psutil
cpu_percent = psutil.cpu_percent(percpu=True)
print(cpu_percent)
