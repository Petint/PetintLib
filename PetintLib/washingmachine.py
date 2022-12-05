__version__ = '0.0.5'


def clean(file_in: str):
    with open(file_in, 'rt', encoding='utf-8') as du:
        data = du.read().splitlines()
    data = [n.split(',') for n in data]
    with open(file_in+'_clean', 'wt', encoding='utf-8') as du:
        du.write(str(data))
