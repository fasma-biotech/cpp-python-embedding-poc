from time import time,ctime

def date():            
    print('Today is', ctime(time()))


if __name__ == '__main__':
    date()