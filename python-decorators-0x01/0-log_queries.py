def log_queries(func):
    def wrapper(*args, **kwargs):
        print(args)
        func()
    return wrapper       