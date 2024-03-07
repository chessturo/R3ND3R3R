from typing import List

from numpy import ndarray, linalg as la
import numpy as np

def computeDistance(m1: ndarray, m2: ndarray):
    diff = m1 - m2
    return la.norm(diff)

def bestApproximation(m1: ndarray, m2: List[List[int]]):
    least_dist = float('inf')
    best_approx = None
    for mat in m2:
        glyph = np.reshape(mat, (8, 16))
        dist = computeDistance(m1, glyph)
        if dist < least_dist:
            least_dist = dist
            best_approx = mat
    return np.reshape(best_approx, (8, 16))


def applyApproximation(img: ndarray, glyphs: List[List[int]]):
    blocks_wide = img.shape[0] // 8
    blocks_high = img.shape[1] // 16

    for i in range(blocks_wide):
        for j in range(blocks_high):
            block = img[i * 8:(i + 1) * 8, j * 16:(j + 1) * 16]
            img[i * 8:(i + 1) * 8, j * 16:(j + 1) * 16] = bestApproximation(block, glyphs)
