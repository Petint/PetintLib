from PetintLib import washingmachine as wm
import json


def main():
    param, data = wm.clean('test.csv')
    print(param, data, sep="\n")
    print(len(data))
    time, wave = wm.cal(param, data)
    print(time)


if __name__ == '__main__':
    main()
