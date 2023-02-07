import PetintLib
import cProfile
import pstats


def main():
    print("Testing autotable.py...")
    size = 5
    test_data = [[x * size + y for y in range(size)] for x in range(size)]
    print("Longest data: ", PetintLib.autotable.auto(test_data))
    table1 = PetintLib.Table(test_data) #, height=3, width=3, align='cc')
    print(table1.make())


def profile():
    data = [[0x0, 0x1, 0x2, 3], [0x4, 0x5, 0x6, 0x7], [0x8, 0x9, 0xA, 0xB], [0xC, 0xD, 0xE, 0xF]]
    with cProfile.Profile() as pr:
        table = PetintLib.Table(data, height=1, align='cc')
        string_table = table.make()
        print(string_table)
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename='autotable.prof')


if __name__ == '__main__':
    main()
    profile()