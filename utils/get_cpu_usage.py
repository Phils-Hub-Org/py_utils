import psutil

def getCpuUsage() -> float:
    """ Get the CPU usage. """
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

if __name__ == '__main__':
    print(getCpuUsage())  # 22.1