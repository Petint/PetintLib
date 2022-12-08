from PetintLib import washingmachine as wm
import json


def main():
    wf = wm.Waveform('test.csv')
    print(wf.param)
    print(wf)
    print(len(wf.waveform_data))
    time, wave = wm.cal(wf)
    print('', time, wave, sep="\n")


if __name__ == '__main__':
    main()
