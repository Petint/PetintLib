__version__ = '2.1.2'


class Table:
    """
table_data: 'list[list[any]]' - Data for the table

width: int - Width of a cell, auto by default

height: int - Height of cell, 1 by default.

align: str - Horizontal: 'w' for west, 'e' - for east, 'c' - for center (center is kinda iffy.)
             Vertical: 'T' for fop, 'B' for bottom, 'C' for center, ('WB' by default)

    """

    # valid kwargs: width: int = 0, height: int = 1, align: str = 'WB'
    def __init__(self, table_data: list | dict, **kwargs):
        """
table_data: 'list[list[any]]' - Data for the table

width: int - Width of a cell, auto by default

height: int - Height of cell, 1 by default.

align: str - Horizontal: 'w' for west, 'e' - for east, 'c' - for center
                 Vertical: 'T' for fop, 'B' for bottom, 'C' for center, ('WT' by default)

        """
        if type(table_data) is dict:
            table_data = list(table_data.items())
        width, height, align = kwargs.get('width', auto(table_data)), kwargs.get('height', 1), kwargs.get('align', 'wt')
        self._table = TableInternal(table_data, width, height, align)

    def make(self) -> str:
        """
        Generates the table.
        Returns string
        usage:
            1. Turn list into table: table1 = Table(data)
            2. print the table :     print(table1.make())
        """
        return self._table.make()


    def __print__(self):
        print(self.make())


class TableInternal:
    """
    Internal class
    Use facade pls
    """

    def __init__(self, tabledata, item_length, cell_height, align):
        # Should I maker this a dataclass?
        self.tabledata = tabledata
        self.item_length = item_length
        self.cell_height = cell_height
        self.align = align.lower()

    def generate_data_row(self, row_data: list) -> str:
        row = ''
        for data_item in row_data:
            frame_space = abs(self.item_length - len(str(data_item)))
            row += '│'
            if self.align[0] == 'w':  # Horizontal align west
                row += f'{data_item}' + frame_space * " "
            elif self.align[0] == 'e':  # Horizontal align east
                row += frame_space * " " + f'{data_item}'
            elif self.align[0] == 'c':  # Horizontal align center
                half_length = self.item_length // 2
                if frame_space % 2 == 0:
                    row += (frame_space - half_length) * " " + f'{data_item}' + (frame_space - half_length) * " "
                else:
                    row += (frame_space - half_length) * " " + f'{data_item}' + (frame_space - half_length + 1) * " "
            else:
                raise ValueError(("Invalid horizontal alignment", self.align[0], "Must be 'E', 'W' or 'C'"))
        row += '│\n'
        empty_row = len(self.tabledata[0]) * ("│" + self.item_length * " ") + "│\n"
        if self.align[1] == 't':  # Horizontal align Top
            row = row + (self.cell_height - 1) * empty_row
        elif self.align[1] == 'b':  # Horizontal align Bottom
            row = (self.cell_height - 1) * empty_row + row
        elif self.align[1] == 'c':  # Horizontal align Center
            half_length = self.cell_height // 2
            row = (self.cell_height - half_length - 1) * empty_row + row + half_length * empty_row
        else:
            raise ValueError(("Invalid vertical alignment", self.align[1], "Must be 'T', 'B' or 'C'"))
        return row

    def generate_separator_row(self, separator) -> str:
        nondata_row = separator[0]  # head: '┌┬┐' | foot: '└┴┘' | separator: '├┼┤'
        nondata_row += self.item_length * "─"
        for _ in range(len(self.tabledata[0]) - 1):
            nondata_row += separator[1]
            nondata_row += self.item_length * "─"
        nondata_row += separator[2] + '\n'
        return nondata_row

    def make(self) -> str:
        str_table = self.generate_separator_row('┌┬┐')  # Head
        separator_row = self.generate_separator_row('├┼┤')  # Separator row
        for row in self.tabledata:  # Main content
            str_table += self.generate_data_row(row)
            if row != self.tabledata[-1]:
                str_table += separator_row
        str_table += self.generate_separator_row('└┴┘')  # Footer
        return str_table


def auto(data):
    """Finds the longest entry and returns its length."""
    lengths = []
    for row in data:
        for entry in row:
            lengths.append(len(str(entry)))
    return max(lengths)
