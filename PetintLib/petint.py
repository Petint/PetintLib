__version__ = '2.0.1'
__all__ = ["constants", "du_to_int", "getmcpi", "filetofloat", "FileImportStrList",
           "randomfoatlist"]
"""Module content"""

constants = {
    "tnt": 46,
    "weed": 420,
    "gridparts": ('─', '│', '┌', '┐', '└', '┘', '├', '┤', '┬', '┴', '┼')
}


def du_to_int(tries: int, message: str) -> int:
    """Hibakezelős számbekérő"""
    if tries != 0:
        try:
            intptszam = int(input(message))
        except ValueError:
            print("Nem számot adtál meg.")
            intptszam = du_to_int(tries - 1, message)
        return intptszam
    else:
        input("Tul sok hibás próbálkozás.")
        return 0


def getmcpi():
    """egyszerű mcpi import"""
    from mcpi.minecraft import Minecraft
    _mc = Minecraft.create()
    print("Import successfull.")
    _mc.postToChat("Import successfull.")
    return _mc


def filetofloat(file_name: str) -> 'list[float]':
    """File import hibakezeléssel
    float listaként
    """
    print("Importind data... ", end="")  # Report to DU
    try:
        input_file = open('./' + file_name, "rt")  # Get file
    except FileNotFoundError:  # If Input file doesn't exist
        raise FileNotFoundError(f"Error, {file_name} can't be found")
    else:
        """return file data as a List of floats"""
        filedata = input_file.read()  # Store file contents
        del input_file  # The variable 'input_file' is no longer needed
        file_data_list = filedata.split('\n')
        # file_data_list = file_data_list.split(',') Broken, don't use.
        del filedata  # Delete variable
        fdf = []
        for x in file_data_list:
            fdf.append(float(x))
        del file_data_list  # Delete old list
        print("Done")
        return fdf  # Return Data as a List of floats


def FileImportStrList(file_name: str) -> 'list[str]':
    """File import hibakezeléssel
    string listaként"""
    print("Importind data... ", end="")  # Report to DU
    try:
        input_file = open('./' + file_name, "rt")  # Get file
    except FileNotFoundError:  # If Input file doesn't exist
        print(f"Error, {file_name} can't be found")
        return ['a', 'b', 'c']
    else:
        """return file data as a List of floats"""
        filedata = input_file.read()  # Store file contents
        del input_file  # The variable 'input_file' is no longer needed
        file_data_list = filedata.split('\n')
        # file_data_list = file_data_list.split(',') Broken, don't use.
        del filedata  # Delete variable
        fdf = []
        for x in file_data_list:
            fdf.append(x)
        del file_data_list  # Delete old list
        print("Done")
        return fdf  # Return Data as a List of floats


def randomfoatlist(numofnums: int) -> 'list[float]':
    """generate list of random numbers"""
    import random
    out = []
    for x in range(numofnums):
        out.append(random.uniform(-10000, 10000))
    return out
