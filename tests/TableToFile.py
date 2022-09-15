from PetintLib import Table


def main():
    size = 5
    test_data = [[x * size + y for y in range(size)] for x in range(size)]
    table1 = Table(test_data, width=3, align='wt')
    with open("table.txt", "w", encoding="utf-8") as f:
        f.write(table1.make())


if __name__ == '__main__':
    main()
