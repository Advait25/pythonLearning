def one_func():
    print('one func')


if __name__ == "__main__":
    print('one.py being run directly')
    one_func()
else:
    print('one.py is imported')
