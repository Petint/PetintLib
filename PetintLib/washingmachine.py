"""For cleaning Osciloscope data"""
__version__ = '1.0'


class Waveform:

    def __init__(self, file_in: str):
        """Turn saved waveforms into usable data"""
        with open(file_in, 'rt', encoding='utf-8') as du:
            data = [n.split(',') for n in du.read().splitlines()]
        keys, vaules = [f[0] for f in data[:13]], [f[1] for f in data[:12]]
        self.waveform_data = [float(f[0]) for f in data[13:]]
        for (i, v) in enumerate(vaules):
            try:
                vaules[i] = float(v)
            except (ValueError, TypeError):
                pass
        self.param = {k: v for (k, v) in zip(keys, vaules)}

    def __str__(self):
        from autotable import Table
        tab = Table(self.param)
        return tab.make()


def cal(waveform: Waveform):
    """Extracts values from the data"""
    time = [i * waveform.param['Horizontal Scale'] for i in range(int(waveform.param['Memory Length']))]
    wf = [i * waveform.param['Vertical Scale'] for i in waveform.waveform_data]
    return time, wf
