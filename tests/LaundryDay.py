from PetintLib import scope as wm


def main():
    wave = wm.Waveform('test.csv')
    print(wave.param)
    print(wave)
    print(len(wave.waveform))
    print('', wave.time, wave.waveform, sep="\n")


if __name__ == '__main__':
    main()
