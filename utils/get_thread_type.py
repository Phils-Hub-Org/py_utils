import threading
from PySide6.QtCore import QThread, QCoreApplication

def get_thread_type() -> str:
    # Check if the current thread is a QThread or threading.Thread
    current_thread = threading.current_thread()
    
    if isinstance(current_thread, QThread):
        return 'QThread (Qt worker thread)'
    elif isinstance(current_thread, threading.Thread):
        return "threading.Thread (Python worker thread)"
    elif QThread.currentThread() == QCoreApplication.instance().thread():
        return "Qt main thread"
    elif threading.current_thread() == threading.main_thread():
        return 'Python main thread'
    else:
        return 'Unknown thread type'

# Example usage
if __name__ == '__main__':
    print(f'Running in the {get_thread_type()}')
