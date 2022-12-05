__version__ = '0.0.5'
import json

def clean(file_in: str):
    with open(file_in, 'rt', encoding='utf-8') as du:
        data = du.read().splitlines()
    data = [n.split(',') for n in data]
    keys = [f[0]for f in data[:13]]
    vaules = [f[1]for f in data[:12]]
    waveform_data = [float(f[0]) for f in data[13:]]
    vaules.append(waveform_data)
    print(keys, vaules, sep='\n')
    d = {}
    for i in keys:
        for j in vaules:
            d[i] = j
    y = json.dumps(d)
    print(y)

