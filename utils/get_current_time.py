from datetime import datetime

def getCurrTime(delimiter: str = ':') -> str:
    """Get the current time with a specified delimiter, default is ':'. Format: HH:MM:SS."""
    return datetime.now().strftime(f'%H{delimiter}%M{delimiter}%S')