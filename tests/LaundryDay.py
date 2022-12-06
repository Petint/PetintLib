from PetintLib import washingmachine as wm
import json


def main():
    param, data = wm.clean('test.csv')
    print(param, data, sep="\n")
    print(len(data))


if __name__ == '__main__':
    main()
