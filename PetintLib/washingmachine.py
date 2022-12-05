"""For cleaning Osciloscope data"""
__version__ = '1.0'

import json


def clean(file_in: str):
    with open(file_in, 'rt', encoding='utf-8') as du:
        data = du.read().splitlines()
    data = [n.split(',') for n in data]
    keys = [f[0] for f in data[:13]]
    vaules = [f[1] for f in data[:12]]
    waveform_data = [float(f[0]) for f in data[13:]]
    vaules.append(waveform_data)
    for (i, v) in enumerate(vaules):
        try:
            vaules[i] = float(v)
        except (ValueError, TypeError):
            pass
    d = {k: v for (k, v) in zip(keys, vaules)}
    y = json.dumps(d)
    print(y)
    with open(file_in.strip('.csv') + '.json', 'wt', encoding='utf-8') as js:
        js.write(y)
    return d
