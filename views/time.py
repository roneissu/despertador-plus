from datetime import datetime


def get_time(fuso):
    print(fuso)
    return datetime.now().astimezone()


def test():
    print(get_time(-3))
    return 1234
