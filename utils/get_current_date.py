from datetime import datetime

def getCurrDate(delimiter: str = '/') -> str:
    """Get the current date with a specified delimiter, default is '/'. Format: DD/MM/YYYY."""
    return datetime.now().strftime(f'%d{delimiter}%m{delimiter}%Y')