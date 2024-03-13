import typing

import numpy
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
        bits = np.multiply(glyph.as_matrix(), np.mean(m1))
        mat = np.reshape(bits, (16, 8))
        dist = compute_distance(m1, mat)
        if dist < least_dist:
            least_dist = dist
            best_approx = mat
            best_approx_char = glyph.char
    return np.reshape(best_approx, (16, 8)), best_approx_char


EPS = 0.001
def amplify_pixel(block_avg: float, block_std: float):
    def func(pixel):
        if block_std > EPS:
            std_dev_diff = (pixel - block_avg) / block_std
            if std_dev_diff > 1:
                return pixel * std_dev_diff
        return pixel

    return func


def apply_approximation(img: ndarray, glyphs: Font):
    rng = np.random.default_rng(seed=42)
    blocks_wide = img.shape[1] // 8
    blocks_high = img.shape[0] // 16
    lines = []
    for j in range(blocks_high):
        lines.append('')
        for i in range(blocks_wide):
            block = img[j * 16:(j + 1) * 16, i * 8:(i + 1) * 8]
            avg_intensity = np.mean(block)
            intensity_std = np.std(block)
            block = np.clip(
                block, # + 0.7 * (rng.random((16, 8)) - 0.5),
                0, 1)
            block = np.vectorize(amplify_pixel(avg_intensity, intensity_std))(block)
            (newblock, char) = best_approximation(block, glyphs)
            img[j * 16:(j + 1) * 16, i * 8:(i + 1) * 8] = np.multiply(newblock, avg_intensity)
            lines[j] += char
        lines[-1] += '\n'

    return lines
