"""
Date Utility Tool
Calculates future dates.
"""
from logs import setup_logger
from datetime import datetime, timedelta

from langchain.tools import tool

logger = setup_logger()
# for getting the future date
@tool
def future_date(days: int) -> str:
    """
    Summary:
        Calculate the date after a given number of days from today.

    Args:
        days (int): Number of days to add to the current date.

    Returns:
        str: Future date in YYYY-MM-DD format, or an error message if calculation fails.
    """
    logger.info(f"Received days input: {days}")
    try:
        target_date = datetime.today() + timedelta(days=days)
        result = target_date.strftime("%Y-%m-%d")
        logger.info(f"Calculated date: {result}")
        return result
    
    except Exception as e:
        logger.error(f"Date tool error: {e}")
        return f"Error calculating date: {str(e)}"
