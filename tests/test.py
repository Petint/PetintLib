import PetintLib


def main():
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
