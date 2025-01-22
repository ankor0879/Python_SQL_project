import sys
import logging

def safe_execute(func):
    """
    Decorator to print the message
    from the raised exception in the wrapped function.

    Args:
        func: The function to decorate.

    Returns:
        The wrapped function.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ConnectionError as e:
            print(f"Critical error: {e}")
            sys.exit(1)
        except RuntimeError as e:
            print(f"Difficulties with getting results, try another search")
            return None
        except Exception as e:
            logging.error(f"Unexpexted error: {e}")
            print(f"Difficulties with getting results, try another search")
            return None
    return wrapper
