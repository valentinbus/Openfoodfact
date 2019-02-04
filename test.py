from init import arg


def test():
    print('coucou')

arg = arg()

if __name__ == "__main__":
    if arg is True:
        arg
    else:
        test()