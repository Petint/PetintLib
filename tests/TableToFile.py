from autotable import Table

size = 5
test_data = [[x * size + y for y in range(size)] for x in range(size)]
table1 = Table(test_data, length=3, align='c')
with open("table.txt", "w", encoding="utf-8") as f:
    f.write(table1.make())
