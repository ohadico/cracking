def rotate90(img):
    n = len(img)
    for i in range(n - 1):
        for j in range(i + 1, n):
            img[i][j], img[j][i] = img[j][i], img[i][j]

    for i in range(n):
        for j in range(n // 2):
            img[i][j], img[i][n - j - 1] = img[i][n - j - 1], img[i][j]

    return img
