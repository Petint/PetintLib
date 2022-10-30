import PetintLib


def main():
    print("Testing autotable.py...")
    size = 5
    test_data = [[x * size + y for y in range(size)] for x in range(size)]
    print(PetintLib.autotable.auto(test_data))
    table1 = PetintLib.Table(test_data, width=4, height=3, align='cc')
    print(table1.make())


if __name__ == '__main__':
    main()
