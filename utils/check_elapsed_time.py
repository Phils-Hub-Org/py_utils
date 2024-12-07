from datetime import datetime, timedelta

def checkElapsedTime(current_date: str, current_time: str, stored_date: str, stored_time: str, hours: int, minutes: int) -> bool:
    """
    Check if the specified number of hours and minutes have elapsed
    since the stored date and time.
    
    Args:
        stored_date (str): Stored date in DD/MM/YYYY format.
        stored_time (str): Stored time in HH:MM:SS format.
        hours (int): Number of hours to check.
        minutes (int): Number of minutes to check.
    
    Returns:
        bool: True if the specified time has elapsed, False otherwise.
    """
    # Combine stored date and time into a single datetime object
    stored_datetime_str = f"{stored_date} {stored_time}"
    stored_datetime = datetime.strptime(stored_datetime_str, '%d/%m/%Y %H:%M:%S')

    # Get current date and time
    curr_datetime_str = f"{current_date} {current_time}"
    curr_datetime = datetime.strptime(curr_datetime_str, '%d/%m/%Y %H:%M:%S')

    # Calculate the difference
    elapsed_time = curr_datetime - stored_datetime

    # Create a timedelta for the specified duration
    required_time = timedelta(hours=hours, minutes=minutes)

    # Check if the elapsed time is greater than or equal to the required time
    return elapsed_time >= required_time
