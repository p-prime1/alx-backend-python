import datetime
def log_queries(func):
    def wrapper(*args, **kwargs):
        print(args, datetime.datetime)
        func()
    return wrapper       