def use_logging(func):
    def wrapper(*args,**kwargs):
        logging.warn('%s is running'%func.__name__)
        return func(*args,**kwargs)

def bar():
    print('i am bar')

bar = use_logging(bar)
bar()