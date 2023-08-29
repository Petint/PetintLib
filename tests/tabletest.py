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
    data = PetintLib.randbytes.randbytearray(20, 10)
    with cProfile.Profile() as pr:
        table = PetintLib.Table(data, height=1, align='wC')
        string_table = table.make()
        print(string_table)
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    stats.dump_stats(filename='autotable.prof')


if __name__ == '__main__':
    main()
    profile()