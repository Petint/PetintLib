"""For cleaning Osciloscope data"""
__version__ = '1.0'

import json


def clean(file_in: str):
    """Turn saved waveforms into usable data"""
    with open(file_in, 'rt', encoding='utf-8') as du:
        data = du.read().splitlines()
    data = [n.split(',') for n in data]
    keys = [f[0] for f in data[:13]]
    vaules = [f[1] for f in data[:12]]
    waveform_data = [float(f[0]) for f in data[13:]]
    for (i, v) in enumerate(vaules):
        try:
            vaules[i] = float(v)
        except (ValueError, TypeError):
            pass
    param = {k: v for (k, v) in zip(keys, vaules)}
    return param, waveform_data


def cal(param: dict, waveform: 'list[float]'):
    """Extracts values from the data"""
    time = [i*param['Horizontal Scale'] for i in range(int(param['Memory Length']))]
    wf = [i*param['Vertical Scale'] for i in waveform]
    return time, wf
