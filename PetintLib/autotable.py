class Table:
    """
table_data: 'list[list[any]]' - Data for the table

width: int - Width of a cell, auto by default

height: int - Height of cell, 1 by default.

align: str - Horizontal: 'w' for west, 'e' - for east, 'c' - for center (center is kinda iffy.)
             Vertical: 'T' for fop, 'B' for bottom, 'C' for center, ('WB' by default)

    """

    def __init__(self, table_data: 'list[list]', width: int = 0, height: int = 1, align: str = 'WB'):
        """
table_data: 'list[list[any]]' - Data for the table

width: int - Width of a cell, auto by default

height: int - Height of cell, 1 by default.

align: str - Horizontal: 'w' for west, 'e' - for east, 'c' - for center (center is kinda iffy.)
                 Vertical: 'T' for fop, 'B' for bottom, 'C' for center, ('WB' by default)

        """
        if width == 0:
            width = auto(table_data)
        self._t1 = TableInternal(table_data, width, height, align)

    def make(self) -> str:
        """
        Generates the table.
        Returns string
        usage:
            1. Turn list into table: table1 = Table(data)
            2. print the table :     print(table1.make())
        """
        return self._t1.make()


class TableInternal:
    """
    Internal class
    Use facade pls
    """

    def __init__(self, table_data: 'list[list]', length: int, height: int, align: str):
        self.tabledata = table_data
        self.item_length = length
        self.cell_height = height
        self.align = align.lower()

    def getfirstrow(self) -> str:
        firstrow = '┌'
        firstrow += self.item_length * "─"
        for __i in range(len(self.tabledata[0]) - 1):
            firstrow += '┬'
            firstrow += self.item_length * "─"
        firstrow += '┐\n'
        return firstrow

    def getrow(self, index: int) -> str:
        row = ''
        erow = len(self.tabledata[0]) * ("│" + self.item_length * " ") + "│\n"
        for __i in range(len(self.tabledata[index])):
            loclen = len(str(self.tabledata[index][__i]))
            diff = self.item_length - loclen
            row += '│'
            if self.align[0] == 'w':  # Align west
                row += f'{self.tabledata[index][__i]}' + diff * " "
            elif self.align[0] == 'e':  # Align east
                row += diff * " " + f'{self.tabledata[index][__i]}'
            elif self.align[0] == 'c':  # Align center /// Credit goes to KillerCat#7249
                half = diff / 2
                mg = int(half) * " "  # margin
                if int(half) == half:
                    row += mg + f'{self.tabledata[index][__i]}' + mg
                else:
                    row += mg + "  " f'{self.tabledata[index][__i]}' + " " + mg
            else:
                raise ValueError(("Invalid horizontal alignment", self.align[0], "Must be 'E', 'W' or 'C'"))
        row += '│\n'
        if self.align[1] == 't':  # Horizontal align Top
            frow = row + (self.cell_height - 1) * erow
        elif self.align[1] == 'b':  # Horizontal align Bottom
            frow = (self.cell_height - 1) * erow + row
        elif self.align[1] == 'c':  # Horizontal align Center
            half = self.cell_height // 2
            frow = (self.cell_height - half - 1) * erow + row + half * erow
        else:
            raise ValueError(("Invalid vertical alignment", self.align[1], "Must be 'T', 'B' or 'C'"))
        return frow

    def getlastrow(self) -> str:
        lastrow = '└'
        lastrow += self.item_length * "─"
        for __i in range(len(self.tabledata[0]) - 1):
            lastrow += '┴'
            lastrow += self.item_length * "─"
        lastrow += '┘\n'
        return lastrow

    def getseprow(self) -> str:
        seprow = '├'
        seprow += self.item_length * "─"
        for __i in range(len(self.tabledata[0]) - 1):
            seprow += '┼'
            seprow += self.item_length * "─"
        seprow += '┤\n'
        return seprow

    def make(self) -> str:
        str_table = ''
        str_table += self.getfirstrow()  # Head
        sepr = self.getseprow()  # Separator row
        for x in range(len(self.tabledata)):  # Main content
            str_table += self.getrow(x)
            if x < len(self.tabledata) - 1:
                str_table += sepr
        str_table += self.getlastrow()  # Footer
        return str_table


def auto(data: 'list[list]') -> int:
    """Finds the longest entry and returns its length."""
    lengths = []
    for i in data:
        for j in i:
            lengths.append(len(str(j)))
    return max(lengths)
