import argparse
from init import init_db



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', '-i', action = 'store_true', help='initalise the db')
    parser.add_argument('--drop', '-d')
    args = parser.parse_args()
    if args.init:
        init.init_db()


if __name__ == "__main__":
    main()