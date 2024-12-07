import psutil

def getMemoryInfo() -> tuple[dict, float]:
    """ Get the memory information. """
    memory_info = psutil.virtual_memory()
    
    # Convert memory values from bytes to GB
    memory_info_gb = {
        'total': int(memory_info.total / (1024 ** 3)),
        'available': int(memory_info.available / (1024 ** 3)),
        'used': int(memory_info.used / (1024 ** 3)),
        'free': int(memory_info.free / (1024 ** 3)),
        'percent': int(memory_info.percent)
    }
    return memory_info_gb

if __name__ == '__main__':
    print(getMemoryInfo())  # {'total': 15, 'available': 3, 'used': 12, 'free': 3, 'percent': 77}
