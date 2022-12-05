from PetintLib import washingmachine as wm
import json

def main():
    original = wm.clean('test.csv')
    with open('test.json', 'rt', encoding='utf-8') as tf:
        read = json.load(tf)
    print(read)
    if read == original:
        result = 'passed'
    else:
        result = 'failed'
    print(f"Test {result} successfully")


if __name__ == '__main__':
    main()
