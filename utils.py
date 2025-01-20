import logging

def safe_execute(func):
    """
    Decorator to safely execute a function and handle errors.

    Args:
        func: The function to wrap.

    Returns:
        The wrapped function.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("An error occurred while processing your request. Please try again.")
            logging.error(f"Error in {func.__name__}: {e}")
            return None
    return wrapper