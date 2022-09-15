import PetintLib


def main():
    input("Testing autotable.py...")
    size = 5
    test_data = [[x * size + y for y in range(size)] for x in range(size)]
    print(PetintLib.autotable.auto(test_data))
    table1 = PetintLib.Table(test_data, width=3, height=2, align='cc')
    print(table1.make())

    input("Testing gagyimatek.py...")
    print(PetintLib.gagyimatek.osszead(5, 5))
    print(PetintLib.gagyimatek.kivon(5, 5))
    print(PetintLib.gagyimatek.szorzas(5, 5))
    print(PetintLib.gagyimatek.oszt(5, 5))
    print(PetintLib.gagyimatek.hatvany(5, 5))
    print(PetintLib.gagyimatek.__all__)
    input()

    input("Testing petint.py...")
    print(PetintLib.petint.filetofloat('asd'))
    input("Testing failed successfully.")


if __name__ == '__main__':
    main()
