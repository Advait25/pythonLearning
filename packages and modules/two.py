from one import one_func

one_func()

def two_func():
    print('two func')


if __name__ == "__main__":
    print('two.py being run directly')
    two_func()
else:
    print('two.py is imported')
