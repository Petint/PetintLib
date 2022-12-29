"""For cleaning Osciloscope data"""
__version__ = '1.1'


class Waveform:

    def __init__(self, waveform_file_in: str):
        """Turn saved waveforms into usable data"""
        with open(waveform_file_in, 'rt', encoding='utf-8') as osciloscope_waveform:
            data = [n.split(',') for n in osciloscope_waveform.read().splitlines()]
        keys, values = [f[0] for f in data[:13]], [f[1] for f in data[:12]]
        waveform_data = (float(f[0]) for f in data[13:])
        values = self._values_to_float(values)
        self.param = {key: value for (key, value) in zip(keys, values)}
        self.time = [i * self.param['Horizontal Scale'] for i in range(int(self.param['Memory Length']))]
        self.waveform = [i * self.param['Vertical Scale'] for i in waveform_data]

    @staticmethod
    def _values_to_float(values):
        for (index, value) in enumerate(values):
            try:
                values[index] = float(value)
            except (ValueError, TypeError):
                pass
        return values

    def __str__(self):
        from PetintLib import Table
        return Table(self.param).make()
