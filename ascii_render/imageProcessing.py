import typing

from monobit import Font, Glyph
from numpy import ndarray, linalg as la
import numpy as np


def compute_distance(m1: ndarray, m2: ndarray):
    diff = m1 - m2
    return la.norm(diff)


def best_approximation(m1: ndarray, m2: Font):
    least_dist = float('inf')
    best_approx = None
    best_approx_char = None
    for glyph in m2.glyphs:
        if glyph.height != 16 or glyph.width != 8:
            continue
        bits = glyph.as_matrix()
        mat = np.reshape(bits, (16, 8))
        dist = compute_distance(m1, mat)
        if dist < least_dist:
            least_dist = dist
            best_approx = mat
            best_approx_char = glyph.char
    return np.reshape(best_approx, (16, 8)), best_approx_char


def apply_approximation(img: ndarray, glyphs: Font):
    blocks_wide = img.shape[1] // 8
    blocks_high = img.shape[0] // 16
    lines = []
    for j in range(blocks_high):
        lines.append('')
        for i in range(blocks_wide):
            block = img[j * 16:(j + 1) * 16, i * 8:(i + 1) * 8]
            (newblock, char) = best_approximation(block, glyphs)
            img[j * 16:(j + 1) * 16, i * 8:(i + 1) * 8] = newblock
            lines[j] += char
        lines[-1] += '\n'

    return lines
