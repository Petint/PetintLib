__version__ = '2.1'
__all__ = ["constants", "user_int_input", "getmcpi", "random_float_generator"]
"""Module content"""

constants = {
    "tnt": 46,
    "weed": 420,
    "gridparts": ('─', '│', '┌', '┐', '└', '┘', '├', '┤', '┬', '┴', '┼')
}


def user_int_input(tries: int, message: str) -> int:
    """Hibakezelős számbekérő"""
    if tries != 0:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Nem számot adtál meg.")
            user_input = user_int_input(tries - 1, message)
        return user_input
    else:
        raise ValueError("Tul sok hibás próbálkozás.")


def getmcpi():
    """egyszerű mcpi import"""
    from mcpi.minecraft import Minecraft
    client = Minecraft.create()
    print("Import successfull.")
    client.postToChat("Import successfull.")
    return client



def random_float_generator(length: int,low: float, high: float):
    """random float generator^2"""
    import random
    return (random.uniform(low, high) for _ in range(length))
