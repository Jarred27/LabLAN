import numpy as np


def transpose(ar):
    a = np.array(ar)
    size = np.shape(a)
    a = a.reshape(size[1], size[0])
    return a


if __name__ == "__main__":
    array = [[1,2,3],[4,5,6],[7,8,9]]
    c = transpose(array)
    print(c)
