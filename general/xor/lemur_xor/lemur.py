import pathlib

import numpy as np
import matplotlib.pyplot as plt
import imageio

here = pathlib.Path(__file__).parent


def get_flag(input_data):
    flag = np.array(imageio.imread(here / "flag.png"), dtype=np.int64)
    lemur = np.array(imageio.imread(here / "lemur.png"), dtype=np.int64)

    plt.imshow(flag ^ lemur)
    plt.show()

    return None


input_data = None
