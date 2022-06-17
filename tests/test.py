import autotable
import gagyimatek
import petint

if __name__ == '__main__':
    input("Testing autotable.py...")
    size = 5
    test_data = [[x * size + y for y in range(size)] for x in range(size)]
    print(autotable.auto(test_data))
    table1 = autotable.Table(test_data, width=3, height=2, align='cc')
    print(table1.make())

    input("Testing gagyimatek.py...")
    print(gagyimatek.osszead(5, 5))
    print(gagyimatek.kivon(5, 5))
    print(gagyimatek.szorzas(5, 5))
    print(gagyimatek.oszt(5, 5))
    print(gagyimatek.hatvany(5, 5))
    print(gagyimatek.__all__)
    input()

    input("Testing petint.py...")
    print(petint.filetofloat('asd'))
    input("Testing failed successfully.")
