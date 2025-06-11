from datetime import datetime, connect


def log_queries(func):
    def wrapper(*args, **kwargs):
        print(args, datetime.date())
        func(*args, **kwargs)

    return wrapper
