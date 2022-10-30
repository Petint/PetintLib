__version__ = '2.0.2'


class Table:
    """
table_data: 'list[list[any]]' - Data for the table

width: int - Width of a cell, auto by default

height: int - Height of cell, 1 by default.

align: str - Horizontal: 'w' for west, 'e' - for east, 'c' - for center (center is kinda iffy.)
             Vertical: 'T' for fop, 'B' for bottom, 'C' for center, ('WB' by default)

    """

    # valid kwargs: width: int = 0, height: int = 1, align: str = 'WB'
    def __init__(self, table_data: 'list[list]', **kwargs):
        """
table_data: 'list[list[any]]' - Data for the table

width: int - Width of a cell, auto by default

height: int - Height of cell, 1 by default.

align: str - Horizontal: 'w' for west, 'e' - for east, 'c' - for center (center is kinda iffy.)
                 Vertical: 'T' for fop, 'B' for bottom, 'C' for center, ('WT' by default)

        """
        w, h, a = kwargs.get('width', auto(table_data)), kwargs.get('height', 1), kwargs.get('align', 'wt')
        self._t1 = TableInternal(table_data, w, h, a)

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

    def getdatarow(self, index: int) -> str:
        r = ''
        er = len(self.tabledata[0]) * ("│" + self.item_length * " ") + "│\n"
        for ii in range(len(self.tabledata[index])):
            loclen = len(str(self.tabledata[index][ii]))
            diff = self.item_length - loclen
            r += '│'
            if self.align[0] == 'w':  # Align west
                r += f'{self.tabledata[index][ii]}' + diff * " "
            elif self.align[0] == 'e':  # Align east
                r += diff * " " + f'{self.tabledata[index][ii]}'
            elif self.align[0] == 'c':  # Align center
                """half = self.cell_height // 2
                r = (self.cell_height - half - 1) * er + r + half * er"""
                half = diff / 2
                mg = int(half) * " "  # margin
                if int(half) == half:
                    r += mg + f'{self.tabledata[index][ii]}' + mg
                else:
                    r += mg + "  " f'{self.tabledata[index][ii]}' + " " + mg
            else:
                raise ValueError(("Invalid horizontal alignment", self.align[0], "Must be 'E', 'W' or 'C'"))
        r += '│\n'
        if self.align[1] == 't':  # Horizontal align Top
            fr = r + (self.cell_height - 1) * er
        elif self.align[1] == 'b':  # Horizontal align Bottom
            fr = (self.cell_height - 1) * er + r
        elif self.align[1] == 'c':  # Horizontal align Center
            half = self.cell_height // 2
            fr = (self.cell_height - half - 1) * er + r + half * er
        else:
            raise ValueError(("Invalid vertical alignment", self.align[1], "Must be 'T', 'B' or 'C'"))
        return fr

    def getdatarow_new(self, rd):
        pass

    def getnondatarow(self, sep) -> str:
        r = sep[0]  # head: '┌┬┐' | foot: '└┴┘' | sep: '├┼┤'
        r += self.item_length * "─"
        for __i in range(len(self.tabledata[0]) - 1):
            r += sep[1]
            r += self.item_length * "─"
        r += sep[2] + '\n'
        return r

    def make(self) -> str:
        str_table = self.getnondatarow('┌┬┐')  # Head
        seprow = self.getnondatarow('├┼┤')  # Separator row
        for x in range(len(self.tabledata)):  # Main content
            str_table += self.getdatarow(x)
            if x < len(self.tabledata) - 1:
                str_table += seprow
        str_table += self.getnondatarow('└┴┘')  # Footer
        return str_table


def auto(data: 'list[list]') -> int:
    """Finds the longest entry and returns its length."""
    lengths = []
    for r in data:
        for e in r:
            lengths.append(len(str(e)))
    return max(lengths)
