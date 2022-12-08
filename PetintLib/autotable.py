__version__ = '2.1.1'
from collections.abc import Iterable


class Table:
    """
table_data: 'list[list[any]]' - Data for the table

width: int - Width of a cell, auto by default

height: int - Height of cell, 1 by default.

align: str - Horizontal: 'w' for west, 'e' - for east, 'c' - for center (center is kinda iffy.)
             Vertical: 'T' for fop, 'B' for bottom, 'C' for center, ('WB' by default)

    """

    # valid kwargs: width: int = 0, height: int = 1, align: str = 'WB'
    def __init__(self, table_data: Iterable, **kwargs):
        """
table_data: 'list[list[any]]' - Data for the table

width: int - Width of a cell, auto by default

height: int - Height of cell, 1 by default.

align: str - Horizontal: 'w' for west, 'e' - for east, 'c' - for center (center is kinda iffy.)
                 Vertical: 'T' for fop, 'B' for bottom, 'C' for center, ('WT' by default)

        """
        if type(table_data) is dict:
            table_data = list(table_data.items())
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

    def __init__(self, td, ln, he, al):
        self.tabledata = td
        self.item_length = ln
        self.cell_height = he
        self.align = al.lower()

    def getdatarow(self, rd: list) -> str:
        # rd: RowData | r: Row | di: DataItem | fs: FrameSpace | er: EmptyRpw
        r = ''
        for di in rd:
            fs = abs(self.item_length - len(str(di)))
            r += '│'
            if self.align[0] == 'w':  # Align to west
                r += f'{di}' + fs * " "
            elif self.align[0] == 'e':  # Align to east
                r += fs * " " + f'{di}'
            elif self.align[0] == 'c':  # Aling to center
                half = self.item_length // 2
                if fs % 2 == 0:
                    r += (fs - half) * " " + f'{di}' + (fs - half) * " "
                else:
                    r += (fs - half) * " " + f'{di}' + (fs - half+1) * " "
            else:
                raise ValueError(("Invalid horizontal alignment", self.align[0], "Must be 'E', 'W' or 'C'"))
        r += '│\n'
        er = len(self.tabledata[0]) * ("│" + self.item_length * " ") + "│\n"
        if self.align[1] == 't':  # Horizontal align Top
            r = r + (self.cell_height - 1) * er
        elif self.align[1] == 'b':  # Horizontal align Bottom
            r = (self.cell_height - 1) * er + r
        elif self.align[1] == 'c':  # Horizontal align Center
            half = self.cell_height // 2
            r = (self.cell_height - half - 1) * er + r + half * er
        else:
            raise ValueError(("Invalid vertical alignment", self.align[1], "Must be 'T', 'B' or 'C'"))
        return r

    def getnondatarow(self, sep) -> str:
        ndr = sep[0]  # head: '┌┬┐' | foot: '└┴┘' | sep: '├┼┤'
        ndr += self.item_length * "─"
        for __i in range(len(self.tabledata[0]) - 1):
            ndr += sep[1]
            ndr += self.item_length * "─"
        ndr += sep[2] + '\n'
        return ndr

    def make(self) -> str:
        str_table = self.getnondatarow('┌┬┐')  # Head
        seprow = self.getnondatarow('├┼┤')  # Separator row
        for row in self.tabledata:  # Main content
            str_table += self.getdatarow(row)
            if row != self.tabledata[-1]:
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
