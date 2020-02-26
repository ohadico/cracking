import numpy as np


def rotate90(img):
    n = len(img)
    for i in range(n - 1):
        for j in range(i + 1, n):
            img[i][j], img[j][i] = img[j][i], img[i][j]

    for i in range(n):
        for j in range(n // 2):
            img[i][j], img[i][n - j - 1] = img[i][n - j - 1], img[i][j]

    return img


def test_rotate90():
    img = np.arange(1, 10).reshape((3, 3))
    assert np.all(rotate90(np.copy(img)) == np.rot90(img, 3))
